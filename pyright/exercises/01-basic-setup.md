# Exercise 1: Basic Setup

Learn to install, configure, and run PyRight for type checking.

## Goal

By the end of this exercise, you'll have PyRight installed and configured, and understand how to interpret its output.

## Prerequisites

- Python 3.8+ installed
- pip or npm available

## Part 1: Installation

Choose one installation method:

**Option A: pip (recommended)**
```bash
pip install pyright
```

**Option B: npm**
```bash
npm install -g pyright
```

Verify installation:
```bash
pyright --version
```

## Part 2: Generate Sample Code

Before we can type check, we need some Python code. Generate the synthetic test codebases:

```bash
cd pyright
python generate_sample_code.py
```

This creates three directories under `sample-code/`:
- `small/` - ~15 files for quick tests
- `medium/` - ~75 files for moderate testing
- `large/` - ~250 files for performance testing

## Part 3: Configuration

The playground includes a `pyrightconfig.json`. Let's examine it:

```bash
cat pyrightconfig.json
```

Key settings:
- `typeCheckingMode: "strict"` - enables all type checks
- `include: ["sample-code"]` - specifies what to analyze
- `pythonVersion: "3.11"` - target Python version

## Part 4: Run Type Checking

Run PyRight on the generated code:

```bash
pyright
```

Expected output shows:
- Files analyzed
- Any type errors found
- Total time taken

### Understanding the Output

PyRight reports:
- **Errors**: Type violations that should be fixed
- **Warnings**: Potential issues
- **Information**: Informational messages

Example output:
```
Found 3 source files
pyright 1.1.x
0 errors, 0 warnings, 0 informations
Completed in 1.23s
```

## Part 5: Explore Statistics

Use `--stats` to see detailed analysis breakdown:

```bash
pyright --stats
```

This shows:
- Parse time
- Binding time
- Type checking time
- Total files and lines analyzed

## Part 6: Try Different Strictness Levels

Override the config temporarily:

```bash
# Basic mode (fewer checks)
pyright --typecheckingmode basic

# Standard mode (balanced)
pyright --typecheckingmode standard

# Strict mode (all checks)
pyright --typecheckingmode strict
```

Compare the error counts at each level.

## Part 7: JSON Output

For CI integration, use JSON output:

```bash
pyright --outputjson
```

This outputs structured data that can be parsed by CI tools.

## Summary

| Command | Purpose |
|---------|---------|
| `pyright --version` | Check installation |
| `pyright` | Run type checking |
| `pyright --stats` | Show analysis statistics |
| `pyright --typecheckingmode <mode>` | Override strictness |
| `pyright --outputjson` | Machine-readable output |

## Next Exercise

Continue to [Exercise 2: Single vs Multi-threaded](02-single-vs-multi.md) to compare performance with the `--threads` flag.
