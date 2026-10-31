"""Build redesign/models/camaro-69.glb for the Dash Builder 3D pilot from the source .blend.

Run with Blender 4.5 (headless), from the repo root:
  blender -b --disable-autoexec <Chevrolet Camaro 1969.blend> --python tools/build_camaro_glb.py -- redesign/models/camaro-69.glb
The source file is not kept in the repo (see "Rules for camaro-69.glb" in docs/dash-builder-notes.md).
"""
import sys

import bpy
from mathutils import Vector

OUT = sys.argv[sys.argv.index('--') + 1]
LENGTH = 4.72  # meters, a 1969 Camaro bumper to bumper
TEX_MAX = 1024

scene = bpy.context.scene
for o in list(scene.objects):
    if o.type == 'MESH' and not o.visible_get():
        bpy.data.objects.remove(o)
root = next(o for o in scene.objects if o.parent is None)
root.name = 'Camaro69'
meshes = [o for o in scene.objects if o.type == 'MESH']


def bounds(objs):
    pts = [o.matrix_world @ Vector(c) for o in objs for c in o.bound_box]
    return (Vector([min(p[i] for p in pts) for i in range(3)]), Vector([max(p[i] for p in pts) for i in range(3)]))


def mats(o):
    return {s.material.name for s in o.material_slots if s.material}


# ---- Materials: the source uses procedural node groups glTF can't carry, so rebuild those as plain
# Principled BSDFs with the group's own color and roughness. Materials already built on a Principled
# BSDF (textures, plastics, glass) are kept.
METAL = ('chrome', 'alumin', 'metal', 'brake disc', 'reflector')


def val(s):
    v = s.default_value
    return tuple(v) if hasattr(v, '__len__') else v


for m in bpy.data.materials:
    nt = m.node_tree
    if not nt:
        continue
    out = next((n for n in nt.nodes if n.type == 'OUTPUT_MATERIAL' and n.is_active_output), None)
    if not out or not out.inputs['Surface'].is_linked:
        continue
    src = out.inputs['Surface'].links[0].from_node
    name = m.name.lower()
    if src.type == 'BSDF_PRINCIPLED' and name != 'rear glass':
        p = src
        # Transmission costs an extra render pass per frame in three.js; plain alpha is enough here.
        if p.inputs['Transmission Weight'].default_value > 0:
            p.inputs['Transmission Weight'].default_value = 0
            p.inputs['Alpha'].default_value = 0.6
            m.surface_render_method = 'BLENDED'
        continue
    color, rough, group = None, None, ''
    if src.type == 'GROUP':
        group = (src.node_tree.name + src.name).lower()
        for s in src.inputs:
            if s.is_linked or not hasattr(s, 'default_value'):
                continue
            n = s.name.lower()
            if color is None and 'color' in n and len(val(s)) == 4:
                color = val(s)
            if rough is None and 'rough' in n and 'clearcoat' not in n and 'flake' not in n:
                rough = val(s)
    if color is None:
        color = tuple(m.diffuse_color)
    met = 1.0 if any(k in name for k in METAL) else 0.0
    paint = 'carpaint' in name
    if 'chrome' in name:
        color, rough = (0.9, 0.9, 0.9, 1), 0.05
    if paint or 'carpaint' in group:
        met, rough = max(met, 0.6), 0.3
    emit = 'glass' not in name and any(k in group + name for k in ('light', 'glow', 'emiss', 'drl'))
    nt.nodes.clear()
    o = nt.nodes.new('ShaderNodeOutputMaterial')
    p = nt.nodes.new('ShaderNodeBsdfPrincipled')
    nt.links.new(p.outputs[0], o.inputs['Surface'])
    p.inputs['Base Color'].default_value = color
    p.inputs['Metallic'].default_value = met
    p.inputs['Roughness'].default_value = 0.5 if rough is None else rough
    if paint:
        p.inputs['Coat Weight'].default_value = 1.0
        p.inputs['Coat Roughness'].default_value = 0.03
    if emit:
        p.inputs['Emission Color'].default_value = color
        p.inputs['Emission Strength'].default_value = 2.0
    if 'glass' in name:
        p.inputs['Base Color'].default_value = (0.9, 0.9, 0.9, 1)
        p.inputs['Roughness'].default_value = 0.05
        p.inputs['Alpha'].default_value = 0.25
        m.surface_render_method = 'BLENDED'
    if paint:
        m.name = 'Paint'  # the page recolors this material

