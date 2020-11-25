from flask import Flask
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

tasks_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books) 

# INDEX
# GET '/books'

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books",  methods=['POST'])
def create_book():
    title = request.form['title']
    genre     = request.form['genre']
    publisher = request.form['publisher']
    author    = request.form['author']
    author    = user_repository.select(user_id)
    book      = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')


# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

