##!/usr/bin/python
#please use tryme/bin/python app.py to run me

import sys
sys.path.append("..")

from flask import Flask, request, redirect, url_for
from flask.templating import render_template
from library_app.src.code.dto import AuthorDto, BookDto, AuthorRef
from library_app.src.code.facade import LibraryManager
from library_app.src.code.sahelper import SaHelper
from library_app.etc import config
from library_app.src.code.validate import AuthorForm, BookForm
import jsonpickle

app = Flask(__name__)

helper = SaHelper(config.profile.db.url)
helper.create_all()
facade = LibraryManager(helper.session)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/books/validate", methods=["POST"])
def validate_book():
    form = BookForm(name = request.form["name"])
    if form.validate():
        return jsonpickle.encode(form.errors)
    
    return jsonpickle.encode(form.errors)

@app.route("/authors/validate", methods=["POST"])
def validate_author():
    form = AuthorForm(name = request.form["name"])
    if form.validate():
        return jsonpickle.encode(form.errors)
    
    return jsonpickle.encode(form.errors)

@app.route("/authors/create", methods=["POST"])
def create_author():
    author = AuthorDto(name = request.form["name"])
    facade.create_author(author)
    return redirect(url_for("authors"))

@app.route("/authors/delete", methods=["POST"])
def delete_author():
    author = AuthorDto(name = request.form["name"])
    facade.delete_author(author)
    return redirect(url_for("authors"))

@app.route("/authors/update", methods=["POST"])
def update_author():
    author_dto = AuthorDto(name = request.form["old_name"])
    author = facade.get_author(author_dto)
    author.name = request.form["new_name"]
    facade.update_author(author)
    return redirect(url_for("authors"))

@app.route("/authors/search")
def search_authors():
    authors = facade.search_authors()
    return jsonpickle.encode(authors)

@app.route("/authors")
def authors():
    authors = facade.search_authors()
    return render_template("authors.html", authors = authors)

@app.route("/books/search")
def search_books():
    expression = request.args.get("expression")
    books = facade.search_books(expression)
    return jsonpickle.encode(books)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/books")
def books():
    books = facade.search_books("")
    return render_template("books.html", books = books)

@app.route("/books/create", methods=["POST"])
def create_book():
    book = BookDto(name = request.form["name"])
    for author in request.form.getlist("authors"):
        book.authors.append(AuthorDto(name = author))
    facade.create_book(book)
    return redirect(url_for("books"))
    #return str(request.form)

@app.route("/books/update", methods=["POST"])
def update_book():
    book_dto = BookDto(name = request.form["old_name"])
    book = facade.get_book(book_dto)
    
    book.name = request.form["name"]
    book.authors = []
    for author in request.form.getlist("authors"):
        book.authors.append(AuthorDto(name = author))
    
    facade.update_book(book)
    return redirect(url_for("books"))
    #return str(request.form)

@app.route("/books/delete", methods=["POST"])
def delete_book():
    book = BookDto(name = request.form["name"])
    facade.delete_book(book)
    return redirect(url_for("books"))
    #return "'%s' deleted ..." % request.form["name"]

if __name__ == "__main__":
    app.debug = True
    app.run()

