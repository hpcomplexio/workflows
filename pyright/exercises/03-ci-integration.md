# Exercise 3: CI Integration

Learn how to integrate PyRight with CI/CD pipelines, with focus on leveraging `--threads` on self-hosted runners.

## Goal

By the end of this exercise, you'll have GitHub Actions workflows configured for both hosted and self-hosted runners with optimal PyRight settings.

## Prerequisites

- Completed [Exercise 2: Single vs Multi-threaded](02-single-vs-multi.md)
- Understanding of GitHub Actions basics

## Background

CI considerations for PyRight:
- **GitHub-hosted runners**: Limited cores (2 vCPUs typically), `--threads` provides modest benefit
- **Self-hosted runners**: Can utilize many cores, `--threads` shines here
- **Caching**: PyRight cache can speed up incremental runs
- **Exit codes**: PyRight returns non-zero on type errors (useful for CI gates)

## Part 1: Basic Workflow (No Threading)

Create `.github/workflows/pyright.yml`:

```yaml
name: Type Check

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyRight
        run: pip install pyright

      - name: Run type checking
        run: pyright
```

This is the simplest approach, suitable for smaller projects.

## Part 2: Workflow with Threading (Self-Hosted)

For self-hosted runners with multiple cores:

```yaml
name: Type Check (Self-Hosted)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  typecheck:
    runs-on: self-hosted  # Your self-hosted runner label
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyRight
        run: pip install pyright

      - name: Show available cores
        run: nproc

      - name: Run type checking (multi-threaded)
        run: pyright --threads
```

## Part 3: Caching for Faster Runs

Add caching to speed up repeated runs:

```yaml
name: Type Check (Cached)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  typecheck:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install PyRight
        run: pip install pyright

      - name: Cache PyRight
        uses: actions/cache@v4
        with:
          path: .pyright_cache
          key: pyright-${{ runner.os }}-${{ hashFiles('pyrightconfig.json') }}
          restore-keys: |
            pyright-${{ runner.os }}-

      - name: Run type checking
        run: pyright --threads
```

**Note**: The cache key includes `pyrightconfig.json` hash to invalidate on config changes.

## Part 4: Conditional Threading

Use threading only when beneficial:

```yaml
name: Type Check (Smart Threading)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  typecheck:
    runs-on: ${{ matrix.runner }}
    strategy:
      matrix:
        include:
          - runner: ubuntu-latest
            threads: false
          - runner: self-hosted
            threads: true

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyRight
        run: pip install pyright

      - name: Run type checking
        run: |
          if [ "${{ matrix.threads }}" = "true" ]; then
            echo "Running with --threads (self-hosted)"
            pyright --threads
          else
            echo "Running single-threaded (hosted)"
            pyright
          fi
```

## Part 5: JSON Output for Annotations

Use JSON output for better GitHub integration:

```yaml
name: Type Check (Annotated)

on:
  pull_request:
    branches: [main]

jobs:
  typecheck:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyRight
        run: pip install pyright

      - name: Run type checking
        id: pyright
        run: |
          pyright --threads --outputjson > pyright-results.json || true

      - name: Upload results
        uses: actions/upload-artifact@v4
        with:
          name: pyright-results
          path: pyright-results.json

      - name: Check for errors
        run: |
          errors=$(jq '.generalDiagnostics | length' pyright-results.json)
          if [ "$errors" -gt 0 ]; then
            echo "Found $errors type errors"
            jq '.generalDiagnostics[] | "\(.file):\(.range.start.line): \(.message)"' pyright-results.json
            exit 1
          fi
```

## Part 6: Performance Comparison in CI

Add timing to compare:

```yaml
name: Type Check (Benchmark)

on:
  workflow_dispatch:  # Manual trigger for benchmarking

jobs:
  benchmark:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyRight
        run: pip install pyright

      - name: Show system info
        run: |
          echo "CPU cores: $(nproc)"
          pyright --version

      - name: Benchmark single-threaded
        run: |
          rm -rf .pyright_cache
          echo "Single-threaded:"
          time pyright --stats

      - name: Benchmark multi-threaded
        run: |
          rm -rf .pyright_cache
          echo "Multi-threaded:"
          time pyright --threads --stats
```

## Part 7: Sample Workflow File

A complete workflow is provided at `.github/workflows/pyright-sample.yml`. Copy and adapt it:

```bash
# View the sample
cat .github/workflows/pyright-sample.yml

# Copy to your project
cp .github/workflows/pyright-sample.yml /path/to/your/project/.github/workflows/
```

## Key Takeaways

1. **Use `--threads` on self-hosted runners** with multiple cores
2. **Cache the `.pyright_cache` directory** for faster incremental runs
3. **Use JSON output** for CI parsing and artifact storage
4. **Benchmark your specific codebase** before committing to `--threads`
5. **Consider conditional threading** based on runner type

## Summary

| Scenario | Recommendation |
|----------|---------------|
| GitHub-hosted (2 vCPU) | Single-threaded or light threading |
| Self-hosted (4+ cores) | Use `--threads` |
| Large monorepo | Definitely use `--threads` |
| Small project | Single-threaded is fine |

## Complete Workflow Reference

See the sample workflow files in `.github/workflows/`:
- `pyright-basic.yml` - Simple single-threaded
- `pyright-threaded.yml` - Multi-threaded for self-hosted
- `pyright-sample.yml` - Full-featured with caching and benchmarks

## Congratulations!

You've completed the PyRight Multithreaded Playground. You now understand:
- How to configure PyRight for type checking
- When `--threads` provides performance benefits
- How to integrate PyRight into CI/CD pipelines
- Best practices for self-hosted runners
