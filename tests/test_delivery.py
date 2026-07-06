from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DeliveryTest(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [
            ROOT / "README.md",
            ROOT / "install.py",
            ROOT / "build_release.py",
            ROOT / "skills/zone-memory/SKILL.md",
            ROOT / "skills/zone-memory/REFERENCE.md",
            ROOT / "skills/zone-memory/references/agents_section.md",
            ROOT / "skills/zone-memory/references/opening_prompts.md",
        ]
        for path in required:
            self.assertTrue(path.is_file(), path)

    def test_installer_validates_package(self) -> None:
        spec = importlib.util.spec_from_file_location("install", ROOT / "install.py")
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source = ROOT / "skills/zone-memory"
        self.assertIsNone(module.validate_package(source))


if __name__ == "__main__":
    unittest.main()
