# Log Analysis :: FSND

### Overview

The code affialiated with this project will allow you to do the following.

1. Query a postgressql database with using python
2. Allow for the user to query the most populor three articles of all time.
3. Allow the user to query to see the most popular articles that any given author has written.
4. Allow the user to query which day lead to more then 1% of the request errors.



## Steps to Run

In order to run the code on this repo you will need to perform the following steps

1. Install Python [Python](https://www.python.org/)
    *  Linux user Python is already installed in your system run the following commands
        * > sudo apt-get  update
          > sudo apt-get install python3.7
          > to run cltr + alt + T in terminal type python3 --version
2. Install Vagrant and set up linux virtual machine [Vagrant](https://www.vagrantup.com/intro/getting-started/)
3. Install Postgres sql in your Vagrant VM
4. Download this Repository
5. Download newsdatabase [sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  
6. In terminal run the following
  >  command psql -d news -f newsdata.sql this **make sure the sql file is in side your vagrant folder**

6. Execute python program by typing **python query.py**

> query.py is based off a class in order to run the methods in side the
> class, under the if__name__ == '__main__' use the variable database_connection. **METHOD NAME**

<!-- ### VIEWS FOR FINDING 1% OF REQUEST LEAD ERRORS
psqlquery.sql has the view and query to test against the database, please remember to download the newsdata base in order for this to work


>  CREATE VIEW findlog AS
  SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as totallogcount
  FROM log
  GROUP BY Date;

> CREATE VIEW elogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as errcount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date; -->
