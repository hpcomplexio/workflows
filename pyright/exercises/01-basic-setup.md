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

**Note: Errors are Expected!**

You'll see **hundreds of type errors** (1000+ warnings) when running PyRight in strict mode on the synthetic code. This is **intentional and expected** for these reasons:

1. **Exercises PyRight fully** - The type checker does real work beyond just parsing
2. **Realistic testing** - Real codebases often have type issues
3. **Better for benchmarking** - Analyzing and reporting errors adds to the workload

The synthetic code was designed to trigger various type checking scenarios, not to be error-free. Focus on the **summary line** and **timing** rather than individual errors.

Example output with errors:
```
Found 19 source files
/path/to/sample-code/small/models/service_02.py
  /path/to/sample-code/small/models/service_02.py:20 - error: Return type is partially unknown
  ... (many more errors) ...
1020 errors, 0 warnings, 8 informations
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

PyRight offers three type checking modes with different levels of strictness. Override the config temporarily to compare:

```bash
# Basic mode (fewer checks)
pyright --typecheckingmode basic

# Standard mode (balanced)
pyright --typecheckingmode standard

# Strict mode (all checks, default in our config)
pyright --typecheckingmode strict
```

### Type Checking Modes Explained

| Mode | Error Count | Description | Use Case |
|------|-------------|-------------|----------|
| **basic** | ~50-100 errors | Minimal checks, focuses on obvious bugs | Legacy codebases, gradual adoption |
| **standard** | ~300-500 errors | Balanced checks, enforces most best practices | Production codebases with some types |
| **strict** | 1000+ errors | All checks enabled, enforces complete typing | New projects, type-complete libraries |

**What each mode checks:**

**Basic mode** checks:
- Syntax errors
- Obvious type mismatches (e.g., `int + str`)
- Undefined variables
- Import errors

**Standard mode** adds:
- Function parameter types
- Return type consistency
- Generic type arguments
- Basic protocol/ABC compliance

**Strict mode** additionally requires:
- All function parameters fully typed
- All return types explicit
- No `Any` types (or flag them as unknown)
- Full type stub coverage for imports
- Complete type annotations everywhere

**For this playground:** We use strict mode to maximize PyRight's workload for realistic performance testing. In your real projects, choose the mode that fits your team's type coverage goals.

Try running all three modes and observe how error counts change:

```bash
echo "=== Basic Mode ==="
pyright --typecheckingmode basic | tail -2

echo "=== Standard Mode ==="
pyright --typecheckingmode standard | tail -2

echo "=== Strict Mode ==="
pyright --typecheckingmode strict | tail -2
```

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
