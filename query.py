#!/usr/bin/env python3

import psycopg2  # needed to create connection to database
import pprint
"""https://docs.python.org/3/library/pprint.html
allows to format the
object we are printing"""


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

    def most_popular_article(self):
        # database name
        dbnews = 'news'
        # created variable to close()
        db = psycopg2.connect(database=dbnews)
        query_article = """
        Select title, count(*) as views
        from articles join log ON articles.slug = substring(log.path, 10)
        GROUP BY title ORDER BY views desc limit 3;
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
        print(author)
        # for authors in author:
        #     print(author . "\n")

# methon below will query for the days where the errors were greater than 1%
    def days_greater_than_1p(self):
        dbnews = "news"
        db = psycopg2.connect(database=dbnews)
        """
        below query i used the following documentation to complete
        https://stackoverflow.com/questions
        /38136854/how-to-use-multiple-with-statements-in-one-postgresql-query"
        http://www.postgresqltutorial.com/postgresql-recursive-query/
        https://www.tutorialspoint.com/postgresql/postgresql_with_clause.html"""
        query_gt1p = """
                WITH total_request AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
                 ), total_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
                ), total_failures AS (
                SELECT total_request.day,
                total_errors.count::float / total_request.count::float * 100
                 AS total_error_count
                FROM total_request, total_errors
                WHERE total_request.day = total_errors.day
                )
               SELECT * FROM total_failures WHERE total_error_count > 1;
               """
        self.cursor.execute(query_gt1p)
        one_percent = self.cursor.fetchall()
        db.close()
        print(one_percent)

        return


if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.most_popular_article()
    database_connection.most_popular_authors()
    database_connection.days_greater_than_1p()
