# CI Failure Analyzer

A GitHub Action that detects common CI failures and provides actionable fixes.

## Features
- Detect missing dependencies
- Identify Playwright setup issues
- Suggest fixes

## Usage

```yaml
- uses: shweta83/ci-failure-analyzer@v1
  with:
    log-file: test_output.log

