// Dash Builder 3D pilot: a 1969 Camaro on a turntable, then the camera climbs in through the back
// glass to the driver's seat. Loaded only for the 1969 Camaro, only with WebGL and motion allowed.
// Uses models/camaro-69.glb when it exists (see docs/dash-builder-notes.md), else a stand-in car.
import * as THREE from 'three';

const RED = 0xb3121b;
const START_YAW = 0.7; // front 3/4 view
const END_YAW = Math.PI; // rear view
const ease = (t) => t * t * (3 - 2 * t);
const span = (p, a, b) => Math.min(1, Math.max(0, (p - a) / (b - a)));

// ---- Stand-in car (meters, front toward +Z, driver on the left at +X) ----
function standIn() {
  const car = new THREE.Group();
  const paint = new THREE.MeshStandardMaterial({ name: 'Paint', color: RED, metalness: 0.45, roughness: 0.32 });
  const chrome = new THREE.MeshStandardMaterial({ color: 0xd8dde3, metalness: 1, roughness: 0.18 });
  const black = new THREE.MeshStandardMaterial({ color: 0x0c0d0f, roughness: 0.85 });
  const trim = new THREE.MeshStandardMaterial({ color: 0x1a1c20, roughness: 0.6 });
  const glass = new THREE.MeshStandardMaterial({ color: 0x0b1420, metalness: 0.3, roughness: 0.05, transparent: true, opacity: 0.45 });
  const W = 1.84;

  // Side profile (length, height), extruded across the width.
  const side = (pts, width, mat, bevel = 0.05) => {
    const shape = new THREE.Shape();
    pts.forEach(([u, v], i) => (i ? shape.lineTo(u, v) : shape.moveTo(u, v)));
    const geo = new THREE.ExtrudeGeometry(shape, { depth: width, bevelEnabled: bevel > 0, bevelSize: bevel, bevelThickness: bevel, bevelSegments: 3, curveSegments: 16 });
    geo.rotateY(-Math.PI / 2);
    geo.translate(width / 2, 0, 0);
    return new THREE.Mesh(geo, mat);
  };

  const body = new THREE.Shape();
  body.moveTo(-2.33, 0.3);
  body.lineTo(-2.36, 0.66);
  body.lineTo(-2.3, 0.8);
  body.lineTo(-1.45, 0.86);
  body.lineTo(0.75, 0.88);
  body.lineTo(2.2, 0.83);
  body.lineTo(2.36, 0.74);
  body.lineTo(2.33, 0.3);
  body.lineTo(1.8, 0.3);
  body.absarc(1.38, 0.34, 0.42, 0, Math.PI, false);
  body.lineTo(-0.96, 0.3);
  body.absarc(-1.38, 0.34, 0.42, 0, Math.PI, false);
  body.lineTo(-2.33, 0.3);
  const bodyGeo = new THREE.ExtrudeGeometry(body, { depth: W, bevelEnabled: true, bevelSize: 0.06, bevelThickness: 0.06, bevelSegments: 4, curveSegments: 20 });
  bodyGeo.rotateY(-Math.PI / 2);
  bodyGeo.translate(W / 2, 0, 0);
  car.add(new THREE.Mesh(bodyGeo, paint));

  // Glass greenhouse and roof
  car.add(side([[-1.45, 0.86], [-0.45, 1.34], [0.22, 1.36], [0.78, 0.88]], 1.5, glass, 0.02));
  const roof = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.04, 0.72), paint);
  roof.position.set(0, 1.36, -0.1);
  car.add(roof);

  // Hood stripes
  [-0.16, 0.16].forEach((x) => {
    const stripe = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.01, 1.35), new THREE.MeshStandardMaterial({ color: 0xf2f2ee, roughness: 0.4 }));
    stripe.position.set(x, 0.92, 1.5);
    stripe.rotation.x = 0.035;
    car.add(stripe);
  });

  // Bumpers, grille, lights
  [[2.42, 0.48], [-2.42, 0.5]].forEach(([z, y]) => {
    const b = new THREE.Mesh(new THREE.BoxGeometry(1.86, 0.1, 0.1), chrome);
    b.position.set(0, y, z);
    car.add(b);
  });
  const grille = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.2, 0.04), black);
  grille.position.set(0, 0.62, 2.39);
  car.add(grille);
  [-0.62, 0.62].forEach((x) => {
    const head = new THREE.Mesh(new THREE.CircleGeometry(0.09, 20), new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0xfff3d6, emissiveIntensity: 0.6 }));
    head.position.set(x, 0.63, 2.415);
    car.add(head);
    const tail = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.11, 0.03), new THREE.MeshStandardMaterial({ color: 0x400000, emissive: 0xff1a1a, emissiveIntensity: 0.7 }));
    tail.position.set(x, 0.68, -2.41);
    car.add(tail);
  });

  // Wheels
  const tireGeo = new THREE.CylinderGeometry(0.34, 0.34, 0.26, 28).rotateZ(Math.PI / 2);
  const hubGeo = new THREE.CylinderGeometry(0.21, 0.21, 0.27, 20).rotateZ(Math.PI / 2);
  [[0.82, 1.38], [-0.82, 1.38], [0.82, -1.38], [-0.82, -1.38]].forEach(([x, z]) => {
    const tire = new THREE.Mesh(tireGeo, black);
    tire.position.set(x, 0.34, z);
    const hub = new THREE.Mesh(hubGeo, chrome);
    hub.position.copy(tire.position);
    car.add(tire, hub);
  });

  // Interior: floor, seats, dash, cluster and wheel
  const floor = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.04, 2.0), trim);
  floor.position.set(0, 0.965, -0.3);
  car.add(floor);
  [0.38, -0.38].forEach((x) => {
    const seat = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.1, 0.5), trim);
    seat.position.set(x, 1.03, -0.25);
    const back = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.2, 0.1), trim);
    back.position.set(x, 1.07, -0.55);
    back.rotation.x = -0.18;
    car.add(seat, back);
  });
  const dash = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.24, 0.36), black);
  dash.position.set(0, 1.0, 0.66);
  car.add(dash);
  const pod = new THREE.Mesh(new THREE.BoxGeometry(0.62, 0.22, 0.06), trim);
  pod.position.set(0.38, 1.06, 0.47);
  pod.rotation.x = -0.2;
  car.add(pod);
  const wheel = new THREE.Mesh(new THREE.TorusGeometry(0.19, 0.018, 10, 40), black);
  wheel.position.set(0.38, 1.0, 0.22);
  wheel.rotation.x = -0.45;
  car.add(wheel);

  return { car, eye: new THREE.Vector3(0.38, 1.22, -0.15), cluster: new THREE.Vector3(0.38, 1.05, 0.47) };
}

