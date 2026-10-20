from __future__ import annotations

import contextlib
import io
from pathlib import Path
import re
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
LANGUAGE_GUIDE_CHECKS = {
    "typescript-javascript": ("noUncheckedIndexedAccess", "void promise", "tsc --noEmit"),
    "go": ("rows.Err()", "%w", "go test -race"),
    "csharp-dotnet": ("CA2016", "CA1851", "ConfigureAwait(false)"),
    "sql": ("CREATE INDEX CONCURRENTLY", "EXPLAIN (ANALYZE, BUFFERS)", "invalid index"),
    "rust": ("clippy::restriction", "cargo fmt --check", "MSRV"),
    "kotlin": ("runTest", "JVM facades", "ensureActive()"),
    "swift": ("Task.detached", "-strict-concurrency=complete", "language mode"),
    "php": ("PER Coding Style", "PDO::prepare()", "php -l"),
    "ruby": ("strict_loading", "after_commit", "TargetRubyVersion"),
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

    def test_language_guides_keep_concrete_checks_and_a_context_budget(self) -> None:
        for name, checks in LANGUAGE_GUIDE_CHECKS.items():
            with self.subTest(standard=name):
                text = (self.plugin / "references" / "standards" / f"{name}.md").read_text()
                self.assertIn("## Correctness and operations", text)
                self.assertIn("## Checks and conventions", text)
                self.assertLessEqual(len(text.split()), 400)
                for check in checks:
                    self.assertIn(check, text)

    def test_each_researched_language_has_a_maintainer_source_record(self) -> None:
        provenance = (self.plugin / "docs" / "standards-provenance.md").read_text()
        self.assertRegex(provenance, r"Research date: \d{4}-\d{2}-\d{2}\.")
        records = dict(re.findall(
            r"^### ([a-z-]+)\n(.*?)(?=^### |^## |\Z)",
            provenance,
            re.MULTILINE | re.DOTALL,
        ))
        self.assertEqual(set(records), set(LANGUAGE_GUIDE_CHECKS))
        for name, record in records.items():
            with self.subTest(standard=name):
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)", record)), 2)
        self.assertIn("not deterministic agent behavior", provenance)

    def test_source_bibliography_stays_out_of_runtime_entrypoints(self) -> None:
        paths = list((self.plugin / "skills").glob("*/SKILL.md"))
        paths.extend((self.plugin / "references" / "standards").glob("*.md"))
        for path in paths:
            with self.subTest(path=path.relative_to(self.plugin)):
                self.assertNotIn("standards-provenance.md", path.read_text())
        routing = (self.plugin / "references" / "standards" / "routing.md").read_text()
        self.assertIn("Do not install tools, enable repo-wide rules", routing)

    def test_domain_organization_is_routed_without_a_new_skill(self) -> None:
        for name in ("builder-kit", "start-new-app", "develop-from-spec"):
            with self.subTest(skill=name):
                text = (self.plugin / "skills" / name / "SKILL.md").read_text()
                self.assertIn("](../../references/architecture/domain-organization.md)", text)
        architecture = (self.plugin / "references" / "lenses" / "systems-architecture.md").read_text()
        self.assertIn("](../architecture/domain-organization.md)", architecture)
        self.assertEqual(len(list((self.plugin / "skills").glob("*/SKILL.md"))), 5)

    def test_missing_domain_guidance_is_rejected(self) -> None:
        (self.plugin / "references" / "architecture" / "domain-organization.md").unlink()
        self.assertTrue(any("domain-organization.md" in error for error in self.errors()))

    def test_domain_acceptance_review_and_handoff_contracts(self) -> None:
        domain = (self.plugin / "references" / "architecture" / "domain-organization.md").read_text()
        self.assertIn("Preserve existing repository conventions and approved architecture", domain)
        self.assertIn("does not require microservices", domain)
        self.assertIn("do not duplicate the map", domain)
        self.assertIn("entrypoint, business rule, adapter, and result/error", domain)
        profiles = (self.plugin / "references" / "workflow" / "profiles.md").read_text()
        self.assertIn("The agent owns naming, organization, tests", profiles)
        self.assertIn("one question at a time", profiles)
        specification = (self.plugin / "templates" / "specification.md").read_text()
        self.assertIn("{{CAPABILITY_OWNERSHIP_AND_NAVIGATION_OR_EXISTING_DESIGN_LINK}}", specification)
        plan = (self.plugin / "templates" / "implementation-plan.md").read_text()
        self.assertIn("capability ownership/dependencies", plan)
        self.assertIn("handoff gaps recorded", plan)
        for name in ("standard-review", "adversarial-review"):
            with self.subTest(lens=name):
                text = (self.plugin / "references" / "lenses" / f"{name}.md").read_text()
                self.assertIn("handoff", text)
        verification = (self.plugin / "references" / "workflow" / "verification.md").read_text()
        self.assertIn("documented run/test commands", verification)
        self.assertIn("not duplicate existing docs", verification)


if __name__ == "__main__":
    unittest.main()
