import uuid
from enum import Enum
from typing import Any

from fastapi import FastAPI, Path, Query
from pydantic import Field, BaseModel

APP_DESCRIPTION = """
# API Description
*But you can write* **all** *this description using* `markdown`!

**MyLibrary** API is a public API that allows you to add, retrieve, edit and check out books from a collection.

## Books

You can:

 * **Add a book**: _Soon!_
 * **Retrieve a book**: _Soon!_
 * **Retrieve all books**: Retrieve every book existing in the collection.
 * **Edit a book**: _Soon!_
 * **Delete a book**: _Soon!_
 
### Other information

```
Add code examples
Or haikus if that's what you want
This markdown does that
```

# Contact 
Contact info and license info renders below *this*:
"""
OPENAPI_TAGS = [
    {
        "name": "Books",
        "description": "This is the **markdown** description for the tag.",
    },
    {
        "name": "Check Out",
        "description": "You can have empty tags, so watch out to keep tags updated",
    },
]

GET_BOOKS_JSON = [
    {
        "book_id": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
        "book_title": "Little Women",
        "isbn": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
        "year": 1868,
        "authors": ["Louise May Alcott"],
        "check_outs": [],
    },
    {
        "book_id": "b5dd7f48-5473-4c5c-9dfc-fd95c1c71d5f",
        "book_title": "Pride and Prejudice",
        "isbn": "b5dd7f48-5473-4c5c-9dfc-fd95c1c71d5f",
        "year": 1813,
        "authors": ["Jane Austen"],
        "check_outs": [],
    },
    {
        "book_id": "e3c6b716-9c1f-4f67-a8a7-5a1f48a67e34",
        "book_title": "To Kill a Mockingbird",
        "isbn": "e3c6b716-9c1f-4f67-a8a7-5a1f48a67e34",
        "year": 1960,
        "authors": ["Harper Lee"],
        "check_outs": [],
    },
    {
        "book_id": "d0efc226-5b42-4f9f-8896-3dbf6a8e515c",
        "book_title": "The Handmaid's Tale",
        "isbn": "d0efc226-5b42-4f9f-8896-3dbf6a8e515c",
        "year": 1985,
        "authors": ["Margaret Atwood"],
        "check_outs": [],
    },
    {
        "book_id": "f2a3cd0e-4b7b-4a32-a2d9-5c5b48a3e210",
        "book_title": "The Long Earth",
        "isbn": "978-0-06-206775-3",
        "year": 2016,
        "authors": ["Terry Pratchett", "Stephen Baxter"],
        "check_outs": [],
    },
]

app = FastAPI(
    title="MyLibrary",
    description=APP_DESCRIPTION,
    summary="MyLibrary API for learning purposes. **Sadly, this does not render markdown**",
    version="0.1.0",
    contact={
        "name": "Your name",
        "url": "https://mylibrary.com/contact",
        "email": "your@email.es",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=OPENAPI_TAGS,
)


class BookFormat(Enum):
    HARDCOVER = "hard cover"
    SOFTCOVER = "soft cover"
    AUDIOBOOK = "audio book"


class Book(BaseModel):
    book_id: uuid.UUID = Field(
        examples=[uuid.uuid4()],
        description="Unique identifier of the book.",
        title="ID",
        default_factory=uuid.uuid4,
    )
    book_title: str = Field(
        examples=["Little Women"], description="**Title** of the book.", title="Title"
    )
    isbn: str = Field(
        examples=[uuid.uuid4()], description="ISBN of the book.", title="ISBN"
    )
    year: int = Field(
        le=2025,
        default=2024,
        examples=[2024],
        description="Year of first publishing.",
        title="Publishing Year",
    )
    book_format: BookFormat | None = Field(
        default=BookFormat.SOFTCOVER, description="Format of the book.", title="Format"
    )
    library_code: str | None = Field(
        pattern=r"-[0-9]+$",
        default=None,
        description="Library code. Must end with character '-' and followed by a number.",
        title="Library code",
    )
    authors: list[str] = Field(
        examples=["['Louise May Alcott']"],
        description="List of authors.",
        title="Authors",
    )
    check_outs: list[Any] | None = Field(
        default=None,
        examples=[None],
        description="List of check outs.",
        title="Check outs",
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

Retrieves a single book from the library's collection.
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
- **Book ID** `book_id`: Unique identifier for each book. This is a universally unique identifier (UUID).

"""


@app.get(
    "/books",
    tags=["Books"],
    summary="Retrieve books from the library's collection",
    description=GET_BOOKS_EP_DESCRIPTION,
)
async def get_books() -> list[Book]:
    raw_books = [book for book in GET_BOOKS_JSON]
    result = [Book.model_validate(raw_book) for raw_book in raw_books]
    return result


@app.get(
    "/books/{book_id}",
    tags=["Books"],
    summary="Retrieve a specific book from the library's collection",
    description=GET_BOOK_EP_DESCRIPTION,
)
async def get_book(
    book_id: uuid.UUID = Path(
        description="A unique identifier for a book from the library's collection",
        title="Book ID",
        example="Book ID in UUID Format (eg. a358bd48-0d86-4743-988b-f81e5d88e5d7)",
    ),
    showing_random: bool | None = Query(default=None, description="Show random book"),
    hidden_random: bool | None = Query(
        default=None,
        description="Show random book. **Hidden Parameter**",
        include_in_schema=False,
    ),
) -> Book:
    result = Book.model_validate(GET_BOOKS_JSON[0])
    return result
