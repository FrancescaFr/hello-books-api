from app.models.book import Book
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book_returns_book(client, one_saved_book):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_book.id
    assert response_body["title"] == one_saved_book.title
    assert response_body["description"] == one_saved_book.description 

def test_create_book(client):
    # arrange (we do have this b/c we are creating a dict to send)
    NEW_BOOK = {"title":"New Book", "description": "A really great new book"}

    # act 
    response = client.post("/books", json=NEW_BOOK)
    response_body = response.get_json(as_text=True)
    # real_book = Book.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Book {NEW_BOOK.title} successfully created"