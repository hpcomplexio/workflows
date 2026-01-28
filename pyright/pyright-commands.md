# PyRight CLI Reference

Quick reference for PyRight command-line options relevant to this playground.

## Basic Usage

| Command | Description |
|---------|-------------|
| `pyright` | Type check current directory using pyrightconfig.json |
| `pyright <path>` | Type check specific file or directory |
| `pyright --help` | Show all available options |

## Performance & Threading

| Command | Description |
|---------|-------------|
| `pyright --threads` | Enable multithreaded analysis (CLI only) |
| `pyright --stats` | Show detailed analysis statistics |
| `time pyright` | Measure total execution time |

**Note:** `--threads` is CLI-only. The language server already uses 2 threads (foreground for LSP, background for analysis).

## Output Formats

| Command | Description |
|---------|-------------|
| `pyright` | Default human-readable output |
| `pyright --outputjson` | JSON output for CI/tooling integration |
| `pyright --verbose` | Verbose output with trace information |

## Configuration

| Command | Description |
|---------|-------------|
| `pyright --project <file>` | Use specific config file |
| `pyright --pythonversion <ver>` | Override Python version (e.g., 3.11) |
| `pyright --typecheckingmode <mode>` | Override mode: off, basic, standard, strict |

## Verification & Analysis

| Command | Description |
|---------|-------------|
| `pyright --verifytypes <package>` | Check type completeness of a package |
| `pyright --dependencies` | Emit dependency information |
| `pyright --createstub <package>` | Create type stub for a package |

## Watch Mode

| Command | Description |
|---------|-------------|
| `pyright --watch` | Watch for file changes and re-analyze |

**Note:** Watch mode and `--threads` can be combined.

## Common Patterns

### Benchmarking Single vs Multi-threaded

```bash
# Clear any caches first
rm -rf .pyright_cache

# Single-threaded baseline
time pyright

# Clear cache again for fair comparison
rm -rf .pyright_cache

# Multi-threaded
time pyright --threads
```

### CI Integration

```bash
# Exit with non-zero on errors (default behavior)
pyright

# JSON output for parsing
pyright --outputjson > pyright-results.json

# Strict mode override
pyright --typecheckingmode strict
```

### Verbose Debugging

```bash
# See what files are being analyzed
pyright --verbose

# Combine with stats
pyright --verbose --stats
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No errors |
| 1 | Type errors found |
| 2 | Configuration error |
| 3 | Fatal error |
