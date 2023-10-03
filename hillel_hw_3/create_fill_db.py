import logging
import sqlite3

from faker import Faker
from typing import List

logger = logging.getLogger(__name__)


def create_tables(cr, command_file_name):
    with open(command_file_name, 'r') as fd:
        sql_file = fd.read()

    sql_commands = sql_file.split(';')
    for query in sql_commands:
        try:
            cr.execute(query)
        except sqlite3.OperationalError as e:
            logger.error(e)


def fill_tables(cr, table_name: str, columns: str, qty_of_records: int, fields_type_to_fake: List[str]):
    fake = Faker()
    values_to_insert = []
    for _ in range(qty_of_records):
        values = tuple(fake.__getattr__(field_type)() for field_type in fields_type_to_fake)
        values_to_insert.append(values)
    cr.executemany(f"INSERT INTO {table_name} {columns} VALUES ({('?, ' * len(fields_type_to_fake))[:-2]})",
                   values_to_insert)


if __name__ == '__main__':
    conn = sqlite3.connect('instance/test_db.db')
    cr = conn.cursor()

    create_tables(cr, 'create_tables.sql')
    fill_tables(cr, 'customers', '(first_name, last_name)', 100,  ['first_name', 'last_name'])
    fill_tables(cr, 'tracks', '(name, duration)', 100,  ['catch_phrase', 'random_int'])

    cr.close()
    conn.commit()
    conn.close()
