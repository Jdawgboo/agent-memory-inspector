import unittest
from tool import inspect


class MemoryTests(unittest.TestCase):
    def test_detects_audit_signals(self):
        result = inspect([
            {"id": "a", "text": "Fact", "source": "note", "created_at": "2026-01-01"},
            {"id": "b", "text": "fact", "created_at": "2026-09-01"},
        ], "2026-09-12")
        self.assertEqual(result["missing_source"], ["b"])
        self.assertEqual(result["stale"], ["a"])
        self.assertEqual(result["duplicates"], ["a:b"])


if __name__ == "__main__":
    unittest.main()
