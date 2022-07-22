# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = poetry run sphinx-build
SPHINXPROJ    = dotenv-linter
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

{% if cookiecutter.other_languages_support == 'y' -%}
.PHONY: translate
translate: gettext
	poetry run sphinx-intl update -p $(BUILDDIR)/gettext {% if cookiecutter.russian_language_support == 'y' -%}-l ru {% endif %}{% if cookiecutter.ukrainian_language_support == 'y' -%}-l uk_UA{% endif %}

{% endif %}# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
