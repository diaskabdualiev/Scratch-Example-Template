# Sphinx Wiki Template 📚

Готовый шаблон для создания красивой документации с помощью Sphinx. Демонстрирует все основные возможности Sphinx с ReadTheDocs темой и русской локализацией.

## 🌟 Возможности

- **ReadTheDocs тема** - современный адаптивный дизайн
- **Русская локализация** - полная поддержка русского языка
- **Математические формулы** - поддержка LaTeX через MathJax
- **Подсветка кода** - для множества языков программирования
- **Автодокументация** - извлечение документации из Python кода
- **Перекрестные ссылки** - удобная навигация между разделами
- **Поиск** - полнотекстовый поиск по документации
- **Мобильная поддержка** - адаптивный дизайн для всех устройств

## 📋 Демонстрационные разделы

### Основы
- **reStructuredText основы** - синтаксис, форматирование, списки
- **Директивы Sphinx** - блоки уведомлений, код, изображения
- **Примеры кода** - подсветка для Python, JS, HTML, SQL и других

### Продвинутые возможности
- **Математические формулы** - LaTeX формулы, матрицы, уравнения
- **Таблицы и списки** - различные типы таблиц и структурирование
- **Перекрестные ссылки** - внутренние и внешние ссылки
- **Продвинутые функции** - автодокументация, версионирование

### Дополнительно
- **Глоссарий** - словарь терминов с автоматической сортировкой

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone <your-repo-url>
cd scratch-wiki
```

### 2. Создание виртуальной среды
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

**Вариант 1: Точные версии (рекомендуется)**
```bash
pip install -r requirements.txt
```

**Вариант 2: Минимальные зависимости**
```bash
pip install -r requirements-minimal.txt
```

> **Примечание:** `requirements.txt` создан через `pip freeze` и содержит точные версии всех пакетов для воспроизводимости. `requirements-minimal.txt` содержит только основные пакеты с гибкими версиями.

### 4. Сборка документации
```bash
# Windows
.\make.bat html

# Linux/Mac
make html
```

### 5. Просмотр результата
```bash
# Windows
start build\html\index.html

# Linux/Mac
open build/html/index.html
```

## 🔧 Настройка под свой проект

### 1. Основная информация
Отредактируйте `source/conf.py`:

```python
project = 'Название вашего проекта'
copyright = '2025, Ваше имя'
author = 'Ваше имя'
release = '1.0.0'
```

### 2. Главная страница
Отредактируйте `source/index.rst`:
- Измените заголовок и описание
- Обновите содержание toctree
- Добавьте свои разделы

### 3. Создание собственных страниц
1. Создайте новые `.rst` файлы в папке `source/`
2. Добавьте их в `toctree` в `index.rst`
3. Используйте примеры как руководство по синтаксису

### 4. Настройка темы
В `source/conf.py` можете изменить:
```python
html_theme_options = {
    'style_nav_header_background': '#ваш_цвет',
    'navigation_depth': 4,
    # другие опции...
}
```

## 📁 Структура проекта

```
scratch-wiki/
├── source/                      # Исходные файлы документации
│   ├── _static/                 # Статические файлы (CSS, JS, изображения)
│   ├── _templates/              # Пользовательские шаблоны
│   ├── conf.py                  # Конфигурация Sphinx
│   ├── index.rst                # Главная страница
│   ├── restructuredtext_basics.rst
│   ├── sphinx_directives.rst
│   ├── code_examples.rst
│   ├── math_formulas.rst
│   ├── tables_and_lists.rst
│   ├── cross_references.rst
│   ├── advanced_features.rst
│   └── glossary.rst
├── build/                       # Собранная документация
│   └── html/                    # HTML версия
├── venv/                        # Виртуальная среда Python
├── make.bat                     # Скрипт сборки для Windows
├── Makefile                     # Скрипт сборки для Linux/Mac
├── requirements.txt             # Точные версии зависимостей (pip freeze)
├── requirements-minimal.txt     # Минимальные зависимости
├── template_setup.py            # Скрипт автоматической настройки шаблона
├── .gitignore                   # Исключения для Git
├── .github/                     # GitHub Actions для автосборки
│   └── workflows/
│       └── docs.yml
└── README.md                    # Этот файл
```

## 🛠️ Полезные команды

### Сборка различных форматов
```bash
# HTML (по умолчанию)
make html

# PDF через LaTeX (требует LaTeX)
make latexpdf

# ePub
make epub

# Проверка ссылок
make linkcheck

# Очистка
make clean
```

### Автосборка при изменениях
```bash
pip install sphinx-autobuild
sphinx-autobuild source build/html
```

## 📚 Полезные ресурсы

- [Официальная документация Sphinx](https://www.sphinx-doc.org/)
- [Руководство по reStructuredText](https://docutils.sourceforge.io/rst.html)
- [Галерея тем Sphinx](https://sphinx-themes.org/)
- [ReadTheDocs тема](https://sphinx-rtd-theme.readthedocs.io/)

## 🎨 Кастомизация

### Добавление CSS стилей
1. Создайте файл `source/_static/custom.css`
2. Добавьте в `conf.py`:
```python
html_css_files = ['custom.css']
```

### Добавление JavaScript
1. Создайте файл `source/_static/custom.js`
2. Добавьте в `conf.py`:
```python
html_js_files = ['custom.js']
```

### Логотип проекта
1. Поместите изображение в `source/_static/`
2. Добавьте в `conf.py`:
```python
html_logo = '_static/logo.png'
```

## 🚀 Развертывание

### GitHub Pages
1. Создайте `.github/workflows/docs.yml`:
```yaml
name: Build and Deploy Docs
on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Build docs
      run: make html
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./build/html
```

### ReadTheDocs
1. Зарегистрируйтесь на [ReadTheDocs](https://readthedocs.org/)
2. Подключите ваш GitHub репозиторий
3. RTD автоматически соберет документацию

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для ваших изменений
3. Внесите изменения и протестируйте их
4. Создайте Pull Request

## 📄 Лицензия

Этот проект является примером и может свободно использоваться как шаблон для ваших проектов.

## 💡 Советы по использованию

1. **Начните с малого** - используйте базовую структуру и добавляйте разделы постепенно
2. **Изучите примеры** - каждый файл демонстрирует различные возможности Sphinx
3. **Настройте под себя** - измените цвета, логотип и стили под ваш бренд
4. **Используйте автодокументацию** - для Python проектов это очень удобно
5. **Регулярно обновляйте** - поддерживайте документацию в актуальном состоянии

## ❓ Частые вопросы

**Q: Как изменить язык документации?**
A: В `conf.py` измените `language = 'ru'` на нужный язык.

**Q: Как добавить свои директивы?**
A: Создайте Python модуль с директивой и добавьте его в `extensions` в `conf.py`.

**Q: Как настроить автоматическую сборку?**
A: Используйте GitHub Actions или настройте хуки Git для автосборки.

---

🎉 **Удачи в создании отличной документации!** 