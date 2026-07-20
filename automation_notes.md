<!-- 1 -->

`python -m venv venv`

python — запускает интерпретатор;
-m — запускает модуль как программу;
первое venv — модуль Python;
второе venv — имя создаваемой директории.

Активировать в Git Bash на Windows:
`source venv/Scripts/activate`

Проверить используемый Python:
`which python`

Выйти из виртуального окружения:
`deactivate`


## Зависимости

Установить библиотеки:
`python -m pip install pytest requests python-dotenv`

Показать установленные библиотеки:
`python -m pip list`

Сохранить зависимости:
`python -m pip freeze > requirements.txt`

Установить зависимости готового проекта:
`python -m pip install -r requirements.txt`


## Работа с директориями

Создать вложенные директории:
`mkdir -p tests/api`

## Pytest

Запустить все тесты:
`python -m pytest`

Запустить с подробным выводом:
`python -m pytest -v`

Показать вывод print:
`python -m pytest -s`

Запустить конкретный файл:
`python -m pytest tests/api/test_example.py`

<!-- 2 -->

