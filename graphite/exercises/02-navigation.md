# Exercise 2: Navigation

## Goal
Learn to move efficiently through your stack.

## Prerequisites
Complete Exercise 01 (you should have a stack with 3 branches).

---

## Part 1: Basic Navigation

### Step 1: Go to the top of your stack
```bash
gt top
```
This jumps to the highest branch in your current stack.

### Step 2: Go to the bottom
```bash
gt bottom
```
This jumps to the lowest branch (just above main).

### Step 3: Move up one branch
```bash
gt up
```

### Step 4: Move down one branch
```bash
gt down
```

### Step 5: Check where you are
```bash
gt log
```
Your current branch is highlighted.

---

## Part 2: Direct Checkout

### Step 1: Jump to a specific branch
```bash
gt checkout <branch-name>
```
Replace `<branch-name>` with the actual name (visible in `gt log`).

### Step 2: Go back to the previous branch
```bash
gt checkout -
```
Like `cd -` in bash, this returns to where you were.

---

## Part 3: Navigation Practice

Try this sequence and predict where you'll end up:

```bash
gt bottom
gt log          # Where are you?

gt up
gt up
gt log          # Where now?

gt top
gt down
gt log          # And now?

gt checkout main
gt log          # Back at trunk
```

---

## Part 4: Navigation + Viewing

Combine navigation with viewing to understand your stack:

```bash
gt bottom && gt log    # Go to bottom, see position
gt top && gt log       # Go to top, see position
```

---

## Summary

| Command | What it does |
|---------|--------------|
| `gt top` | Jump to top of stack |
| `gt bottom` | Jump to bottom of stack |
| `gt up` | Move up one branch |
| `gt down` | Move down one branch |
| `gt checkout <name>` | Go to specific branch |
| `gt checkout -` | Go to previous branch |

---

## Tips

- Use `gt log` after navigation to confirm your position
- `gt top` and `gt bottom` are fastest for jumping to extremes
- `gt up` and `gt down` are best for moving through related branches

---

Next: [Exercise 03 - Syncing and Submitting](./03-syncing-submitting.md)
