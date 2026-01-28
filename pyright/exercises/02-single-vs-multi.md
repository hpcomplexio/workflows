# Exercise 2: Single vs Multi-threaded Performance

Compare PyRight's single-threaded and multi-threaded (`--threads`) performance across different codebase sizes.

## Goal

By the end of this exercise, you'll understand when `--threads` provides meaningful speedup and how to measure it.

## Prerequisites

- Completed [Exercise 1: Basic Setup](01-basic-setup.md)
- Sample code generated via `python generate_sample_code.py`

## Background

PyRight's `--threads` flag enables multithreaded type analysis:
- Uses multiple CPU cores for parallel analysis
- Directory-aware task distribution (files in same directory processed together)
- Most beneficial for large codebases (3x+ speedup reported)
- Minimal impact on small codebases

**Important**: `--threads` is CLI-only. The language server already uses 2 threads.

## Part 1: Establish Baseline (Small Codebase)

First, let's benchmark the small codebase:

```bash
cd pyright

# Clear any cached data
rm -rf .pyright_cache

# Single-threaded baseline
time pyright sample-code/small
```

Note the total time. Now with multithreading:

```bash
# Clear cache for fair comparison
rm -rf .pyright_cache

# Multi-threaded
time pyright --threads sample-code/small
```

**Expected**: Minimal difference (possibly slower due to thread overhead).

## Part 2: Medium Codebase

```bash
# Clear cache
rm -rf .pyright_cache

# Single-threaded
time pyright sample-code/medium

# Clear cache
rm -rf .pyright_cache

# Multi-threaded
time pyright --threads sample-code/medium
```

**Expected**: Slight improvement with `--threads`.

## Part 3: Large Codebase

This is where `--threads` shines:

```bash
# Clear cache
rm -rf .pyright_cache

# Single-threaded
time pyright sample-code/large

# Clear cache
rm -rf .pyright_cache

# Multi-threaded
time pyright --threads sample-code/large
```

**Expected**: Significant speedup (potentially 2-3x faster).

## Part 4: Detailed Statistics

Use `--stats` to understand where time is spent:

```bash
# Single-threaded with stats
pyright --stats sample-code/large

# Multi-threaded with stats
pyright --threads --stats sample-code/large
```

Compare:
- Parse time
- Binding time
- Checking time

The checking phase benefits most from parallelization.

## Part 5: Multiple Runs for Accuracy

For accurate benchmarks, run multiple times:

```bash
# Simple benchmark script
for i in {1..3}; do
  echo "Run $i (single-threaded):"
  rm -rf .pyright_cache
  time pyright sample-code/large 2>&1 | grep real
done

echo "---"

for i in {1..3}; do
  echo "Run $i (multi-threaded):"
  rm -rf .pyright_cache
  time pyright --threads sample-code/large 2>&1 | grep real
done
```

## Part 6: Document Your Results

Record your findings:

| Codebase | Files | Single-threaded | Multi-threaded | Speedup |
|----------|-------|-----------------|----------------|---------|
| small    | ~15   | ___s            | ___s           | ___x    |
| medium   | ~75   | ___s            | ___s           | ___x    |
| large    | ~250  | ___s            | ___s           | ___x    |

**Your system info:**
- CPU cores: `sysctl -n hw.ncpu` (macOS) or `nproc` (Linux)
- PyRight version: `pyright --version`

## Part 7: Watch Mode with Threads

You can combine `--threads` with `--watch`:

```bash
pyright --threads --watch sample-code/large
```

Make a small change to a file and observe re-analysis time.

Press `Ctrl+C` to exit watch mode.

## Key Takeaways

1. **Small codebases**: `--threads` may be slower due to thread overhead
2. **Large codebases**: Expect 2-3x speedup (varies by CPU cores)
3. **Cache matters**: Clear `.pyright_cache` for accurate benchmarks
4. **CPU cores**: More cores = more potential benefit
5. **Directory locality**: PyRight groups files by directory for better cache locality

## Summary

| Command | Purpose |
|---------|---------|
| `time pyright` | Measure single-threaded time |
| `time pyright --threads` | Measure multi-threaded time |
| `pyright --stats` | Detailed timing breakdown |
| `rm -rf .pyright_cache` | Clear cache for fair benchmarks |

## Next Exercise

Continue to [Exercise 3: CI Integration](03-ci-integration.md) to learn how to use `--threads` in GitHub Actions and self-hosted runners.
