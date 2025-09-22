import csv

import click

from opinions_app import app, db
from opinions_app.models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    # Открыть файл.
    with open('opinions.csv', encoding='utf-8') as f:
        # Создать итерируемый объект, который отображает каждую строку
        # в качестве словаря с ключами из шапки файла.
        reader = csv.DictReader(f)
        # Для подсчёта строк добавить счётчик.
        counter = 0
        for row in reader:
            # Распакованный словарь использовать
            # для создания экземпляра модели Opinion.
            opinion = Opinion(**row)
            # Добавить объект в сессию и закоммитить
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено мнений: {counter}')
