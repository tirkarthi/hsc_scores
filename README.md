# hsc_scores
A simple bot to crawl scores for 2017 Anna univ counselling

The 2017 marks are available at `marks-2017.db` and `marks-2017.csv` as SQLite and csv respectively. I am not responsible for the correctness of the data since it was scraped. Use it at your own discretion.

### Example usage

```bash
➜  hsc_scores git:(master) ✗ sqlite3 marks-2017.db
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite> .headers on
sqlite> .mode column
sqlite> select * from marks where bname="Civil Engineering" limit 1;

bc          bcm         bcode       bname              hd                                                    mbc         oc          sca         sc          st
----------  ----------  ----------  -----------------  ----------------------------------------------------  ----------  ----------  ----------  ----------  ----------
163.0       168.25      CE          Civil Engineering  2710 . Karpagam College Of Engineering (AUT)          162.75      170.75      79.75       121.75      94.25
```

All the best.
