# ETL Pipeline for Sparkify

## Description
An ETL model designed using Postgres SQL for Sparkify database, modeling user activity data to create a database and ETL pipeline for a music streaming app. 

## Database
The database ```sparkify``` consists of 5 tables consisting fact and dimension tables.

There is one fact table : 

```songplays``` 

and four dimension tables:
```
1. users
2. songs
3. artists
4. time
```


## Directory Structure

    ├── README.md
    ├── create_tables.py
    ├── etl.py
    ├── sql_queries.py
    ├── test.ipynb
    ├── data
        └── log_data
         └── 2018
          └── 11
        └── user_data
