=======================
Продвинутые функции
=======================

Этот раздел демонстрирует продвинутые возможности Sphinx для создания 
профессиональной документации.

Автодокументация Python
========================

Sphinx может автоматически генерировать документацию из docstrings Python:

.. automodule:: os
   :members: getcwd, listdir
   :undoc-members:
   :show-inheritance:

Пример модуля для автодокументации:

.. code-block:: python
   :caption: example_module.py

   """Пример модуля для демонстрации автодокументации."""
   
   class Calculator:
       """Простой калькулятор для демонстрации."""
       
       def __init__(self):
           """Инициализация калькулятора."""
           self.history = []
       
       def add(self, a: float, b: float) -> float:
           """
           Сложение двух чисел.
           
           Args:
               a: Первое число
               b: Второе число
               
           Returns:
               Сумма чисел
               
           Example:
               >>> calc = Calculator()
               >>> calc.add(2, 3)
               5.0
           """
           result = a + b
           self.history.append(f"{a} + {b} = {result}")
           return result

Условная документация
=====================

Содержимое может отображаться условно:

.. ifconfig:: language == 'ru'

   Этот текст показывается только для русской локализации.

.. ifconfig:: language == 'en'

   This text is shown only for English localization.

Версионирование
===============

.. versionadded:: 1.0
   Добавлена поддержка математических формул.

.. versionchanged:: 1.1
   Улучшена обработка изображений.

.. deprecated:: 1.2
   Функция ``old_method()`` устарела. Используйте ``new_method()``.

.. versionremoved:: 2.0
   Поддержка Python 2.7 удалена.

Пользовательские директивы
==========================

Пример создания пользовательской директивы:

.. code-block:: python
   :caption: Добавление в conf.py

   from docutils import nodes
   from docutils.parsers.rst import Directive
   
   class HighlightBox(Directive):
       has_content = True
       
       def run(self):
           container = nodes.container()
           container['classes'] = ['highlight-box']
           self.state.nested_parse(self.content, 0, container)
           return [container]
   
   def setup(app):
       app.add_directive('highlight', HighlightBox)

Включение файлов
================

Sphinx позволяет включать содержимое из внешних файлов:

.. code-block:: rst

   .. include:: ../README.rst
      :start-line: 1
      :end-line: 5

Это полезно для включения общих частей документации.

Замещения
=========

Вы можете определить замещения для часто используемых фраз:

.. |project| replace:: Alashed Scratch
.. |version| replace:: 1.0.0
.. |author| replace:: Dias Kabdualiyev

Проект |project| версии |version| создан автором |author|.

Роли (Roles)
============

Встроенные роли:

* :abbr:`HTML (HyperText Markup Language)`
* :acronym:`API (Application Programming Interface)`
* :command:`make html`
* :file:`/path/to/file.txt`
* :guilabel:`&File --> &Open`
* :kbd:`Ctrl+C`
* :mailheader:`Content-Type`
* :makevar:`BUILDDIR`
* :manpage:`grep(1)`
* :menuselection:`File --> Open`
* :mimetype:`text/html`
* :newsgroup:`comp.lang.python`
* :program:`sphinx-build`
* :regexp:`[a-z]+`
* :samp:`print {variable}`

Пользовательские роли:

.. role:: red

CSS для пользовательской роли:

.. raw:: html

   <style>
   .red { color: red; }
   </style>

Использование: :red:`красный текст`.

Расширения
==========

Популярные расширения Sphinx:

.. code-block:: python
   :caption: Дополнительные расширения в conf.py

   extensions = [
       'sphinx.ext.autodoc',      # Автодокументация
       'sphinx.ext.viewcode',     # Ссылки на код
       'sphinx.ext.napoleon',     # Google/NumPy docstrings
       'sphinx.ext.intersphinx',  # Ссылки между проектами
       'sphinx.ext.todo',         # TODO списки
       'sphinx.ext.mathjax',      # Математика
       'sphinx.ext.ifconfig',     # Условная документация
       'sphinx.ext.graphviz',     # Диаграммы Graphviz
       'sphinx.ext.inheritance_diagram',  # Диаграммы наследования
       'sphinx_rtd_theme',        # ReadTheDocs тема
   ]

