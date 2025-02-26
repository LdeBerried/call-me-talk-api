import uuid

from fastapi import Path, APIRouter, Body

from app.src.domain.book import (
    GET_BOOKS_JSON,
    Book,
    GET_BOOK_JSON,
    GET_BOOK_WITH_MULTIPLE_AUTHORS_JSON, POST_BOOK_JSON, POST_BOOK_WITH_MULTIPLE_AUTHORS_JSON,
)

GET_BOOKS_EP_DESCRIPTION = """
## GET /books

Retrieves a list of books from the library's collection.

### Description

This endpoint is used to fetch a list of books available in the library's collection. The collection is updated daily to ensure the most up-to-date information is provided to users. Books can be filtered and sorted using query parameters (such as title, authors, year, or format) to facilitate efficient searching and retrieval.

### How It Works

When a request is made to this endpoint, the server queries the database for all available books and returns a JSON array of book objects. Each book object adheres to the following `Book` schema:

### Schema Details

- **Book ID** `book_id`: A unique identifier for each book. This is a universally unique identifier (UUID).
- **Title** `book_title`: The title of the book.
- **ISBN** `isbn`: The International Standard Book Number (ISBN) that uniquely identifies the book.
- **Publishing Year** `year`: The year when the book was first published. It can be any year up to and including 2025.
- **Format** `book_format`: The format of the book, such as softcover or hardcover.
- **Library Code** `library_code`: A unique code assigned by the library, must end with the character '-' followed by a number.
- **Authors** `authors`: A list of authors who contributed to the book.
- **Check Outs** `check_outs`: A list of instances when the book was checked out, if any.

### Domain Terminology

- **UUID**: Universally Unique Identifier. A 128-bit identifier used to uniquely identify information in computer systems.
- **ISBN**: International Standard Book Number. A unique identifier for books, allowing for more efficient management and sale of books.
- **Softcover**: A type of book binding that uses a flexible paper cover.
- **Hardcover**: A type of book binding that uses a rigid protective cover.
- **Audiobook**: Audible type of book avaliable for download.

"""

GET_BOOK_EP_DESCRIPTION = """
## GET /books/{book_id}

Retrieves a single book from the library's collection using its title.
### Description
This endpoint is used to fetch a single book from the library's collection. The collection is updated daily to ensure the most up-to-date information is provided. Individual books can only be retrieved by using their unique book identifier (`book_id`).

### How It Works
When a request is made to this endpoint, the server queries the database for the specific book and returns a single book object. The book object adheres to the following `Book` schema:

### Schema Details

- **Book ID** `book_id`: A unique identifier for each book. This is a universally unique identifier (UUID).
- **Title** `book_title`: The title of the book.
- **ISBN** `isbn`: The International Standard Book Number (ISBN) that uniquely identifies the book.
- **Publishing Year** `year`: The year when the book was first published. It can be any year up to and including 2025.
- **Format** `book_format`: The format of the book, such as softcover or hardcover.
- **Library Code** `library_code`: A unique code assigned by the library, must end with the character '-' followed by a number.
- **Authors** `authors`: A list of authors who contributed to the book.
- **Check Outs** `check_outs`: A list of instances when the book was checked out, if any.

### Domain Terminology
- **Book Title** `book_title`: Title for the book in string form.

"""

router = APIRouter(prefix="/v2/books", tags=["Books", "v2"])


@router.get(
    "/{book_title}",
    summary="Retrieve a specific book from the library's collection",
    description=GET_BOOK_EP_DESCRIPTION,
)
async def get_book(
    book_title: str = Path(
        description="The title of a book from the library's collection",
        title="Book Title",
        examples=["Book Title in str Format (eg. Little Women)"],
    ),
) -> Book:
    matching_books = [book for book in GET_BOOKS_JSON if book.book_title == book_title]
    result = Book.model_validate(matching_books[0])
    return result


@router.post(
    "/",
    summary="Add a new book to the library collection",
    description=GET_BOOK_EP_DESCRIPTION,
)
async def post_book(
    book: Book = Body(
        description="A new book for the library's collection. This Book has all attributes that created Books already "
                    "have *except* for `BookID`, which is asigned by this API when adding it to the library "
                    "using this endpoint.",
        title="Book",
        openapi_examples={
            "Book with one author": {
                "summary": "Book with one author",
                "value": POST_BOOK_JSON,
            },
            "Book with two authors": {
                "summary": "Book with two authors",
                "value": POST_BOOK_WITH_MULTIPLE_AUTHORS_JSON,
            },
        },
    ),
) -> uuid.UUID:
    book.book_id = uuid.uuid4()
    return book.book_id
