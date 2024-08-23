import { defineConfig } from 'tsup'

export default defineConfig({
	entry: ['./gen/typescript/**/*.ts'],
	splitting: false,
	sourcemap: true,
	bundle: false,
	clean: true,
	shims: true,
	format: ["esm", "cjs"],
	legacyOutput: false,
	dts: true,
	target: 'es2022'
})
