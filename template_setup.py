#!/usr/bin/env python3
"""
Скрипт для быстрой настройки Sphinx Wiki Template под новый проект.

Использование:
    python template_setup.py

Этот скрипт поможет вам быстро адаптировать шаблон под ваш проект,
изменив основные настройки в conf.py и index.rst.
"""

import os
import sys
from pathlib import Path


def get_user_input():
    """Получает информацию о проекте от пользователя."""
    print("🚀 Настройка Sphinx Wiki Template")
    print("=" * 40)
    
    project_name = input("Название проекта: ").strip()
    if not project_name:
        project_name = "My Documentation"
    
    author_name = input("Имя автора: ").strip()
    if not author_name:
        author_name = "Author Name"
    
    copyright_year = input("Год для копирайта (по умолчанию 2025): ").strip()
    if not copyright_year:
        copyright_year = "2025"
    
    version = input("Версия проекта (по умолчанию 1.0.0): ").strip()
    if not version:
        version = "1.0.0"
    
    description = input("Короткое описание проекта: ").strip()
    if not description:
        description = "Документация проекта"
    
    language = input("Язык документации (ru/en, по умолчанию ru): ").strip().lower()
    if language not in ['ru', 'en']:
        language = 'ru'
    
    return {
        'project_name': project_name,
        'author_name': author_name,
        'copyright_year': copyright_year,
        'version': version,
        'description': description,
        'language': language
    }


def update_conf_py(config):
    """Обновляет файл conf.py с новыми настройками."""
    conf_path = Path('source/conf.py')
    
    if not conf_path.exists():
        print(f"❌ Файл {conf_path} не найден!")
        return False
    
    # Читаем текущий файл
    with open(conf_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Заменяем основные настройки
    replacements = {
        "project = 'Alashed Scratch'": f"project = '{config['project_name']}'",
        "copyright = '2025, Dias Kabdualiyev'": f"copyright = '{config['copyright_year']}, {config['author_name']}'",
        "author = 'Dias Kabdualiyev'": f"author = '{config['author_name']}'",
        "release = '1.0.0'": f"release = '{config['version']}'",
        "language = 'ru'": f"language = '{config['language']}'",
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Обновляем настройки темы
    if "'description': 'Демонстрация возможностей Sphinx'" in content:
        content = content.replace(
            "'description': 'Демонстрация возможностей Sphinx'",
            f"'description': '{config['description']}'"
        )
    
    # Записываем обновленный файл
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Файл conf.py обновлен")
    return True


def update_index_rst(config):
    """Обновляет главную страницу index.rst."""
    index_path = Path('source/index.rst')
    
    if not index_path.exists():
        print(f"❌ Файл {index_path} не найден!")
        return False
    
    # Читаем текущий файл
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Заменяем заголовок и описание
    old_title = "Демонстрация возможностей Sphinx"
    new_title = config['project_name']
    
    # Создаем новую шапку
    title_underline = "=" * len(new_title)
    new_header = f"""====================================
{new_title}
====================================

{config['description']}

.. note::
   Документация создана с помощью Sphinx Wiki Template.
   Вы можете адаптировать её под свои нужды."""

    # Заменяем старую шапку
    lines = content.split('\n')
    new_lines = []
    skip_until_note = False
    
    for i, line in enumerate(lines):
        if line.strip() == "====================================":
            # Найдена старая шапка, заменяем её
            new_lines.extend(new_header.split('\n'))
            # Пропускаем старую шапку до первой директивы .. note::
            skip_until_note = True
            continue
        
        if skip_until_note:
            if line.strip().startswith(".. note::"):
                # Нашли конец старой шапки, начинаем добавлять строки снова
                skip_until_note = False
                # Пропускаем старую note директиву
                continue
            elif line.strip() == "Что такое Sphinx?":
                # Альтернативный способ найти конец шапки
                skip_until_note = False
                new_lines.append(line)
            continue
        
        new_lines.append(line)
    
    # Записываем обновленный файл
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print("✅ Файл index.rst обновлен")
    return True


def create_backup():
    """Создает резервную копию важных файлов."""
    backup_dir = Path('backup_original')
    backup_dir.mkdir(exist_ok=True)
    
    files_to_backup = ['source/conf.py', 'source/index.rst']
    
    for file_path in files_to_backup:
        src = Path(file_path)
        if src.exists():
            dst = backup_dir / src.name
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"💾 Резервные копии сохранены в {backup_dir}")


def main():
    """Основная функция скрипта."""
    print("Добро пожаловать в настройку Sphinx Wiki Template! 🎉\n")
    
    # Проверяем, что мы в правильной директории
    if not Path('source/conf.py').exists():
        print("❌ Ошибка: Файл source/conf.py не найден!")
        print("Убедитесь, что вы запускаете скрипт из корня проекта Sphinx.")
        sys.exit(1)
    
    # Создаем резервную копию
    create_backup()
    
    # Получаем информацию от пользователя
    config = get_user_input()
    
    print("\n🔧 Применяем настройки...")
    
    # Обновляем файлы
    success = True
    success &= update_conf_py(config)
    success &= update_index_rst(config)
    
    if success:
        print("\n🎉 Настройка завершена успешно!")
        print("\nСледующие шаги:")
        print("1. Просмотрите изменения в source/conf.py и source/index.rst")
        print("2. Запустите: make html")
        print("3. Начните редактировать содержимое под ваш проект")
        print("4. Удалите демонстрационные файлы, если они не нужны")
        print("\n💡 Совет: Резервные копии сохранены в папке backup_original/")
    else:
        print("\n❌ Произошли ошибки при настройке. Проверьте сообщения выше.")
        sys.exit(1)


if __name__ == '__main__':
    main() 