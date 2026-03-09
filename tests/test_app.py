import unittest

from app import get_messages, health_check


class TestApp(unittest.TestCase):
    def test_messages_include_expected_lines(self):
        messages = get_messages()
        self.assertIn("Hello, DevOps!", messages)
        self.assertIn("Full loop: code -> Git -> CI -> Docker.", messages)

    def test_messages_are_strings(self):
        messages = get_messages()
        self.assertTrue(all(isinstance(m, str) for m in messages))

    def test_health_check_status_is_ok(self):
        result = health_check()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["service"], "my-devops-demo2")
        self.assertIn("timestamp", result)


if __name__ == "__main__":
    unittest.main()
