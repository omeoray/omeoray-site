"""Stage only the public website files for Replit static publishing."""

from pathlib import Path
import shutil

from build_llms_full import build as build_llms_full


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "dist"

FILES = (
    Path("index.html"),
    Path("styles.css"),
    Path("favicon.svg"),
    Path("contact/index.html"),
    Path("blog/index.html"),
    Path("blog/feed.xml"),
    Path("blog/b33n-place-recommendations-from-friends/index.html"),
    Path("blog/b33n-place-recommendations-from-friends/index.md"),
    Path("robots.txt"),
    Path("sitemap.xml"),
    Path("llms.txt"),
    Path("assets/apple-touch-icon.png"),
    Path("assets/auntyrun.png"),
    Path("assets/b33n.png"),
    Path("assets/omeoray-mark.png"),
    Path("assets/plug.png"),
    Path("assets/og-omeoray.png"),
    Path("assets/blog/b33n-og.png"),
    Path("assets/blog/b33n-hero.svg"),
    Path("assets/blog/b33n-rec-request.svg"),
    Path("assets/blog/b33n-capture.svg"),
    Path("assets/blog/b33n-assistant.svg"),
)


def main() -> None:
    # dist is generated output; replace it each build to prevent stale files
    # from being included in the published site.
    if PUBLIC.exists():
        if PUBLIC.is_symlink() or not PUBLIC.is_dir():
            raise RuntimeError(f"Refusing to replace non-directory output path: {PUBLIC}")
        shutil.rmtree(PUBLIC)

    for relative_path in FILES:
        source = ROOT / relative_path
        if not source.is_file():
            raise FileNotFoundError(f"Required public website file is missing: {source}")
        destination = PUBLIC / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    # Generated rather than copied, so the published copy always matches the posts.
    (PUBLIC / "llms-full.txt").write_text(build_llms_full(), encoding="utf-8")

    print(f"Prepared {len(FILES) + 1} public website files in {PUBLIC}")


if __name__ == "__main__":
    main()
