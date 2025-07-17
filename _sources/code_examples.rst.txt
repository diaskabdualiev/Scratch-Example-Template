=================
Примеры кода
=================

Sphinx отлично поддерживает подсветку синтаксиса для множества языков программирования.

Python
======

.. code-block:: python
   :caption: Класс для работы с пользователями
   :linenos:

   class User:
       """Класс пользователя системы."""
       
       def __init__(self, name: str, email: str):
           self.name = name
           self.email = email
           self._is_active = True
       
       @property
       def is_active(self) -> bool:
           """Проверяет, активен ли пользователь."""
           return self._is_active
       
       def deactivate(self) -> None:
           """Деактивирует пользователя."""
           self._is_active = False
           print(f"Пользователь {self.name} деактивирован")
   
   # Пример использования
   user = User("Иван Иванов", "ivan@example.com")
   print(f"Статус: {user.is_active}")

JavaScript
==========

.. code-block:: javascript
   :caption: Асинхронная загрузка данных
   :emphasize-lines: 8,12

   async function fetchUserData(userId) {
       try {
           const response = await fetch(`/api/users/${userId}`);
           
           if (!response.ok) {
               throw new Error(`HTTP error! status: ${response.status}`);
           }
           
           const userData = await response.json();
           return userData;
       } catch (error) {
           console.error('Ошибка при загрузке данных пользователя:', error);
           throw error;
       }
   }
   
   // Использование
   fetchUserData(123)
       .then(data => console.log('Данные пользователя:', data))
       .catch(err => console.error('Ошибка:', err));

HTML и CSS
==========

.. code-block:: html
   :caption: Пример HTML страницы

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Пример страницы</title>
       <style>
           .container {
               max-width: 800px;
               margin: 0 auto;
               padding: 20px;
           }
           .highlight {
               background-color: #ffffcc;
               padding: 10px;
               border-radius: 5px;
           }
       </style>
   </head>
   <body>
       <div class="container">
           <h1>Добро пожаловать</h1>
           <p class="highlight">Это выделенный текст</p>
       </div>
   </body>
   </html>

SQL
===

.. code-block:: sql
   :caption: Запросы к базе данных

   -- Создание таблицы пользователей
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       email VARCHAR(255) UNIQUE NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       is_active BOOLEAN DEFAULT TRUE
   );
   
   -- Вставка данных
   INSERT INTO users (name, email) VALUES 
       ('Иван Иванов', 'ivan@example.com'),
       ('Петр Петров', 'petr@example.com');
   
   -- Сложный запрос с JOIN
   SELECT 
       u.name,
       u.email,
       COUNT(o.id) as order_count,
       SUM(o.total) as total_spent
   FROM users u
   LEFT JOIN orders o ON u.id = o.user_id
   WHERE u.is_active = TRUE
   GROUP BY u.id, u.name, u.email
   HAVING COUNT(o.id) > 0
   ORDER BY total_spent DESC;

JSON
====

.. code-block:: json
   :caption: Конфигурационный файл

   {
       "name": "Демо проект",
       "version": "1.0.0",
       "description": "Демонстрационный проект для Sphinx",
       "authors": [
           {
               "name": "Dias Kabdualiyev",
               "email": "dias@example.com"
           }
       ],
       "dependencies": {
           "sphinx": "^8.0.0",
           "sphinx-rtd-theme": "^3.0.0"
       },
       "scripts": {
           "build": "sphinx-build -b html source build/html",
           "clean": "rm -rf build/",
           "serve": "python -m http.server 8000 -d build/html"
       },
       "config": {
           "language": "ru",
           "theme": "alabaster",
           "extensions": [
               "sphinx.ext.autodoc",
               "sphinx.ext.viewcode"
           ]
       }
   }

Bash/Shell
==========

.. code-block:: bash
   :caption: Скрипт развертывания

   #!/bin/bash
   
   # Установка зависимостей
   echo "Установка зависимостей..."
   pip install -r requirements.txt
   
   # Сборка документации
   echo "Сборка документации..."
   if make html; then
       echo "✅ Документация собрана успешно"
   else
       echo "❌ Ошибка при сборке документации"
       exit 1
   fi
   
   # Запуск локального сервера
   echo "Запуск сервера на порту 8000..."
   cd build/html
   python -m http.server 8000

YAML
====

.. code-block:: yaml
   :caption: GitHub Actions workflow

   name: Build Documentation
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       
       steps:
       - uses: actions/checkout@v3
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.9'
       
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install sphinx sphinx-rtd-theme
       
       - name: Build documentation
         run: |
           make html
       
       - name: Deploy to GitHub Pages
         uses: peaceiris/actions-gh-pages@v3
         if: github.ref == 'refs/heads/main'
         with:
           github_token: ${{ secrets.GITHUB_TOKEN }}
           publish_dir: ./build/html

Dockerfile
==========

.. code-block:: dockerfile
   :caption: Контейнер для документации

   FROM python:3.9-slim
   
   WORKDIR /docs
   
   # Установка системных зависимостей
   RUN apt-get update && apt-get install -y \
       make \
       && rm -rf /var/lib/apt/lists/*
   
   # Копирование requirements
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Копирование исходников
   COPY source/ source/
   COPY Makefile .
   
   # Сборка документации
   RUN make html
   
   # Запуск веб-сервера
   EXPOSE 8000
   CMD ["python", "-m", "http.server", "8000", "-d", "build/html"]

Интерактивные примеры
=====================

Консольная сессия:

.. code-block:: console
   :caption: Работа с виртуальной средой

   $ python -m venv venv
   $ source venv/bin/activate  # Linux/Mac
   $ venv\Scripts\activate     # Windows
   (venv) $ pip install sphinx
   Collecting sphinx...
   Successfully installed sphinx-8.2.3
   (venv) $ sphinx-quickstart
   Welcome to the Sphinx quickstart utility...

Вывод программы:

.. code-block:: text
   :caption: Результат выполнения

   Компиляция завершена успешно.
   
   Создано файлов: 15
   Время выполнения: 2.34 секунды
   Размер вывода: 2.1 МБ
   
   Следующие шаги:
   1. Проверьте результат в папке build/
   2. Откройте index.html в браузере
   3. При необходимости внесите изменения

Включение внешних файлов
========================

Можно включать код из внешних файлов:

.. literalinclude:: conf.py
   :language: python
   :lines: 9-13
   :caption: Информация о проекте из conf.py
   :emphasize-lines: 3 