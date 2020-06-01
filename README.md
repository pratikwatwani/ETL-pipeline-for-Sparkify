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

![Database](https://github.com/pratikwatwani/ETL-pipeline-for-Sparkify/blob/master/Database.png)

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
           └── 2018-11-01-events.json
           └── 2018-11-012-events.json
           .
           .
           └── 22018-11-30-events.json
        └── song_data
         └── A
          └── A
           └── A
           └── B
           └── C
          └── B
           └── A
           └── B
           └── C

## Running the Project

Step 1: In a shell, run ```create_tables.py``` with ```python create_tables.py``` which will call queries from ```sql_queries.py```

Step 2: Run ```etl.py``` to execute the pipeline

Step 3: Use ```test.ipynb``` notebook to view tables and other SQL queries (EDA shown below)


## Exploratory Data Analysis
### 1. Streaming by Location (Top 10)
```
location	                            count
--------------------------------------------------
San Francisco-Oakland-Hayward, CA	    | 691
Portland-South Portland, ME	            | 665
Lansing-East Lansing, MI	            | 557
Chicago-Naperville-Elgin, IL-IN-WI	    | 475
Atlanta-Sandy Springs-Roswell, GA	    | 456
Waterloo-Cedar Falls, IA	            | 397
Lake Havasu City-Kingman, AZ	            | 321
Tampa-St. Petersburg-Clearwater, FL	    | 307
San Jose-Sunnyvale-Santa Clara, CA	    | 292
Sacramento--Roseville--Arden-Arcade, CA     | 270
```

### 2. Streaming by Platform
```
platforms	     count
----------------------
Windows NT 6.1	| 884
Windows NT 5.1	| 955
iPhone	        | 239
X11	        | 1153
compatible	| 11
Windows NT 6.3	| 576
Windows NT 6.2	| 2
Macintosh	| 3000
```

### 3. Total album length for each artist (Top 10)
```
artist	            total_album_minutes
----------------------------------------
Clp	                |  605
Faiz Ali Faiz	        |  599
Montserrat Caballé	|  511
Blue Rodeo	        |  491
John Wesley	        |  485
Casual	                |  478
Trafik	                |  424
Jinx	                |  407
Steve Morse	        |  364
Terry Callier	        |  343
```

### 4. Streaming by week 
```
week	 count
----------------
1	   | 6813
```

### 5. Service type weight 
```
level	 count
-------------
free   | 1229
paid   | 5591
```

### 6. Top artists by each location (Top 10)
```
location	                                    name	      counts
San Francisco-Oakland-Hayward, CA	      |  Marc Shaiman	|  691
Portland-South Portland, ME	              |  Marc Shaiman	|  665
Lansing-East Lansing, MI	              |  Marc Shaiman	|  557
Chicago-Naperville-Elgin, IL-IN-WI	      |  Marc Shaiman	|  475
Atlanta-Sandy Springs-Roswell, GA	      |  Marc Shaiman	|  456
Waterloo-Cedar Falls, IA	              |  Marc Shaiman	|  397
Lake Havasu City-Kingman, AZ	              |  Marc Shaiman   |  321
Tampa-St. Petersburg-Clearwater, FL	      |  Marc Shaiman	|  307
San Jose-Sunnyvale-Santa Clara, CA	      |  Marc Shaiman	|  292
Sacramento--Roseville--Arden-Arcade, CA	      |  Marc Shaiman	|  270
```

### 7. Average album length over years
```
year	average_album_length
0     |         245.57
1961  |	        156.39
1964  |	        164.81
1969  |	        148.04
1972  |	        342.57
1982  |	        233.40
1984  |	        269.82
1985  |	        124.86
1986  |	        307.38
1987  |	        491.13
1992  |	        133.33
1993  |	        270.60
1994  |	        270.67
1997  |	        240.69
1999  |	        236.25
2000  |	        203.61
2003  |	        136.44
2004  |	        249.02
2005  |	        262.09
2007  |	        209.61
2008  |	        149.86
```
