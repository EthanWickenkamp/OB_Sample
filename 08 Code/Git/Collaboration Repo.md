
# GitHub Private Repo Collaboration

Start-to-finish flow for being added as a collaborator on someone else's private GitHub repo.

## The Flow

1. **Owner creates the repo as private.** Lives under his personal GitHub account (not an org).
2. **Owner invites collaborators by email.** GitHub sends an invite link; you click it while logged in to your own GitHub account and accept.
3. **Owner's tokens belong to him, not the repo.** Any Personal Access Token he generates is tied to *his* GitHub account. He can't "attach" a token to the repo for you to use.
4. **You make your own tokens.** Because your GitHub account now has access to the repo, any PAT you generate under *your* account settings automatically inherits that access. You never touch his tokens.
5. **Owner can promote you to Admin.** Once you're listed as a collaborator, he changes your role in the repo settings (see below).

## How the Owner Grants Admin

On GitHub.com:

- **Repo → Settings → Collaborators → Manage access**
- Find your name in the list.
- Click the role dropdown (currently Read or Write) → select **Admin** → confirm.
- Change is instant; you get an email notification.

Only the owner/admin sees the Settings tab. You won't see it yourself until he promotes you.

## Role Ladder (Personal Repo)

Read → Triage → Write → Maintain → **Admin**

| Capability | Required Role |
|---|---|
| Clone, pull | Read |
| Push commits | Write |
| Manage issues/PRs | Triage / Maintain |
| Add deploy keys, webhooks, branch protection | Admin |
| Change repo settings | Admin |
| **Invite new collaborators** | **Owner only** (on personal repos) |

## Deploy Keys vs Personal Access Tokens

- **Deploy key** = an SSH public key attached to a specific repo, grants access without a user account. Only **Admin** can add/remove them.
- **Personal Access Token (PAT)** = tied to *your* GitHub account, inherits your account's permissions across all repos you have access to. You generate these in your own account settings (`Settings → Developer settings → Personal access tokens`).

If you just want to clone/push from a new machine, generate your own PAT — you don't need a deploy key.

## The Catch on Personal Repos

Even as **Admin** on a personal repo, you **cannot invite new collaborators**. That power stays with the owner, always. If multiple people need to share gatekeeping duties, the repo needs to live in a **GitHub Organization** instead — in an org, Admin role on a repo *does* let you invite others (subject to org-level member privilege settings).

## Summary

- Repo access is attached to your GitHub *account*, not to tokens or keys.
- You generate your own PAT under your own account.
- Owner promotes you via Settings → Collaborators → role dropdown → Admin.
- Admin on a personal repo = full settings control, but still can't invite others.
- Move to an org if you need shared invite power.

