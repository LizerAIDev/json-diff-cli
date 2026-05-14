# JSON Diff CLI

[English](#english) · [中文](#中文)

---

## English

Colorized JSON diff for terminal — compare two JSON files and see differences highlighted in green/red.

### Features

- **Recursive diff** — handles nested objects and arrays
- **Color output** — green for additions, red for removals
- **Zero dependencies** — pure Python standard library
- **Path notation** — shows exact location of each difference

### Quick Start

```bash
python main.py file1.json file2.json
```

### Example

```bash
$ python main.py old.json new.json
- name: "old_project"
+ name: "new_project"
+ version: "2.0"
- debug: true

3 difference(s) found.
```

### Options

| Flag | Description |
|------|-------------|
| `--color` | Enable color output (default) |
| `--no-color` | Disable color output |

---

## 中文

终端彩色 JSON 对比工具——比较两个 JSON 文件，差异以红绿色高亮显示。

### 功能

- **递归对比** — 支持嵌套对象和数组
- **彩色输出** — 绿色新增，红色删除
- **零依赖** — 纯 Python 标准库
- **路径标记** — 精确显示每个差异的位置

### 快速开始

```bash
python main.py file1.json file2.json
```

### 示例

```bash
$ python main.py old.json new.json
- name: "old_project"
+ name: "new_project"
+ version: "2.0"
- debug: true

发现 3 处差异。
```

### 选项

| 参数 | 说明 |
|------|------|
| `--color` | 启用彩色输出（默认） |
| `--no-color` | 禁用彩色输出 |

---

*By Lizer | [github.com/LizerAIDev](https://github.com/LizerAIDev)*
