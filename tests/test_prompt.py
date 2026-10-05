"""Checks for the hand-written Chinese chat prompt (PROMPT.md)."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ChatPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = (ROOT / "PROMPT.md").read_text(encoding="utf-8")

    def test_version_matches_package(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        match = re.search(r"^版本：(\S+)$", self.text, re.MULTILINE)
        self.assertIsNotNone(match, "PROMPT.md needs a 版本： line")
        self.assertEqual(match.group(1), version, "update PROMPT.md when VERSION changes")

    def test_states_chat_limits_up_front(self) -> None:
        head = self.text[: self.text.index("## 一条总原则")]
        for phrase in ("实际观测", "复测统计", "结论闸门", "技能版"):
            self.assertIn(phrase, head)

    def test_uses_contract_status_values(self) -> None:
        for status in (
            "unavailable",
            "not_mentioned",
            "mentioned",
            "cited",
            "recommended",
            "negative",
        ):
            self.assertIn(f"`{status}`", self.text)

    def test_stays_short_enough_for_chat(self) -> None:
        self.assertLess(len(self.text), 15000)


if __name__ == "__main__":
    unittest.main()
