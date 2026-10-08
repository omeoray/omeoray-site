"""Stage only the public website files for Replit static publishing."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "dist"

FILES = (
    Path("index.html"),
    Path("styles.css"),
    Path("favicon.svg"),
    Path("contact/index.html"),
    Path("assets/apple-touch-icon.png"),
    Path("assets/auntyrun.png"),
    Path("assets/b33n.png"),
    Path("assets/omeoray-mark.png"),
    Path("assets/plug.png"),
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

    print(f"Prepared {len(FILES)} public website files in {PUBLIC}")


if __name__ == "__main__":
    main()
