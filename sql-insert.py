import sys
import json
import sqlite3

conn = sqlite3.connect('data')

# Table schema : create table marks("an_rank" text, "code" text, "name" text, "district" text, "course" text, "cut_off" text, "caste" text)

with open(sys.argv[1]) as f:
    rows = json.loads(f.read())
    cursor = conn.cursor()
    for row in rows:
        columns = ', '.join(map(lambda x: '_'.join(x.split()), row.keys()))
        placeholders = ", ".join('?' * len(row.values()))
        values = list(map(str, row.values()))
        actual = []
        for value in values:
            try:
                actual.append(float(value))
            except Exception as e:
                actual.append(value)
        sql = 'INSERT INTO marks ({}) VALUES ({})'.format(columns, placeholders)
        cursor.execute(sql, values)
    cursor.close()
conn.commit()
conn.close()
