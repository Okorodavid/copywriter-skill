"""Build the upload zips into dist/.

    python scripts/build.py

dist/copywriter-claude-skill.zip  upload to claude.ai (Settings > Capabilities > Skills)
dist/copywriter-chatgpt.zip       instructions + knowledge files for a Custom GPT or ChatGPT Project
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "plugins" / "copywriter" / "skills" / "copywriter"
DIST = ROOT / "dist"
GPT_INSTRUCTIONS_LIMIT = 8000  # characters allowed in a Custom GPT's Instructions box


def check() -> list[str]:
    problems = []
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not front:
        problems.append("SKILL.md has no frontmatter")
    else:
        fields = dict(line.split(": ", 1) for line in front.group(1).splitlines() if ": " in line)
        if not re.fullmatch(r"[a-z0-9-]{1,64}", fields.get("name", "")):
            problems.append("SKILL.md name must be lowercase letters, digits and hyphens")
        if not 0 < len(fields.get("description", "")) <= 1024:
            problems.append("SKILL.md description must be 1-1024 characters")
    for ref in re.findall(r"`references/([\w.-]+)`", text):
        if not (SKILL / "references" / ref).exists():
            problems.append(f"SKILL.md points to missing references/{ref}")
    gpt = (ROOT / "chatgpt" / "instructions.md").read_text(encoding="utf-8")
    if len(gpt) > GPT_INSTRUCTIONS_LIMIT:
        problems.append(f"chatgpt/instructions.md is {len(gpt)} characters (limit {GPT_INSTRUCTIONS_LIMIT})")
    for name in re.findall(r"\b([\w-]+\.md)\b", gpt):
        if not (SKILL / "references" / name).exists():
            problems.append(f"chatgpt/instructions.md names missing knowledge file {name}")
    return problems


def build() -> None:
    DIST.mkdir(exist_ok=True)
    files = sorted(p for p in SKILL.rglob("*") if p.is_file())

    with zipfile.ZipFile(DIST / "copywriter-claude-skill.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, Path("copywriter") / p.relative_to(SKILL))

    with zipfile.ZipFile(DIST / "copywriter-chatgpt.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.write(ROOT / "chatgpt" / "instructions.md", "instructions.md")
        z.write(ROOT / "chatgpt" / "SETUP.md", "SETUP.md")
        for p in sorted((SKILL / "references").glob("*.md")):
            z.write(p, Path("knowledge") / p.name)

    for z in sorted(DIST.glob("*.zip")):
        print(f"{z.relative_to(ROOT)}  {z.stat().st_size // 1024} KB")


if __name__ == "__main__":
    problems = check()
    for p in problems:
        print("problem:", p)
    if problems:
        sys.exit(1)
    build()
