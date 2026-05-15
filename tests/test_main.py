#!/usr/bin/env python3
"""Tests for json-diff-cli"""
import sys
import os
import json
import tempfile
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import load_json, diff_json, colorize


class TestLoadJson:
    def test_load_valid_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"key": "value"}, f)
            f.flush()
            result = load_json(f.name)
        assert result == {"key": "value"}

    def test_load_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{invalid json}")
            f.flush()
            with pytest.raises(json.JSONDecodeError):
                load_json(f.name)

    def test_load_nested_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            data = {"a": {"b": {"c": [1, 2, 3]}}}
            json.dump(data, f)
            f.flush()
            result = load_json(f.name)
        assert result == data


class TestDiffJson:
    def test_identical_objects(self):
        a = {"key": "value", "num": 42}
        b = {"key": "value", "num": 42}
        assert diff_json(a, b) == []

    def test_identical_nested(self):
        a = {"outer": {"inner": [1, 2, 3]}}
        b = {"outer": {"inner": [1, 2, 3]}}
        assert diff_json(a, b) == []

    def test_value_change(self):
        a = {"name": "old"}
        b = {"name": "new"}
        result = diff_json(a, b)
        assert any("old" in line for line in result)
        assert any("new" in line for line in result)
        assert any("-" == line[0] for line in result)
        assert any("+" == line[0] for line in result)

    def test_added_key(self):
        a = {"a": 1}
        b = {"a": 1, "b": 2}
        result = diff_json(a, b)
        assert any(line.startswith("+") and "b" in line for line in result)

    def test_removed_key(self):
        a = {"a": 1, "b": 2}
        b = {"a": 1}
        result = diff_json(a, b)
        assert any(line.startswith("-") and "b" in line for line in result)

    def test_type_change(self):
        a = {"key": "string"}
        b = {"key": 42}
        result = diff_json(a, b)
        # Type change shows both values
        assert len(result) == 2

    def test_list_addition(self):
        a = [1, 2]
        b = [1, 2, 3]
        result = diff_json(a, b)
        assert any("+" in line and "3" in line for line in result)

    def test_list_removal(self):
        a = [1, 2, 3]
        b = [1, 2]
        result = diff_json(a, b)
        assert any("-" in line and "3" in line for line in result)

    def test_nested_diff(self):
        a = {"user": {"name": "Alice", "age": 30}}
        b = {"user": {"name": "Alice", "age": 31}}
        result = diff_json(a, b)
        assert any("age" in line for line in result)

    def test_deeply_nested_path(self):
        a = {"a": {"b": {"c": "old"}}}
        b = {"a": {"b": {"c": "new"}}}
        result = diff_json(a, b)
        # Path should be a.b.c
        assert any("a.b.c" in line for line in result)

    def test_primitive_values(self):
        assert len(diff_json(1, 2)) == 2
        assert diff_json("same", "same") == []

    def test_list_value_change(self):
        a = {"items": [1, 2, 3]}
        b = {"items": [1, 5, 3]}
        result = diff_json(a, b)
        assert any("items[1]" in line for line in result)

    def test_both_empty(self):
        assert diff_json({}, {}) == []
        assert diff_json([], []) == []

    def test_empty_vs_nonempty(self):
        result = diff_json({}, {"key": "value"})
        assert len(result) > 0

    def test_keys_sorted(self):
        a = {"b": 1, "a": 2}
        b = {"a": 2, "c": 3}
        result = diff_json(a, b)
        # "c" is added, "b" is removed - order in result should have c before b
        # since we iterate sorted(all_keys) and "b" is in a but not b (removal), "c" is in b but not a (addition)
        # sorted keys: a, b, c -> a same, b removed, c added
        assert result[0].startswith("-")  # - b: 1
        assert result[1].startswith("+")  # + c: 3


class TestColorize:
    def test_add_line(self):
        result = colorize("+ added line")
        assert "\033[92m" in result
        assert "\033[0m" in result

    def test_remove_line(self):
        result = colorize("- removed line")
        assert "\033[91m" in result
        assert "\033[0m" in result

    def test_other_line(self):
        result = colorize("some line")
        assert result == "some line"
