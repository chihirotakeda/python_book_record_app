import pandas as pd
import requests
from xml.etree import ElementTree
import csv
import sqlite3
from python_book_record_app.info import *


def get_gr_book_info(shelf, per_page):
    url = "https://www.goodreads.com/review/list"
    params = {
        'v': '2',
        'id': Info.id,
        'shelf': shelf,
        'sort': 'author',
        'key': Info.key,
        'per_page': per_page
    }

    response_shelf = requests.get(url, params)
    shelf_content = response_shelf.content
    root = ElementTree.fromstring(shelf_content)
    reviews = root.iter('review')
    book_info_ls = []
    for review in reviews:
        gid = int(review.find('./book/id').text)
        isbn = review.find('./book/isbn').text
        title = review.find('./book/title').text
        author = review.find('.//author/name').text
        image_url = review.find('./book/image_url').text
        link = review.find('./book/link').text
        publisher = review.find('./book/publisher').text
        read_count = int(review.find('read_count').text)

        book_info = {
            'gid': gid,
            'isbn': isbn,
            'title': title,
            'author': author,
            'image_url': image_url,
            'link': link,
            'publisher': publisher,
            'read_count': read_count
        }
        book_info_ls.append(book_info)
    return book_info_ls


def create_csv_file(file):
    with open(file, 'w') as csv_file:
        fieldnames = ['gid', 'isbn', 'title', 'author',
                      'image_url', 'link', 'publisher', 'read_count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        book_info = get_gr_book_info('reading-challenge-100', 100)
        writer.writerows(book_info)


def import_csv_to_db(file, dbname, tb_name):
    create_csv_file(file)
    df = pd.read_csv(file)
    conn = sqlite3.connect(dbname)
    df.to_sql(tb_name, conn, if_exists='replace')
    conn.close()


def db_rows(table, dbname):
    select_sql = 'SELECT * FROM {}'.format(table)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        print(row)
    cur.close()
    conn.close()


# import_csv_to_db('book_info.csv', 'book_info.db', 'book_info')
# db_rows('book_info', 'book_info.db')
