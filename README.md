# JSON Diff CLI

Colorized JSON diff for terminal — compare two JSON files and see differences highlighted in green/red.

## Quick Start

```bash
python main.py file1.json file2.json
```

## Features

- **Recursive diff** — nested objects and arrays
- **Color output** — green for additions, red for removals
- **Zero dependencies** — pure Python standard library
- **Path notation** — shows exact location of each difference

## Example

```bash
$ python main.py old.json new.json
- name: "old_project"
+ name: "new_project"
+ version: "2.0"
- debug: true

3 difference(s) found.
```

---

*By Lizer - [github.com/LizerAIDev](https://github.com/LizerAIDev)*
