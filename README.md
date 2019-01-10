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
5. In terminal run the following
  >  command psql -d news -f newsdata.sql this **make sure the sql file is in side your vagrant folder**
  
6. Execute python program by typing **python query.py**