// ---- Real model ----
async function loadModel(base, url) {
  const [{ GLTFLoader }, { DRACOLoader }] = await Promise.all([import(`${base}GLTFLoader.min.js`), import(`${base}DRACOLoader.min.js`)]);
  const draco = new DRACOLoader().setDecoderPath(`${base}draco/`);
  const gltf = await new GLTFLoader().setDRACOLoader(draco).loadAsync(url);
  draco.dispose();
  const model = gltf.scene;
  model.traverse((o) => {
    if (!o.isMesh) return;
    (Array.isArray(o.material) ? o.material : [o.material]).forEach((m) => { if (m.name === 'Paint') m.color.setHex(RED); });
  });
  // Center the car on the ground so the camera path fits any origin the artist used.
  const box = new THREE.Box3().setFromObject(model);
  const center = box.getCenter(new THREE.Vector3());
  model.position.set(-center.x, -box.min.y, -center.z);
  const car = new THREE.Group();
  car.add(model);
  car.updateMatrixWorld(true);
  const eye = car.getObjectByName('DriverEye');
  const cluster = car.getObjectByName('Cluster');
  if (!eye || !cluster) throw new Error('camaro-69.glb needs empties named DriverEye and Cluster');
  return { car, eye: eye.getWorldPosition(new THREE.Vector3()), cluster: cluster.getWorldPosition(new THREE.Vector3()) };
}

