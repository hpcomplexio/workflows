# Exercise 5: Recovery

## Goal
Learn to recover from mistakes using undo, track, and untrack.

---

## Part 1: Undo

**Undo** reverses the most recent Graphite operation.

### Step 1: Do something you'll undo
```bash
gt checkout main
echo "oops" > oops.txt && git add . && gt create -m "mistake"
gt log
```

### Step 2: Undo it
```bash
gt undo
```

### Step 3: Verify
```bash
gt log
```
The branch is gone. Your working directory is back to its previous state.

### What can you undo?
- `gt create`
- `gt modify`
- `gt fold`
- `gt move`
- `gt reorder`
- Most other Graphite operations

### Tip
If you're unsure about an operation, just try it. You can always `gt undo`.

---

## Part 2: Track and Untrack

### Tracking an Existing Branch

If you created a branch with regular git (not Graphite), you can add it to your stack:

### Step 1: Create a regular git branch
```bash
gt checkout main
git checkout -b my-regular-branch
echo "content" > regular.txt
git add . && git commit -m "regular commit"
```

### Step 2: Track it with Graphite
```bash
gt track
```
Now this branch is part of your Graphite stack.

### Step 3: Verify
```bash
gt log
```

---

### Untracking a Branch

If you want to remove a branch from Graphite's tracking (but keep it in git):

### Step 1: Go to the branch
```bash
gt checkout <branch-name>
```

### Step 2: Untrack it
```bash
gt untrack
```

### Step 3: Verify
```bash
gt log        # Branch won't appear
git branch    # Branch still exists in git
```

---

## Part 3: Recovery Scenarios

### Scenario A: "I created a branch by mistake"
```bash
gt undo
```

### Scenario B: "I folded the wrong branches"
```bash
gt undo
```

### Scenario C: "I made a git branch but want it in my stack"
```bash
gt track
```

### Scenario D: "I want to manage this branch with regular git"
```bash
gt untrack
```

### Scenario E: "I messed up and undo isn't enough"
```bash
# Git's reflog is your friend
git reflog
git reset --hard <commit-hash>
```

---

## Summary

| Command | What it does |
|---------|--------------|
| `gt undo` | Reverse the last Graphite operation |
| `gt track` | Start tracking a git branch with Graphite |
| `gt untrack` | Stop tracking (branch stays in git) |

---

## Tips

1. **Use `gt undo` liberally** - It's safe and fast
2. **Check `gt log` often** - Know your state before and after operations
3. **When in doubt, `gt sync`** - Gets you back to a known good state
4. **Git reflog is the ultimate safety net** - Even if Graphite can't help, git remembers everything

---

## Congratulations!

You've completed all the exercises. You now know how to:
- View and create stacked branches
- Navigate through your stack
- Sync and submit PRs
- Reorganize your stack
- Recover from mistakes

For a quick reference, see [graphite-commands.md](../graphite-commands.md).
