/**
 * Protected Paths — vault write boundary for Pi
 *
 * Adapted from the official example that ships with pi
 * (examples/extensions/protected-paths.ts, v0.81.1).
 *
 * Policy:
 *   - write/edit inside ALLOWED_WRITE_ROOTS  -> allowed silently
 *   - write/edit to ALWAYS_BLOCKED paths     -> blocked, no prompt
 *   - write/edit anywhere else in the vault  -> confirmation dialog
 *     (blocked automatically when no UI is available, e.g. RPC/print mode)
 *   - paths outside the vault                -> blocked, no prompt
 *
 * Limitation: only the write/edit tools are gated. The bash tool can still
 * write anywhere (echo >, sed -i, ...). Pair with a bash gate if that matters.
 */

import { dirname, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

// Vault-relative, forward slashes, trailing slash on folders.
const ALLOWED_WRITE_ROOTS = ["AGENTS/12 PI/", "Inbox/"];
const ALWAYS_BLOCKED = [".git/", ".obsidian/", ".pi/", "10 CLAUDE/", ".claude/"];

// This file lives at <vault>/.pi/extensions/, so the vault root is two up.
// cwd can't be used: agents launch from their own subdirectories.
const VAULT_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");

function vaultRelative(rawPath: string, cwd: string): string | null {
	const rel = relative(VAULT_ROOT, resolve(cwd, rawPath)).replace(/\\/g, "/");
	return rel.startsWith("..") ? null : rel;
}

export default function (pi: ExtensionAPI) {
	pi.on("tool_call", async (event, ctx) => {
		if (event.toolName !== "write" && event.toolName !== "edit") {
			return undefined;
		}

		const rawPath = event.input.path as string;
		const rel = vaultRelative(rawPath, process.cwd());

		if (rel === null) {
			return { block: true, reason: `Path "${rawPath}" is outside the vault` };
		}
		if (ALWAYS_BLOCKED.some((p) => rel.startsWith(p))) {
			return { block: true, reason: `Path "${rel}" is protected` };
		}
		if (ALLOWED_WRITE_ROOTS.some((p) => rel.startsWith(p))) {
			return undefined;
		}

		if (!ctx.hasUI) {
			return { block: true, reason: `Write outside Pi workspace blocked (no UI to confirm): ${rel}` };
		}
		const ok = await ctx.ui.confirm(
			"Write outside Pi workspace",
			`Pi wants to ${event.toolName} a file outside its workspace:\n\n  ${rel}\n\nAllow?`,
		);
		return ok ? undefined : { block: true, reason: "Blocked by user" };
	});
}
