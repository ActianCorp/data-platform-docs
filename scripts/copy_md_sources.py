#!/usr/bin/env python3
"""Copy every source .md file from docs/ into site/ at the same relative path.

This is the Zensical replacement for the old MkDocs post-build hook
(hooks/copy_md_sources.py). Zensical does not support the `hooks:` option, so
this runs as a standalone step AFTER `zensical build`:

    zensical build && python scripts/copy_md_sources.py

It makes raw Markdown available at predictable public URLs on the deployed
site (e.g. https://docs.actian.com/.../getting-started.md), for:
  - in-app docs browsers that need Markdown endpoints
  - users who want to copy-paste page content into Claude / ChatGPT
"""
import argparse
import os
import shutil
import sys


def copy_md_sources(docs_dir: str, site_dir: str) -> int:
    if not os.path.isdir(site_dir):
        sys.exit(f"error: site_dir '{site_dir}' not found — run `zensical build` first")

    count = 0
    for root, _dirs, files in os.walk(docs_dir):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            src_path = os.path.join(root, filename)
            rel_path = os.path.relpath(src_path, docs_dir)
            dst_path = os.path.join(site_dir, rel_path)

            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
            count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", default="docs")
    parser.add_argument("--site-dir", default="site")
    args = parser.parse_args()

    n = copy_md_sources(args.docs_dir, args.site_dir)
    print(f"Copied {n} Markdown source files into '{args.site_dir}/'")
