# Генератор HTML-страницы об организации

Этот скрипт создаёт HTML-страницу с названием и описанием организации, в которой я прохожу практическую подготовку.  
Поддерживается выбор одного из пяти предустановленных шрифтов, соответствующих стилям популярных компаний.

---

## Состав проекта

- `main.py` — основной скрипт генерации
- `template.html` — HTML-шаблон страницы
- `fonts.css` — CSS-файл с импортами Google Fonts
- `out/index.html` — итоговая HTML-страница (генерируется при запуске)

---

## Установка и запуск

### 1. Установите Python 3

Если не установлен:

```bash
brew install python
```

### 2. Создайте виртуальное окружение (рекомендуется)

```bash
python3 -m venv venv
source venv/bin/activate   # Для macOS/Linux
venv\Scripts\activate      # Для Windows
```

### 3. Установите зависимости

```bash
pip install jinja2
```

### 4. Запуск

```bash
python main.py --font=<название_шрифта>
```

Доступные варианты шрифтов:
- roboto
- opensans
- montserrat
- ptsans
- ubuntu

Пример:

```bash
python main.py --font=montserrat
```
