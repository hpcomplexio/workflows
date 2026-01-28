# Exercise 3: Syncing and Submitting

## Goal
Learn to keep your stack in sync with the remote and submit PRs.

## Prerequisites
- A stack with at least 2 branches (from previous exercises)
- Push access to the remote repository

---

## Part 1: Syncing Your Stack

### What `gt sync` does:
1. Pulls the latest changes from trunk (main)
2. Rebases your entire stack on top of trunk
3. Cleans up any branches that have been merged

### Step 1: Sync your stack
```bash
gt sync
```

### Step 2: View the result
```bash
gt log
```
Your stack is now rebased on the latest main.

---

## Part 2: Submitting PRs

### Step 1: Submit the current branch (and all branches below it)
```bash
gt submit
```
This will:
- Push your branches to the remote
- Create (or update) PRs for each branch
- Set up the PR chain so reviewers see the dependencies

### Step 2: Check the result
```bash
gt log
```
You should see PR numbers next to your branches.

### Step 3: Submit your entire stack
If you want to submit ALL branches (including ones above your current position):
```bash
gt submit --stack
```
Or use the shortcut:
```bash
gt ss
```

---

## Part 3: Updating PRs After Changes

### Step 1: Make a change to a branch
```bash
gt bottom
echo "update" >> config.md
git add .
gt modify
```

### Step 2: Re-submit to update the PR
```bash
gt submit
```
This pushes the updated branch and updates the PR.

### Step 3: Update all PRs in the stack
```bash
gt ss
```

---

## Part 4: Update-Only Mode

If you only want to update existing PRs (not create new ones):
```bash
gt submit --stack --update-only
```
Or:
```bash
gt ss -u
```

---

## Part 5: Addressing Feedback on Parent Branches

This is one of the most powerful features of stacked diffs. When a parent branch gets review feedback, Graphite makes it easy to update the entire stack.

### Scenario
You have a stack: A -> B -> C (each building on the previous).
A reviewer requests changes to branch A.

### Step 1: Navigate to the branch that needs changes
```bash
gt checkout A
# or use navigation
gt bottom  # if A is at the bottom
```

### Step 2: Make the requested changes
```bash
# Edit your files to address feedback
# For example:
echo "addressed feedback" >> config.md
git add .
```

### Step 3: Amend the branch
```bash
gt modify
```
This updates A's commit with your new changes.

### Step 4: Rebase the children
```bash
gt sync
```
Graphite rebases B and C on top of the updated A.

### Step 5: Update all PRs
```bash
gt ss
```
All three PRs (A, B, C) are now updated with A's changes propagated through.

### Handling Conflicts

If B or C conflict with A's changes, `gt sync` will pause:

```bash
# 1. Resolve conflicts in your editor
# 2. Stage the resolved files
git add .
# 3. Continue the rebase
gt continue
```

### The Full Workflow
```bash
gt checkout A           # Go to branch needing changes
# ... make edits ...
git add .
gt modify               # Amend A
gt sync                 # Rebase B and C onto new A
gt ss                   # Update all PRs
```

### Why This Matters
Without Graphite, you'd have to manually:
1. Amend A
2. Checkout B, rebase onto A
3. Checkout C, rebase onto B
4. Push all three branches

With Graphite: `gt modify` -> `gt sync` -> done.

---

## Common Workflows

### After making changes anywhere in your stack:
```bash
gt ss  # Push everything and update all PRs
```

### After a teammate merges a PR below yours:
```bash
gt sync  # Rebase on latest trunk, clean up merged branches
gt ss    # Update remaining PRs
```

### Starting a new day of work:
```bash
gt sync  # Get latest changes
gt log   # See current state
```

---

## Tips

- Run `gt sync` regularly to avoid conflicts
- Use `gt ss` liberally - it's safe and keeps PRs up to date
- Check `gt log` after operations to verify state

---

Next: [Exercise 04 - Reorganizing](./04-reorganizing.md)