Диаграммы
=========

Sphinx поддерживает различные типы диаграмм через расширения.

Пример Graphviz диаграммы (требует установки sphinx.ext.graphviz):

.. code-block:: rst

   .. graphviz::

      digraph G {
          rankdir=LR;
          A -> B -> C;
          A -> C;
          B -> D;
          C -> D;
      }

Пример UML диаграммы наследования (требует sphinx.ext.inheritance_diagram):

.. code-block:: rst

   .. inheritance-diagram:: builtins.list builtins.dict
      :parts: 1

Интернационализация
===================

Sphinx поддерживает создание многоязычной документации:

.. code-block:: bash

   # Извлечение строк для перевода
   make gettext
   
   # Создание переводов
   sphinx-intl update -p build/gettext -l en -l de
   
   # Сборка с переводом
   make -e SPHINXOPTS="-D language='en'" html

Темы оформления
===============

Настройка темы Alabaster:

.. code-block:: python
   :caption: Настройки темы в conf.py

   html_theme_options = {
       'logo': 'logo.png',
       'logo_name': True,
       'description': 'Демонстрация Sphinx',
       'github_user': 'username',
       'github_repo': 'repo',
       'github_banner': True,
       'github_button': True,
       'show_powered_by': False,
       'extra_nav_links': {
           'PDF': 'https://example.com/docs.pdf',
           'Исходный код': 'https://github.com/user/repo',
       }
   }

Кастомизация вывода
===================

HTML выходные файлы:

.. code-block:: python

   html_additional_pages = {
       'download': 'download.html',
   }
   
   html_extra_path = ['robots.txt', '.nojekyll']

PDF вывод через LaTeX:

.. code-block:: python

   latex_elements = {
       'papersize': 'a4paper',
       'pointsize': '12pt',
       'preamble': r'''
       \usepackage[utf8]{inputenc}
       \usepackage[russian]{babel}
       ''',
   }

Производительность
==================

Оптимизация сборки:

.. code-block:: python

   # Параллельная сборка
   html_build_parallel = True
   
   # Кеширование
   html_cache_path = 'cache'

Отладка
=======

Полезные опции для отладки:

.. code-block:: bash

   # Подробный вывод
   sphinx-build -v source build
   
   # Проверка ссылок
   sphinx-build -b linkcheck source build
   
   # Профилирование
   sphinx-build -E -a source build

Интеграция с Git
=================

Автоматическое определение версии:

.. code-block:: python
   :caption: В conf.py

   import subprocess
   
   try:
       release = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
   except:
       release = '1.0.0'

Хуки Git для автосборки:

.. code-block:: bash
   :caption: .git/hooks/post-commit

   #!/bin/bash
   cd docs/
   make html

Развертывание
=============

GitHub Pages:

.. code-block:: yaml
   :caption: .github/workflows/docs.yml

   name: Build and Deploy Docs
   on:
     push:
       branches: [ main ]
   
   jobs:
     build-and-deploy:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Setup Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.9'
       - name: Install dependencies
         run: pip install sphinx sphinx-rtd-theme
       - name: Build docs
         run: make html
       - name: Deploy to GitHub Pages
         uses: peaceiris/actions-gh-pages@v3
         with:
           github_token: ${{ secrets.GITHUB_TOKEN }}
           publish_dir: ./build/html

Мониторинг документации
=======================

Метрики качества документации:

* Покрытие API автодокументацией
* Количество битых ссылок
* Время сборки
* Размер вывода

Инструменты для анализа:

.. code-block:: bash

   # Анализ битых ссылок
   sphinx-build -b linkcheck source build
   
   # Статистика документации
   sphinx-build -b coverage source build

Безопасность
============

Рекомендации по безопасности:

* Не включайте конфиденциальную информацию в публичную документацию
* Проверяйте права доступа к приватным репозиториям
* Используйте HTTPS для всех внешних ссылок
* Регулярно обновляйте зависимости Sphinx

.. warning::
   Будьте осторожны с директивой `.. raw::` - она может быть источником уязвимостей. 