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


    def most_popular_authors(self):
        self.cursor.execute("SELECT * FROM authors ")
        authors = self.cursor.fetchall()

        for author in authors:
            print(authors)

    def most_popular_article(self):
        query = """
                   SELECT A.title, count(L.path)
                    FROM  log AS L
                    LEFT JOIN articles as A on A.slug = L.path
                    WHERE L.path = '/article/'
                    GROUP BY A.title, L.path
                    ORDER BY count(L.path) DESC
                    LIMIT 3;
            """
        self.cursor.execute(query)
        articles = self.cursor.fetchall()

        for article in articles:
            print('"{title}" {count}'.format(
                title=article[0], count=article[1]))


if __name__ == '__main__':
    database_connection = DatabaseConnection()
    # database_connection.most_popular_authors()
    database_connection.most_popular_article()
