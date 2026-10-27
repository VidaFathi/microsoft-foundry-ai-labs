"""Offline tests of request construction (no Azure charges)."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from chatbot_app import DEPLOYMENT_NAME, ask_ai  # noqa: E402


class ChatbotTests(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.client.responses.create.return_value = SimpleNamespace(
            id="resp_sample", output_text="Hello!"
        )

    def test_first_question(self):
        response = ask_ai(self.client, "  Hello  ")
        self.assertEqual(response.output_text, "Hello!")
        self.client.responses.create.assert_called_once_with(
            model=DEPLOYMENT_NAME, input="Hello"
        )

    def test_follow_up_includes_previous_id(self):
        ask_ai(self.client, "Explain it", "resp_previous")
        self.client.responses.create.assert_called_once_with(
            model=DEPLOYMENT_NAME,
            input="Explain it",
            previous_response_id="resp_previous",
        )

    def test_empty_question_rejected(self):
        with self.assertRaises(ValueError):
            ask_ai(self.client, " ")
        self.client.responses.create.assert_not_called()


if __name__ == "__main__":
    unittest.main()
