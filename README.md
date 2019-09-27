# cmake-format-pre-commit-hook
A [pre-commit](https://pypi.org/project/pre-commit/) hook for [cmake-format](https://pypi.org/project/cmake-format/).

# Example

Here's the most basic way to add a hook to `cmake-format` to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/iconmaster5326/cmake-format-pre-commit-hook
  rev: master
  hooks:
    - id: cmake-format
```
