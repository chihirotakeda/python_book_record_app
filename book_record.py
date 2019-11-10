from bottle import run, redirect, request, route, template, static_file
import sqlite3
from goodreads import client

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


@route("/add_book")
def add_book():
    return template('book_add')


@route("/book_home")
def show_current_book_info():
    book_info = get_basic_book_info("0141040343")
    book_description = get_book_description("0141040343")
    return template('book_home', book_info=book_info, book_description=book_description)


def get_basic_book_info(isbn):
    gc = client.GoodreadsClient("QSaZ6iPhVmKVYUMN5rzCfw", "5v8xoxLgyMCbcuNGBgiWo8xkhqnfctEWF20r6Xdas")
    book = gc.book(None, isbn)
    title = book.title
    author = book.authors[0]
    publisher = book.publisher
    img_url = book.image_url
    book_link = book.link
    book_info = [title, author, publisher, img_url, book_link]
    return book_info


def get_book_description(isbn):
    gc = client.GoodreadsClient("QSaZ6iPhVmKVYUMN5rzCfw", "5v8xoxLgyMCbcuNGBgiWo8xkhqnfctEWF20r6Xdas")
    book = gc.book(None, isbn)
    description = book.description
    return description


# Static file
@route("/static/<filename:path>")
def css(filename):
    return static_file(filename, root="./static")


@route("/static/font/<filename:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filename):
    return static_file(filename, root="static/font")


@route("/static/img/<filename:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filename):
    return static_file(filename, root="./static/img")


@route("/static/js/<filename:re:.*\.js>")
def js(filename):
    return static_file(filename, root="static/js")


run(host='localhost', port=8080, debug=True)