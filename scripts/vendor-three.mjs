// Copies the pinned three.js files the Dash Builder needs into redesign/js/vendor/three/<version>/.
// Run after `npm install`: node scripts/vendor-three.mjs
import { build } from 'esbuild';
import { copyFile, mkdir, readFile, rm } from 'node:fs/promises';

const pkg = JSON.parse(await readFile('node_modules/three/package.json', 'utf8'));
const src = 'node_modules/three';
const out = `redesign/js/vendor/three/${pkg.version}`;
await rm(out, { recursive: true, force: true });
await mkdir(`${out}/draco`, { recursive: true });

const common = { bundle: true, minify: true, format: 'esm', target: 'es2020', legalComments: 'eof', logLevel: 'warning' };
// three.js itself, as one file (0.18x splits it into module + core and no longer ships a .min build).
await build({ ...common, entryPoints: [`${src}/build/three.module.js`], outfile: `${out}/three.module.min.js` });
// Loaders keep importing 'three', which the page's import map points at the file above.
await build({ ...common, entryPoints: [`${src}/examples/jsm/loaders/GLTFLoader.js`], outfile: `${out}/GLTFLoader.min.js`, external: ['three'] });
await build({ ...common, entryPoints: [`${src}/examples/jsm/loaders/DRACOLoader.js`], outfile: `${out}/DRACOLoader.min.js`, external: ['three'] });
for (const f of ['draco_wasm_wrapper.js', 'draco_decoder.wasm']) await copyFile(`${src}/examples/jsm/libs/draco/gltf/${f}`, `${out}/draco/${f}`);
await copyFile(`${src}/LICENSE`, `${out}/LICENSE`);
process.stdout.write(`three ${pkg.version} -> ${out}\n`);
