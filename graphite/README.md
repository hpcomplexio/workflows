# Graphite CLI Playground

A hands-on playground for learning [Graphite](https://graphite.dev) stacked diffs workflow.

## Getting Started

1. Make sure Graphite CLI is installed: `brew install withgraphite/tap/graphite`
2. Run `gt log` to see your current stack
3. Start with [Exercise 01](exercises/01-viewing-creating.md)

## Exercises

| Exercise | Focus |
|----------|-------|
| [01 - Viewing & Creating](exercises/01-viewing-creating.md) | `gt log`, `gt create`, `gt modify` |
| [02 - Navigation](exercises/02-navigation.md) | `gt up`, `gt down`, `gt top`, `gt bottom` |
| [03 - Syncing & Submitting](exercises/03-syncing-submitting.md) | `gt sync`, `gt submit` |
| [04 - Reorganizing](exercises/04-reorganizing.md) | `gt fold`, `gt pop`, `gt move`, `gt squash` |
| [05 - Recovery](exercises/05-recovery.md) | `gt undo`, `gt track`, `gt untrack` |

## Quick Reference

See [graphite-commands.md](graphite-commands.md) for a command cheatsheet.

## Tips

- Run `gt log` constantly to understand your stack state
- Use `gt undo` liberally - it's safe and fast
- Don't be afraid to delete branches and start over - that's what playgrounds are for
