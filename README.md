# cmake-format-pre-commit-hook
A [pre-commit](https://pypi.org/project/pre-commit/) hook for [cmake-format](https://pypi.org/project/cmake-format/).

# Usage

By default, this hook runs on files beginning with `CMakeLists` and files ending with `.cmake` (all case sensitive).
It uses the default configurations, unless you have a `.cmake-format{.py,.yaml,.json}` file, as is usual with `cmake-format`.
You can also specift formatting optinos with `args:` in your `.pre-commit-config.yaml`.

# Example

Here's the most basic way to add a hook to `cmake-format` to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/iconmaster5326/cmake-format-pre-commit-hook
  rev: master
  hooks:
    - id: cmake-format
```
