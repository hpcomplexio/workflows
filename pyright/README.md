# PyRight Multithreaded Playground

A hands-on playground for exploring PyRight's `--threads` feature, focusing on performance benchmarks and CI/CD integration patterns.

## Background

PyRight supports multithreaded type checking via the `--threads` CLI flag. Key facts:

- **CLI-only** - the `--threads` flag only works with command-line usage (not LSP)
- **Performance** - can provide 3x+ speedup on large codebases
- **Architecture** - uses directory-aware task distribution for optimal parallelization
- **Status** - experimental but production-ready for CI workflows

Source: [PyRight Discussion #8767](https://github.com/microsoft/pyright/discussions/8767)

## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+ (for npm installation) OR pip

### Installation

**Option 1: pip (recommended)**
```bash
pip install pyright
```

**Option 2: npm**
```bash
npm install -g pyright
```

### Generate Sample Code

Before running the exercises, generate the synthetic test code:

```bash
cd pyright
python generate_sample_code.py
```

This creates three test codebases:
- `sample-code/small/` - ~15 files (baseline)
- `sample-code/medium/` - ~75 files
- `sample-code/large/` - ~250 files

**Note:** The playground uses `typeCheckingMode: "strict"` in `pyrightconfig.json`, so you'll see **1000+ type errors** when running PyRight. This is intentional - the synthetic code exercises PyRight's type checking thoroughly for realistic performance testing. Focus on timing and statistics rather than individual errors.

## Exercises

| # | Exercise | Focus |
|---|----------|-------|
| 1 | [Basic Setup](exercises/01-basic-setup.md) | Install, configure, run type checks |
| 2 | [Single vs Multi-threaded](exercises/02-single-vs-multi.md) | Performance comparison with `--threads` |
| 3 | [CI Integration](exercises/03-ci-integration.md) | GitHub Actions patterns for self-hosted runners |

## Quick Reference

See [pyright-commands.md](pyright-commands.md) for a complete CLI reference.

### Essential Commands

```bash
# Basic type checking
pyright

# Multithreaded (CLI only)
pyright --threads

# With timing
time pyright
time pyright --threads

# Show statistics
pyright --stats
```

## Key Takeaways

After completing the exercises, you should understand:

1. How to configure PyRight for strict type checking
2. When `--threads` provides meaningful speedup (large codebases)
3. How to integrate multithreaded PyRight into CI/CD pipelines
4. Performance measurement techniques for type checking

## Tips

- The `--threads` flag has minimal impact on small codebases
- Always benchmark on representative code before adopting in CI
- Self-hosted runners with more cores benefit most from `--threads`
- Use `--stats` to understand analysis breakdown
