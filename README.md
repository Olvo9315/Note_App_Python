# Приложение для Управления Заметками
Это простое приложение на Python, которое позволяет пользователям выполнять операции CRUD (Create, Read, Update, Delete) с заметками. Пользователи могут взаимодействовать с программой через интерфейс командной строки (CLI), чтобы эффективно управлять своими заметками.

## Особенности
- **Чтение Заметок:** Просмотр всех заметок, хранящихся в системе.
- **Получение Заметки по Идентификатору:** Получение конкретной заметки, предоставив ее уникальный идентификатор.
- **Добавление Заметки:** Создание новой заметки, указав заголовок и текст.
- **Обновление Заметки:** Изменение содержимого существующей заметки.
- **Удаление Заметки:** Удаление заметки из системы по ее идентификатору.
- **Сортировка Заметок по Дате:** Возможность сортировки заметок по дате их создания.
- **Сохранение Данных:** Заметки сохраняются в файле JSON (notes.json) для постоянного хранения между сеансами.

## Структура Файлов
- **main.py:** Содержит основную логику программы, включая интерфейс командной строки и варианты меню.
- **note_manager.py:** Определяет класс NoteManager, отвечающий за управление заметками.
- **note.py:** Определяет класс Note, представляющий отдельные заметки.
- **notes.json:** Файл JSON, используемый для постоянного хранения данных о заметках.
- **README.md:** Этот файл, предоставляющий обзор приложения и инструкции по его использованию.
