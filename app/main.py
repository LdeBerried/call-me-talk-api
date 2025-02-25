import uuid
from typing import Any

from fastapi import FastAPI
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


class Book(BaseModel):
    book_id: uuid.UUID = Field(
        examples=[uuid.uuid4()],
        description="Unique identifier of the book.",
        title="ID",
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


@app.get(
    "/books",
    tags=["Books"],
    summary="You have a non-markdown Request summary",
    description="**Retrieve all books** from collection. <br/> *This description renders markdown.*",
)
async def get_books() -> list[Book]:
    raw_books = [book for book in GET_BOOKS_JSON]

    # Creating book from comprehension list + Book __init__
    result = [
        Book(
            book_id=uuid.UUID(raw_book.get("book_id")),
            book_title=raw_book.get("book_title"),
            isbn=raw_book.get("isbn"),
            year=raw_book.get("year"),
            authors=raw_book.get("authors"),
        )
        for raw_book in raw_books
    ]

    # Creating book from dict spread + Book __init__
    result = [Book(**raw_book) for raw_book in raw_books]

    # Creating book from Pydantic's model_validate
    result = [Book.model_validate(raw_book) for raw_book in raw_books]
    return result