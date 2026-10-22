from __future__ import annotations

import os
import json
from pathlib import Path

project = "BMatrix"
author = "BMatrix contributors"
publication_path = Path(__file__).parent.parent / "publication.json"
if publication_path.is_file():
    publication = json.loads(publication_path.read_text(encoding="utf-8"))
else:
    publication = {
        "appVersion": "development preview",
        "documentationRevision": "local/unpublished",
    }
release = publication.get("appVersion", "development preview")
language = "en"

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
]
myst_enable_extensions = ["substitution"]

source_suffix = {
    ".md": "markdown",
}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_heading_anchors = 3
myst_substitutions = {
    "app_version": publication.get("appVersion", "development preview"),
    "docs_revision": publication.get("documentationRevision", "local/unpublished"),
}
nitpicky = True

html_theme = "furo"
html_title = "BMatrix User Guide"
html_baseurl = os.environ.get(
    "BMATRIX_DOCS_BASEURL",
    "https://tibarbosa.github.io/bmatrix-releases/",
)
