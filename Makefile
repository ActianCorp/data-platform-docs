# Zensical build targets for the Actian Data Platform documentation portal.
# Zensical reads zensical.toml. Raw-Markdown mirroring is a post-build step
# because Zensical does not support MkDocs `hooks:`.

.PHONY: serve build clean

# Local live-reload preview.
serve:
	zensical serve

# Production build: generate the site, then mirror .md sources into site/.
build:
	zensical build
	python3 scripts/copy_md_sources.py

clean:
	rm -rf site
