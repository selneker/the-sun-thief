// The Sun Thief — coolest-art-01 entry.
// The piece is entry.png beside this file; the grader sees exactly those bytes.
// This program copies the image to /output/entry.png (MAKEFUN_OUTPUT_DIR stands in outside the grader).
// It writes nothing else, so two runs produce the same file.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
