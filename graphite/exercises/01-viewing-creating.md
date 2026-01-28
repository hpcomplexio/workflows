# Exercise 1: Viewing and Creating

## Goal
Learn to view your stack and create new branches.

---

## Part 1: Viewing Your Stack

### Step 1: See the stack visualization
```bash
gt log
```
This shows a visual tree of your branches and how they stack on each other.

Press `q` to exit the log view.

### Step 2: List all tracked branches
```bash
gt ls
```
This shows a flat list of branches Graphite is tracking.

---

## Part 2: Creating Your First Stack

### Step 1: Start from main
```bash
gt checkout main
```

### Step 2: Create your first branch
Create a file and make your first stacked branch:
```bash
echo "# Config" > config.md
git add config.md
gt create -m "docs: add config file"
```

### Step 3: View your stack
```bash
gt log
```
You should see your new branch stacked on main.

### Step 4: Create a second branch (stacked on the first)
```bash
echo "# API" > api.md
git add api.md
gt create -m "docs: add api file"
```

### Step 5: Create a third branch
```bash
echo "# Examples" > examples.md
git add examples.md
gt create -m "docs: add examples file"
```

### Step 6: View the full stack
```bash
gt log
```
You now have 3 branches stacked on each other!

---

## Part 3: Modifying a Branch

### What if you need to make changes to the current branch?

### Step 1: Make a change
```bash
echo "More content" >> examples.md
git add examples.md
```

### Step 2: Amend the current branch
```bash
gt modify
```
This amends the commit without changing the message.

### Step 3: Amend with a new message
```bash
echo "Even more" >> examples.md
git add examples.md
gt modify -m "docs: add examples with details"
```

---

## Summary

| Command | What it does |
|---------|--------------|
| `gt log` | Visualize your stack |
| `gt ls` | List tracked branches |
| `gt create -m "msg"` | Create a new branch |
| `gt modify` | Amend current branch |
| `gt modify -m "msg"` | Amend with new message |

---

Next: [Exercise 02 - Navigation](./02-navigation.md)