# Single-sided faces so the camera sees out from inside. Glass stays double-sided (it is see-through
# either way, and one layer per window must show from both sides).
for m in bpy.data.materials:
    m.use_backface_culling = 'glass' not in m.name.lower()

# Windows are stacked two or three times in the source (identical bounds). Keep one layer each so the
# glass reads as glass and the climb-in goes through a single pane.
seen = {}
for o in sorted(meshes, key=lambda o: o.name):
    if not any('glass' in m.lower() for m in mats(o)):
        continue
    lo, hi = bounds([o])
    key = tuple(round(v, 2) for v in (*lo, *hi))
    if key in seen:
        bpy.data.objects.remove(o)
    else:
        seen[key] = o
meshes = [o for o in scene.objects if o.type == 'MESH']

# ---- Geometry: the body, glass and cabin stay as they are (custom normals intact). The heavy wheel
# parts take the cuts; the brake discs (half the source triangles) sit behind the wheel covers.
lo, hi = bounds(meshes)
for o in meshes:
    olo, ohi = bounds([o])
    c = (olo + ohi) / 2
    tris = sum(len(p.vertices) - 2 for p in o.data.polygons)
    names = {m.lower() for m in mats(o)}
    cabin = abs(c.x) < 0.5 and -0.6 < c.y < 1.1 and c.z > 0.25
    if tris < 2000 or cabin or any('paint' in m or 'glass' in m for m in names):
        continue
    ratio = 2500 / tris if any('brake disc' in m for m in names) else min(1.0, (500 / tris) ** 0.5)
    if ratio < 0.98:
        o.modifiers.new('Decimate', 'DECIMATE').ratio = ratio

# ---- Textures: at most 1024 px, written as WebP by the exporter.
for img in bpy.data.images:
    if img.size[0] > TEX_MAX or img.size[1] > TEX_MAX:
        img.scale(min(img.size[0], TEX_MAX), min(img.size[1], TEX_MAX))

# ---- Camera targets, measured in the source cabin (before scaling). Cluster: the center of the
# gauge faces (the mesh with the Dash texture), on the driver side (+X). DriverEye: in line with
# the cluster, just ahead of the front seat back (y 0.14) and about 1.05 m above the ground (z 0.76).
glo, ghi = bounds([max((o for o in meshes if 'Dash' in mats(o)), key=lambda o: len(o.data.polygons))])
targets = {'Cluster': (glo + ghi) / 2}
targets['DriverEye'] = Vector((targets['Cluster'].x, 0.14, 0.76))

# ---- Scale to real size (meters). The front already faces -Y in Blender, which is +Z in glTF.
lo, hi = bounds(meshes)
k = LENGTH / (hi.y - lo.y)
origin = root.matrix_world.translation.copy()
root.scale *= k
bpy.context.view_layer.update()
for name, p in targets.items():
    e = bpy.data.objects.new(name, None)
    scene.collection.objects.link(e)
    e.location = origin + (p - origin) * k
    e.empty_display_size = 0.05

lo, hi = bounds(meshes)
print('SIZE', tuple(round(v, 3) for v in hi - lo), 'TARGETS', {n: tuple(round(v, 3) for v in bpy.data.objects[n].location) for n in targets})
bpy.ops.export_scene.gltf(
    filepath=OUT, export_format='GLB', use_visible=True, export_apply=True,
    export_draco_mesh_compression_enable=True, export_draco_mesh_compression_level=6,
    export_image_format='WEBP', export_image_quality=85)
