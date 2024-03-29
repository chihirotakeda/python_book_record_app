from bottle import run, redirect, request, route, template, static_file
import sqlite3
from goodreads import client
from info import Info

book_db = "./data/book_info.db"


@route("/book_list")
def book_list():
    books = get_list()
    return template('book_record', books=books)


def get_list():
    conn = sqlite3.connect(book_db)
    c = conn.cursor()
    c.execute("SELECT title, author, isbn, image_url, link FROM book_info")
    books = []
    for row in c.fetchall():
        books.append({
            "title": row[0],
            "author": row[1],
            "isbn": row[2],
            "img": row[3],
            "link": row[4]
        })
    conn.close()
    return books


@route("/add_book")
def add_book():
    return template('book_add')


@route("/book_home")
def show_current_book_info():
    book_info = get_basic_book_info("0679772871")
    book_description = get_book_description("0679772871")
    book_img = get_book_list_img()
    return template('book_home', book_info=book_info, book_description=book_description, book_img=book_img)


def get_basic_book_info(isbn):
    gc = client.GoodreadsClient(Info.key, Info.secret)
    book = gc.book(None, isbn)
    title = book.title
    author = book.authors[0]
    publisher = book.publisher
    img_url = book.image_url
    book_link = book.link
    book_info = [title, author, publisher, img_url, book_link]
    return book_info


def get_book_description(isbn):
    gc = client.GoodreadsClient(Info.key, Info.secret)
    book = gc.book(None, isbn)
    description = book.description
    return description


def get_book_list_img():
    conn = sqlite3.connect(book_db)
    cur = conn.cursor()
    query = "SELECT image_url, title, link FROM book_info WHERE read_count = 0 AND image_url NOT LIKE '%nophoto%'"
    cur.execute(query)
    book_img = cur.fetchall()
    cur.close()
    conn.close()
    return book_img

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