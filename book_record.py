from bottle import run, redirect, request, route, template
import sqlite3

book_db = "sample_book.db"


@route("/book_list")
def book_list():
    books = get_list()
    return template('book_record', books=books)


def get_list():
    conn = sqlite3.connect(book_db)
    c = conn.cursor()
    c.execute("SELECT title, volume, author, publisher, memo FROM books")
    books = []
    for row in c.fetchall():
        books.append({
            "title": row[0],
            "volume": row[1],
            "author": row[2],
            "publisher": row[3],
            "memo": row[4]
        })
    conn.close()
    return books


run(host='localhost', port=8080, debug=True)