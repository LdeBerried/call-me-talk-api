import uuid
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

POST_BOOK_JSON = {
    "book_title": "Little Women",
    "isbn": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
    "year": 1868,
    "authors": ["Louise May Alcott"],
    "check_outs": [],
}
POST_BOOK_WITH_MULTIPLE_AUTHORS_JSON = {
    "book_title": "The Long Earth",
    "isbn": "978-0-06-206775-3",
    "year": 2016,
    "authors": ["Terry Pratchett", "Stephen Baxter"],
    "check_outs": [],
}

GET_BOOK_JSON = {
"book_id": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
        "book_title": "Little Women",
        "isbn": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
        "year": 1868,
        "authors": ["Louise May Alcott"],
        "check_outs": [],
}

GET_BOOK_WITH_CHECKOUT_JSON = {
    "book_id": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
    "book_title": "Little Women",
    "isbn": "a6cc9558-ae56-4533-bbde-8db27e8b00c7",
    "year": 1868,
    "authors": ["Louise May Alcott"],
    "check_outs": [{"date": "2025-02-23", "ongoing": True, "recipient": "Jane Doe"}],
}


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


class BookFormat(Enum):
    HARDCOVER = "hard cover"
    SOFTCOVER = "soft cover"
    AUDIOBOOK = "audio book"


class Book(BaseModel):
    book_id: uuid.UUID | None = Field(
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
