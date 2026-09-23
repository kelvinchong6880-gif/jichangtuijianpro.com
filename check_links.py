"""Check generated internal links, fragment IDs and static assets without extra packages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys


DIST = Path(__file__).resolve().parent / "dist"
REDIRECTS = Path(__file__).resolve().parent / "public" / "_redirects"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        key = {"a": "href", "link": "href", "script": "src", "img": "src", "source": "src"}.get(tag)
        if key and attrs.get(key):
            self.references.append((tag, attrs[key]))
        if tag in {"img", "source"} and attrs.get("srcset"):
            for candidate in attrs["srcset"].split(","):
                self.references.append((tag, candidate.strip().split()[0]))


def main():
    if not DIST.is_dir():
        raise SystemExit("Build output is missing. Run npm run build first.")
    pages = {}
    for file in DIST.rglob("*.html"):
        parser = PageParser()
        parser.feed(file.read_text(encoding="utf-8"))
        path = "/" + file.relative_to(DIST).as_posix()
        if path.endswith("index.html"):
            path = path[: -len("index.html")]
        pages[path] = parser
    redirects = set()
    if REDIRECTS.exists():
        for line in REDIRECTS.read_text(encoding="utf-8").splitlines():
            fields = line.split()
            if fields and not line.lstrip().startswith("#"):
                redirects.add(fields[0])

    errors = []
    checked = 0
    for page_path, parser in pages.items():
        for tag, ref in parser.references:
            target = urlsplit(urljoin("https://local.invalid" + page_path, ref))
            if target.netloc != "local.invalid" or target.scheme not in {"http", "https"}:
                continue
            path = unquote(target.path)
            file_path = DIST / path.lstrip("/")
            page_target = path if path.endswith("/") else path + "/"
            checked += 1
            if path not in redirects and page_target not in pages and not file_path.is_file():
                errors.append(f"{page_path}: missing {tag} target {ref}")
                continue
            if tag == "a" and target.fragment and page_target in pages:
                if unquote(target.fragment) not in pages[page_target].ids:
                    errors.append(f"{page_path}: missing fragment {ref}")
    for error in errors:
        print(error)
    print(f"Checked {checked} internal references across {len(pages)} pages; {len(errors)} issue(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
