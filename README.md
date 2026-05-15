# JSON Diff CLI | JSON 对比工具

[![CI](https://github.com/LizerAIDev/json-diff-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/LizerAIDev/json-diff-cli/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Colorized JSON diff for terminal — compare two JSON files and see differences highlighted in red/green.

终端彩色 JSON 对比工具——比较两个 JSON 文件，差异以红绿色高亮显示。

---

### Example / 示例

```bash
$ json-diff old.json new.json
- debug: true
+ debug: false
+ features: ["ai"]
- name: "old_project"
+ name: "new_project"
- version: "1.0"
+ version: "2.0"

7 difference(s) found.
```

## Features / 功能

| Feature | Description |
|---------|-------------|
| 🔍 Recursive diff | Handles nested objects and arrays |
| 🎨 Color output | Green for additions, red for removals |
| 📍 Path notation | Shows exact location (e.g., `data.users[0].name`) |
| ⚡ Zero dependencies | Pure Python standard library |

## Quick Start / 快速开始

```bash
# Compare two JSON files
json-diff file1.json file2.json

# Or run directly
python main.py file1.json file2.json
```

### Install / 安装

```bash
pip install json-diff-cli-lizer
json-diff old.json new.json
```

### Options / 参数

| Flag | Description |
|------|-------------|
| `--color` | Enable color output (default) |
| `--no-color` | Disable color output |

## Examples / 示例

### Compare API responses

```bash
json-diff api_v1.json api_v2.json
```

### Compare config files

```bash
json-diff config.dev.json config.prod.json
```

### Use in scripts

```bash
if json-diff old.json new.json --no-color | grep -q "difference"; then
  echo "Configs changed!"
fi
```

## Tech Stack / 技术栈

- **Python 3.9+** — Zero external dependencies
- **json** — Standard library JSON parser
- **argparse** — Standard library CLI parser

## License / 许可证

[MIT License](LICENSE)

---

<div align="center">

Made with ❤️ by [Lizer](https://github.com/LizerAIDev) | Powered by [Hermes Agent](https://hermes-agent.nousresearch.com)

</div>