export async function mount({ canvas, stage, base, model }) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0e0f11);
  scene.fog = new THREE.Fog(0x0e0f11, 14, 30);
  scene.add(new THREE.HemisphereLight(0xdfe8ff, 0x16181c, 1.3));
  const key = new THREE.DirectionalLight(0xffffff, 2.4);
  key.position.set(5, 8, 6);
  const rim = new THREE.DirectionalLight(0x7dbbff, 1.6);
  rim.position.set(-6, 4, -6);
  scene.add(key, rim);
  const ground = new THREE.Mesh(new THREE.CircleGeometry(12, 64), new THREE.MeshStandardMaterial({ color: 0x16181c, roughness: 0.95 }));
  ground.rotation.x = -Math.PI / 2;
  const shadow = new THREE.Mesh(new THREE.CircleGeometry(1, 48), new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.55 }));
  shadow.rotation.x = -Math.PI / 2;
  shadow.scale.set(1.25, 2.7, 1);
  shadow.position.y = 0.005;
  scene.add(ground, shadow);

  let rig = null;
  if (model) {
    try { rig = await loadModel(base, model); } catch { rig = null; }
  }
  if (!rig) rig = standIn();
  const { car, eye, cluster } = rig;
  scene.add(car);

  const camera = new THREE.PerspectiveCamera(36, 1, 0.05, 60);
  const start = new THREE.Vector3();
  const startLook = new THREE.Vector3(0, 0.62, 0);
  let path = null;
  const look = new THREE.Vector3();
  const world = (v) => car.localToWorld(v.clone());

  // The climb-in path, in car space at the rear view: back off behind the car, through the back
  // glass, to the driver's eye.
  const buildPath = () => {
    car.rotation.y = END_YAW;
    car.updateMatrixWorld(true);
    path = new THREE.CatmullRomCurve3([
      start.clone(),
      world(new THREE.Vector3(eye.x * 0.3, eye.y + 0.35, eye.z - 3.2)),
      world(new THREE.Vector3(eye.x * 0.7, eye.y + 0.02, eye.z - 1.0)),
      world(eye),
    ], false, 'centripetal');
  };

  let progress = 0;
  const pose = () => {
    const turn = ease(span(progress, 0, 0.42));
    const climb = ease(span(progress, 0.46, 0.8));
    car.rotation.y = START_YAW + (END_YAW - START_YAW) * turn;
    car.updateMatrixWorld(true);
    if (climb > 0) {
      camera.position.copy(path.getPoint(climb));
      look.lerpVectors(startLook, world(cluster), ease(span(climb, 0.35, 1)));
    } else {
      camera.position.copy(start);
      look.copy(startLook);
    }
    camera.fov = 36 + 22 * climb;
    camera.updateProjectionMatrix();
    camera.lookAt(look);
  };

  let visible = false;
  let queued = false;
  const draw = () => {
    queued = false;
    if (!visible) return;
    pose();
    renderer.render(scene, camera);
  };
  const request = () => {
    if (queued || !visible) return;
    queued = true;
    requestAnimationFrame(draw);
  };

  const resize = () => {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    // Tall phone screens need the camera further back to fit the whole car.
    const dist = camera.aspect < 1 ? 8.4 / Math.max(camera.aspect, 0.45) : 8.2;
    start.set(0, 1.9, Math.min(dist, 17));
    buildPath();
    request();
  };
  new ResizeObserver(resize).observe(canvas);
  // Only render while the stage is on screen.
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    request();
  }).observe(stage);
  resize();

  return {
    setProgress(p) {
      progress = p;
      request();
    },
  };
}
