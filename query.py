#!/usr/bin/env python

import psycopg2  # needed to create connection to database
import pprint
""" https://docs.python.org/3/library/pprint.html
    allows to format the object we are printing"""


"""
3 queries

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time ?
3. On Which days did more than 1% of the request lead to errors

(think about adding views to the queries)
"""

# following code reference pynative.com


# using class to connect to database  using try/catch for errors

class DatabaseConnection:
    def __init__(self):
        try:
            dbnews = 'news'
            self.connection = psycopg2.connect(database=dbnews)
            self.cursor = self.connection.cursor()

        except:
            pprint("Cannot Connect to database")


# method below will be used to get back the most
# popular three articles of all timeself

"""
https://stackoverflow.com/questions/8578385/postgresql-create-view - reference for the views created
"""

    def most_popular_article(self):
        # database name
        dbnews = 'news'
        # created variable to close()
        db = psycopg2.connect(database=dbnews)
        query_article = """
        Select title, count(*) as views from articles join log ON articles.slug = substring(log.path, 10) GROUP BY title ORDER BY views desc limit 3
        """
        self.cursor.execute(query_article)
        articles = self.cursor.fetchall()
        db.close()
        print(articles)

    def most_popular_authors(self):
        dbnews = 'news'
        db = psycopg2.connect(database=dbnews)
        query_authors = """SELECT authors.name, count(*) as views
                  FROM articles
                  JOIN authors
                  ON articles.author = authors.id
                  JOIN log
                  ON articles.slug = substring(log.path, 10)
                  WHERE log.status LIKE '200 OK'
                  GROUP BY authors.name ORDER BY views DESC LIMIT 3;"""
        self.cursor.execute(query_authors)
        author = self.cursor.fetchall()
        db.close()
        print("these are the top three {}".format(author))
        # for authors in author:
        #     print(author . "\n")

# methon below will query for the days where the errors were greater than 1%
    def days_greater_than_1p(self):
        dbnews = "news"
        db = psycopg2.connect(database=dbnews)
        # view codeis on the readme file
        query_gt1p = """
          SELECT elogs.date, round(100.0*errcount/totallogcount,2) as percent
                      FROM findlog, elogs
                      WHERE findlog.date = elogs.date
                      AND errcount > totallogcount/100;
         """
            one_percent = self.cursor.fetchall()
            db.close()
            print(one_percent)


if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.most_popular_article()
    database_connection.most_popular_authors()
    database_connection.days_greater_than_1p()
