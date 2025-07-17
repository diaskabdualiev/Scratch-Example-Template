# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Alashed Scratch'
copyright = '2025, Dias Kabdualiyev'
author = 'Dias Kabdualiyev'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Автодокументация
    'sphinx.ext.viewcode',      # Ссылки на исходный код
    'sphinx.ext.todo',          # TODO директивы
    'sphinx.ext.mathjax',       # Математические формулы
    'sphinx.ext.ifconfig',      # Условная документация
    'sphinx.ext.napoleon',      # Google/NumPy стиль docstrings
    'sphinx.ext.intersphinx',   # Ссылки на другую документацию
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# Настройки для TODO
todo_include_todos = True

# Включение нумерации рисунков и таблиц
numfig = True
numfig_format = {
    'figure': 'Рисунок %s',
    'table': 'Таблица %s',
    'code-block': 'Листинг %s'
}

# Настройки для Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Настройки темы ReadTheDocs
html_theme_options = {
    'analytics_id': '',  # ID Google Analytics (если нужен)
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980b9',
    # Настройки toc
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# ReadTheDocs тема использует собственную навигацию
# html_sidebars не требуется для RTD темы

# Дополнительные настройки для RTD
html_context = {
    'display_github': True,   # Интеграция с GitHub
    'github_user': 'your-username',
    'github_repo': 'scratch-wiki',
    'github_version': 'main',
    'conf_py_path': '/source/',
}
