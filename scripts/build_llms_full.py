"""Build llms-full.txt: the whole site as one Markdown file for language models.

It is llms.txt followed by every blog post's Markdown twin, newest first.
Run it after adding or editing a post; prepare_static.py also runs it so the
published copy is never stale.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def build() -> str:
    parts = [(ROOT / "llms.txt").read_text(encoding="utf-8").rstrip()]
    posts = sorted((ROOT / "blog").glob("*/index.md"), key=post_date, reverse=True)
    for post in posts:
        slug = post.parent.name
        parts.append(
            f"---\n\n<!-- https://omeoray.com/blog/{slug}/ -->\n\n"
            + post.read_text(encoding="utf-8").rstrip()
        )
    return "\n\n".join(parts) + "\n"


def post_date(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("date:"):
            return line.split(":", 1)[1].strip()
    return ""


def main() -> None:
    (ROOT / "llms-full.txt").write_text(build(), encoding="utf-8")
    print("Wrote llms-full.txt")


if __name__ == "__main__":
    main()
