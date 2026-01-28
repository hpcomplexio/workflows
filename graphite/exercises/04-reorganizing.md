# Exercise 4: Reorganizing Your Stack

## Goal
Learn to restructure your stack by folding, popping, moving, and squashing branches.

## Prerequisites
A stack with at least 3 branches.

---

## Part 1: Folding Branches

**Fold** combines the branch above you into your current branch.

### Scenario
You have: A -> B -> C
You realize A and B should be one commit.

### Step 1: Go to the lower branch
```bash
gt checkout A
# or
gt bottom
```

### Step 2: Fold the branch above into current
```bash
gt fold
```
This merges B's changes into A. Your stack is now: A -> C

### Step 3: Verify
```bash
gt log
```

---

## Part 2: Popping a Branch

**Pop** removes the current branch from the stack but keeps your changes as uncommitted files.

### Step 1: Go to a branch you want to remove
```bash
gt checkout <branch-name>
```

### Step 2: Pop it
```bash
gt pop
```
The branch is removed, but your changes are still in the working directory (unstaged).

### Step 3: Decide what to do with the changes
```bash
git status  # See the uncommitted changes
# Option A: Discard them
git checkout .
# Option B: Add them to a different branch
gt checkout <other-branch>
git add . && gt modify
```

---

## Part 3: Moving a Branch

**Move** changes a branch's parent.

### Scenario
You have: A -> B -> C
You want: A -> C (with B moved elsewhere or based directly on main)

### Step 1: Go to the branch you want to move
```bash
gt checkout B
```

### Step 2: Move it onto a different parent
```bash
gt move --onto main
```
Now B is based on main instead of A.

### Step 3: Verify the new structure
```bash
gt log
```

---

## Part 4: Squashing Commits

**Squash** combines multiple commits on the current branch into one.

### When to use
If you made multiple commits on one branch and want to clean them up.

### Step 1: Check your commits
```bash
git log --oneline -5
```

### Step 2: Squash them
```bash
gt squash
```
This combines all commits on the current branch into a single commit.

---

## Part 5: Reordering Branches

**Reorder** lets you change the order of branches in your stack.

### Step 1: View current order
```bash
gt log
```

### Step 2: Reorder interactively
```bash
gt reorder
```
Follow the prompts to rearrange your stack.

---

## Part 6: Absorb (Advanced)

**Absorb** automatically distributes staged changes to the correct commits in your stack.

### Scenario
You're at the top of your stack and realize you need to fix something that belongs in an earlier branch.

### Step 1: Make the fix
```bash
# Edit a file that was introduced in an earlier branch
echo "fix" >> config.md
git add config.md
```

### Step 2: Absorb the changes
```bash
gt absorb
```
Graphite figures out which branch introduced that file and adds your fix there.

### Step 3: Verify
```bash
gt log
gt checkout <earlier-branch>
git log -1  # See the fix was absorbed
```

---

## Summary

| Command | What it does |
|---------|--------------|
| `gt fold` | Merge branch above into current |
| `gt pop` | Remove branch, keep changes uncommitted |
| `gt move --onto <branch>` | Change parent branch |
| `gt squash` | Combine commits on current branch |
| `gt reorder` | Reorder branches in stack |
| `gt absorb` | Auto-distribute staged changes |

---

## Common Reorganization Scenarios

### "These two branches should be one"
```bash
gt checkout <lower-branch>
gt fold
```

### "This branch doesn't belong in this stack"
```bash
gt checkout <branch>
gt move --onto main
```

### "I need to remove this branch entirely"
```bash
gt checkout <branch>
gt pop
git checkout .  # discard changes
```

### "I committed to the wrong branch"
```bash
git add <files>
gt absorb  # Let Graphite figure it out
```

---

Next: [Exercise 05 - Recovery](./05-recovery.md)
