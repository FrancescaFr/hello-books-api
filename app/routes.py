from flask import Blueprint, jsonify, abort, make_response
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Dune", "A fantasy novel set in an imaginary world."),
#     Book(2, "IQ84", "A dystopian scifi novel"),
#     Book(3, "The Great Train Robbery", "Historical Fiction novel"),
# ]

#books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     book_list = []
#     for book in books:
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

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))



# hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello-world")

# @hello_world_bp.route("", methods=["GET"])
# def handle_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body

# @hello_world_bp.route("/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#   "name": "Ada Lovelace",
#   "message": "Hello!",
#   "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body