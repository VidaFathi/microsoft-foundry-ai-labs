"""Self-contained tests for Module 1 prompt construction."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from prompt_design import build_messages  # noqa: E402


class PromptDesignTests(unittest.TestCase):
    def test_roles_and_order(self):
        result = build_messages("Be concise.", "What is inference?")
        self.assertEqual([m["role"] for m in result], ["system", "user"])
        self.assertEqual(result[1]["content"], "What is inference?")

    def test_whitespace(self):
        result = build_messages("  Be clear.  ", "  What is an SDK?  ")
        self.assertEqual(result[0]["content"], "Be clear.")
        self.assertEqual(result[1]["content"], "What is an SDK?")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            build_messages("", "What is an LLM?")
        with self.assertRaises(ValueError):
            build_messages("Be clear", "  ")


if __name__ == "__main__":
    unittest.main()
