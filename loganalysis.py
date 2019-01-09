#!/usr/bin/env python

import psycopg2


def main():

    """
    This program will connect to a local database and calculate three
    different metrics related to http requests made on a website.
    """
    print("What are the most popular three articles of all time?\n")
    get_most_popular_article()
    print("Who are the most popular article authors of all time?\n")
    get_most_popular_author()
    print("On which days did more than 1% of requests lead to errors?\n")
    get_error_days()


def get_most_popular_article():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        """select most_read_article.title, most_read_article.views
        from most_read_article limit 3;"""
        )
    results = cursor.fetchall()
    for result in results:
        print("%s -- %d views" % (result[0], result[1]))
    print("\n")
    conn.close()


def get_most_popular_author():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        """select authors.name, sum(most_read_article.views) as views
        from most_read_article
        left join authors on most_read_article.author = authors.id
        group by authors.name order by views desc;"""
        )
    results = cursor.fetchall()
    for result in results:
        print("%s -- %d views" % (result[0], result[1]))
    print("\n")
    conn.close()


def get_error_days():
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(
        """select to_char(temp.date, 'YYYY-MM-DD'), temp.failure_rate
        from (select date_trunc('day', log.time) as date,
        count(case when status != '200 OK' then status end)::decimal
        / count(status) as failure_rate
        from log group by date) as temp where temp.failure_rate >= 0.01;"""
        )
    results = cursor.fetchall()
    for result in results:
        print("%s -- %.1f %% errors" % (result[0], result[1]*100))
    print("\n")
    conn.close()


if __name__ == '__main__':
    main()
