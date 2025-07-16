.. Alashed Scratch documentation master file, created by
   sphinx-quickstart on Wed Jul 16 14:06:33 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================
Демонстрация возможностей Sphinx
====================================

Добро пожаловать в демонстрационную документацию, созданную с помощью Sphinx!
Этот проект показывает основные возможности генератора документации Sphinx.

.. note::
   Это демонстрационная документация, созданная для изучения возможностей Sphinx.
   Вы можете адаптировать её под свои нужды.

Что такое Sphinx?
=================

**Sphinx** — это инструмент, который упрощает создание красивой документации. 
Он был создан для документации Python, но теперь используется для документации 
проектов на многих языках программирования.

Основные преимущества:
----------------------

* **Форматы вывода**: HTML, PDF, EPub и многие другие
* **Межссылочность**: автоматические ссылки между документами
* **Подсветка кода**: поддержка синтаксиса для множества языков
* **Математические формулы**: поддержка LaTeX
* **Темы**: красивые и настраиваемые темы
* **Расширения**: богатая экосистема расширений

.. warning::
   Для правильной работы всех примеров убедитесь, что у вас установлены 
   все необходимые расширения Sphinx.

Содержание демонстрации
=======================

.. toctree::
   :maxdepth: 2
   :caption: Основы:
   :numbered:

   restructuredtext_basics
   sphinx_directives
   code_examples

.. toctree::
   :maxdepth: 2
   :caption: Продвинутые возможности:

   math_formulas
   tables_and_lists
   cross_references
   advanced_features

.. toctree::
   :maxdepth: 1
   :caption: Дополнительно:

   glossary

Быстрый старт
=============

Чтобы собрать эту документацию:

.. code-block:: batch

   # Активировать виртуальную среду (Windows)
   venv\Scripts\activate

   # Собрать HTML документацию
   .\make.bat html

   # Открыть результат
   build\html\index.html

Полезные ссылки
===============

* `Официальная документация Sphinx <https://www.sphinx-doc.org/>`_
* `Руководство по reStructuredText <https://docutils.sourceforge.io/rst.html>`_
* `Галерея тем Sphinx <https://sphinx-themes.org/>`_

.. seealso::
   
   Изучите разделы этой документации, чтобы увидеть возможности Sphinx в действии!

Индексы и поиск
===============

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

