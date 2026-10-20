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
CHECKS = runpy.run_path(str(ROOT / "scripts" / "check"))
CHECK_COPILOT = CHECKS["check_copilot_builder_kit"]
CHECK_STANDARDS = CHECKS["check_builder_kit_standards"]
STANDARD_NAMES = {
    "typescript-javascript", "go", "csharp-dotnet", "sql", "rust", "kotlin", "swift", "php", "ruby",
    "frontend", "python", "java", "cpp", "jenkins",
}


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
            CHECK_STANDARDS(errors)
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

    def test_all_language_and_existing_standards_are_routed(self) -> None:
        standards = self.plugin / "references" / "standards"
        self.assertEqual({path.stem for path in standards.glob("*.md")} - {"routing"}, STANDARD_NAMES)
        routing = (standards / "routing.md").read_text()
        for name in STANDARD_NAMES:
            with self.subTest(standard=name):
                self.assertIn(f"]({name}.md)", routing)
        self.assertEqual(self.errors(), [])

    def test_missing_standard_is_rejected_for_bare_relative_links(self) -> None:
        standards = self.plugin / "references" / "standards"
        for name in sorted(STANDARD_NAMES):
            with self.subTest(standard=name):
                path = standards / f"{name}.md"
                original = path.read_text()
                path.unlink()
                try:
                    self.assertTrue(any(f"{name}.md" in error for error in self.errors()))
                finally:
                    path.write_text(original)

    def test_unrouted_standard_is_rejected(self) -> None:
        routing = self.plugin / "references" / "standards" / "routing.md"
        routing.write_text(routing.read_text().replace("[Go](go.md)", "Go"))
        self.assertTrue(any("not routed: go.md" in error for error in self.errors()))

    def test_missing_standards_router_is_rejected(self) -> None:
        (self.plugin / "references" / "standards" / "routing.md").unlink()
        self.assertTrue(any("missing Builder Kit standards routing" in error for error in self.errors()))

    def test_direct_implementation_and_review_entrypoints_route_standards(self) -> None:
        for name in ("builder-kit", "start-new-app", "develop-from-spec", "adversarial-review"):
            with self.subTest(skill=name):
                text = (self.plugin / "skills" / name / "SKILL.md").read_text()
                self.assertIn("](../../references/standards/routing.md)", text)
        standard_review = self.plugin / "references" / "lenses" / "standard-review.md"
        self.assertIn("](../standards/routing.md)", standard_review.read_text())

    def test_stack_discovery_shares_the_specification_workflow(self) -> None:
        specification = self.plugin / "references" / "workflow" / "specification.md"
        interview = specification.read_text()
        start = (self.plugin / "skills" / "start-new-app" / "SKILL.md").read_text()
        self.assertIn("specification.md#conditional-stack-selection-interview", start)
        self.assertIn("Ask one question at a time", interview)
        self.assertIn("only about unknowns", interview)
        self.assertIn("not ordinary changes to an established stack", interview)
        self.assertIn("mark unverified hosting claims explicitly", interview)
        self.assertIn("Require explicit user approval before committing to the selection or scaffolding", interview)
        self.assertIn("Do not deploy anything during discovery", interview)
        template = (self.plugin / "templates" / "specification.md").read_text()
        self.assertIn("{{EVIDENCE_AND_GAPS}}", template)
        self.assertIn("{{BLOCKERS_AND_STACK_APPROVAL}}", template)


if __name__ == "__main__":
    unittest.main()
