import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class ConfigurationTests(unittest.TestCase):
    def test_valid_package(self):
        self.assertTrue(validator.validate())
    def test_reject_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("__pycache__"))
            path = copy / "mcp.json"
            value = json.loads(path.read_text())
            value["mcpServers"]["parny"]["auth"]["CLIENT_SECRET"] = "TEST_ONLY"
            path.write_text(json.dumps(value))
            with self.assertRaises(AssertionError):
                validator.validate(copy)
    def test_reject_path_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("__pycache__"))
            path = copy / ".cursor-plugin/plugin.json"
            value = json.loads(path.read_text())
            value["mcpServers"] = "../mcp.json"
            path.write_text(json.dumps(value))
            with self.assertRaises(AssertionError):
                validator.validate(copy)

if __name__ == "__main__":
    unittest.main()
