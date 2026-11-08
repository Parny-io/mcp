"""Local structural checks, not an official Cursor schema or runtime test."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    manifest = json.loads((root / ".cursor-plugin/plugin.json").read_text())
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"]), "Invalid plugin name"
    config_path = manifest["mcpServers"]
    assert not Path(config_path).is_absolute() and ".." not in Path(config_path).parts
    variables = manifest["variables"]
    assert variables["type"] == "object"
    assert "PARNY_OAUTH_CLIENT_ID" in variables["required"]
    assert variables["properties"]["PARNY_OAUTH_CLIENT_ID"]["type"] == "string"
    config = json.loads((root / config_path).read_text())
    server = config["mcpServers"]["parny"]
    assert server["url"] == "https://mcp.parny.io/v2/mcp"
    assert server["auth"]["CLIENT_ID"] == "${PARNY_OAUTH_CLIENT_ID}"
    assert server["auth"]["scopes"] == ["mcp:sre", "mcp:developer"]
    assert "CLIENT_SECRET" not in server["auth"] and "headers" not in server
    example = json.loads((root / "examples/cursor-mcp.json").read_text())
    assert example["mcpServers"]["parny"]["auth"]["CLIENT_ID"] == "${env:PARNY_OAUTH_CLIENT_ID}"
    for path in root.rglob("*.json"):
        json.loads(path.read_text())
    return True

if __name__ == "__main__":
    validate()
    print("PASS: JSON syntax and local configuration checks. OAuth runtime NOT tested.")
