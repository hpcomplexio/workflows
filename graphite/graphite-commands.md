# Graphite CLI Quick Reference

## Viewing

| Command | Description |
|---------|-------------|
| `gt log` | Visualize your stack |
| `gt ls` | List all tracked branches |

## Creating

| Command | Description |
|---------|-------------|
| `gt create -m "msg"` | Create new branch in stack |
| `gt modify` | Amend current branch |
| `gt modify -m "msg"` | Amend with new message |

## Navigation

| Command | Description |
|---------|-------------|
| `gt checkout <branch>` | Switch to branch |
| `gt up` | Move up the stack |
| `gt down` | Move down the stack |
| `gt top` | Jump to top of stack |
| `gt bottom` | Jump to bottom of stack |

## Syncing

| Command | Description |
|---------|-------------|
| `gt sync` | Rebase stack on trunk |
| `gt submit` | Create/update PRs |
| `gt ss` | Submit entire stack (shortcut) |

## Reorganizing

| Command | Description |
|---------|-------------|
| `gt fold` | Merge branch above into current |
| `gt pop` | Remove branch, keep changes |
| `gt move --onto <branch>` | Move to different parent |
| `gt reorder` | Reorder branches |
| `gt split` | Split current commit |
| `gt squash` | Combine commits on branch |
| `gt absorb` | Auto-distribute staged changes |

## Recovery

| Command | Description |
|---------|-------------|
| `gt undo` | Reverse the last Graphite operation |
| `gt track` | Start tracking branch |
| `gt untrack` | Stop tracking branch |

## Collaboration

| Command | Description |
|---------|-------------|
| `gt get <pr>` | Download a PR's stack |
| `gt freeze` | Lock branch from changes |
| `gt unfreeze` | Unlock branch |
