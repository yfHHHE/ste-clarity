"""Check distributable skill resources and plugin metadata with the standard library."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills/ste-clarity"
MIRROR = ROOT / ".cursor/skills/ste-clarity"


def check(condition, message):
    if not condition:
        raise SystemExit(message)


def files_at(directory):
    return {p.relative_to(directory): p.read_bytes() for p in directory.rglob("*") if p.is_file()}


def main():
    skill = (CANONICAL / "SKILL.md").read_text()
    check(skill.startswith("---\n"), "Missing frontmatter")
    frontmatter = skill.split("---", 2)[1]
    check("name: ste-clarity" in frontmatter, "Wrong skill name")
    check("description:" in frontmatter, "Missing skill description")
    check(re.search(r"(?m)^disable-model-invocation: true$", frontmatter), "Claude explicit-only invocation is missing")
    policy = (CANONICAL / "agents/openai.yaml").read_text()
    check(re.search(r"(?m)^policy:\n  allow_implicit_invocation: false$", policy), "Codex explicit-only invocation is missing")
    check(files_at(CANONICAL) == files_at(MIRROR), "Cursor mirror differs from canonical skill")

    manifests = [json.loads((ROOT / f".{agent}-plugin/plugin.json").read_text()) for agent in ("codex", "claude")]
    check(all(m["name"] == "ste-clarity" for m in manifests), "Plugin name mismatch")
    check(len({m["version"] for m in manifests}) == 1, "Plugin version mismatch")
    check((ROOT / manifests[0]["skills"]).is_dir(), "Missing Codex skills directory")
    for path in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
        market = json.loads((ROOT / path).read_text())
        check(market["name"] == "ste-clarity", "Marketplace name mismatch")
        check(market["plugins"][0]["name"] == "ste-clarity", "Marketplace plugin mismatch")
    source = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())["plugins"][0]["source"]
    check(source["url"] == "https://github.com/yfHHHE/ste-clarity.git", "Wrong public repository")
    check(source["ref"] == "main", "Wrong marketplace branch")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("https://", "http://", "#")):
                continue
            target = target.split("#", 1)[0]
            check((path.parent / target).exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}")
    print("PASS: skill metadata, complete Cursor mirror, plugin manifests, explicit-only invocation metadata, and local links")


if __name__ == "__main__":
    main()
