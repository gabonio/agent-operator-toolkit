from __future__ import annotations

import contextlib
import io
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
CHECK_COPILOT = runpy.run_path(str(ROOT / "scripts" / "check"))["check_copilot_builder_kit"]


class CopilotBuilderKitChecks(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.plugin = self.root / "plugins" / "builder-kit"
        shutil.copytree(ROOT / "plugins" / "builder-kit", self.plugin)
        self.skill = self.plugin / "skills" / "builder-kit" / "SKILL.md"

    def errors(self) -> list[str]:
        errors: list[str] = []
        with patch.dict(CHECK_COPILOT.__globals__, ROOT=self.root), contextlib.redirect_stdout(io.StringIO()):
            CHECK_COPILOT(errors)
        return errors

    def test_current_bundle_is_valid(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_missing_skill_is_rejected(self) -> None:
        self.skill.unlink()
        self.assertTrue(any("skill set differs" in error for error in self.errors()))

    def test_mismatched_skill_name_is_rejected(self) -> None:
        self.skill.write_text(self.skill.read_text().replace("name: builder-kit", "name: other"))
        self.assertTrue(any("name must match" in error for error in self.errors()))

    def test_missing_frontmatter_is_rejected(self) -> None:
        self.skill.write_text("# Builder Kit\n")
        self.assertTrue(any("missing skill frontmatter" in error for error in self.errors()))

    def test_empty_description_is_rejected(self) -> None:
        lines = self.skill.read_text().splitlines()
        self.skill.write_text("\n".join("description: " if line.startswith("description:") else line for line in lines) + "\n")
        self.assertTrue(any("missing single-line skill description" in error for error in self.errors()))

    def test_automatic_invocation_is_rejected(self) -> None:
        self.skill.write_text(self.skill.read_text().replace("disable-model-invocation: true", "disable-model-invocation: false"))
        self.assertTrue(any("explicitly invoked" in error for error in self.errors()))

    def test_missing_reference_is_rejected(self) -> None:
        (self.plugin / "references" / "workflow" / "profiles.md").unlink()
        self.assertTrue(any("profiles.md" in error for error in self.errors()))

    def test_reference_outside_plugin_is_rejected_even_when_it_exists(self) -> None:
        (self.root / "outside.md").write_text("# Outside\n")
        self.skill.write_text(self.skill.read_text() + "\n[Outside](../../../../outside.md)\n")
        self.assertTrue(any("non-portable resource" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
