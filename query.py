import  psycopg2 # needed to create connection to database
import pprint #https://docs.python.org/3/library/pprint.html allows to format the object we are printing


"""
3 queries

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time ?
3. On Which days did more than 1% of the request lead to errors

(think about adding views to the queries)
"""

# following code reference pynative.com


# using class to cnnect to database  using try/catch for errors abs

class  DatabaseConnection:
    def __init__(self):
        try:
            dbnews = 'news'
            self.connection = psycopg2.connect(database=dbnews)
            self.conenction.autocommit = True
            self.cursor = self.connection.cursor()
        except:
