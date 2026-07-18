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

Запустить все тесты: 
`python -m pytest` 

Запустить все тесты с подробным выводом: 
`python -m pytest -v` 

Запустить один файл:
`python -m pytest tests/test_project.py -v` 

Запустить один тест: 
`python -m pytest tests/test_project.py::test_division -v` 

Запустить тесты по части названия: 
`python -m pytest -k "division" -v` 

Правила поиска тестов: - файл обычно начинается с `test_`; - тестовая функция начинается с `test_`; - `assert` проверяет, что выражение истинно.