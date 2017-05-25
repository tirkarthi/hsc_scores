# hsc_scores
A simple bot to crawl scores for 2016 Anna univ counselling

# Installation

* Activate virtualenv
* `pip install -r requirements.txt`
* Run the bot as `python bot.py` which dumps each college marks as json of the form collegecode.json
* Create data using `sqlite3 data` and then run the create table command available as comment in `sql-insert.py` and then run `python sql-insert.py`

# SQLite database

The SQLite database is available as `data`. Run `sqlite3 data`. Use `.tables` which gives a single table name that contains all the marks for 2016. Use `.schema <table_name>` to get the schema and the column names are self-documentary.

# Todo

* Make the database as excel sheets.

All the best!
