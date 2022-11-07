from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET","POST"])
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = [book.to_dict() for book in books]
        return jsonify(books_response)
    elif request.method == "POST": 
        request_body = request.get_json()  # type: ignore
        new_book = Book(title=request_body["title"], 
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created!", 201)

@books_bp.route("/<id>", methods=["GET"])
def get_book(id):
    validate_model(Book,id)
    book = Book.query.get(id)
    return jsonify(book.to_dict())

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     book_list = []
#     for book in book_list:
#         book_list.append({
#             "id" : book.id, 
#             "title" : book.title, 
#             "description" : book.description}) 
#     return jsonify(book_list)

# @books_bp.route("/<book_id>", methods = ["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#     return jsonify({
#         "id" : book.id, 
#         "title" : book.title, 
#         "description" : book.description})

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"object '{model_id}' is invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{model_id} not found"}, 404))


