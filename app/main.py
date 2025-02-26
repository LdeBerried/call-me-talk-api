import os

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from starlette.staticfiles import StaticFiles

from .api.routers.v1 import books as v1_books
from .api.routers.v2 import books as v2_books

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
    {"name": "v1", "description": "This tag groups every v1 EP existing"},
    {"name": "v2", "description": "This tag groups every v2 EP existing"},
    {
        "name": "Check Out",
        "description": "You can have empty tags, so watch out to keep tags updated",
    },
]

app = FastAPI(
    title="MyLibrary",
    description=APP_DESCRIPTION,
    summary="MyLibrary API for learning purposes", # No MD
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
    docs_url=None
)

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + "API",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="https://alicebiometrics.com/favicon.ico",
    )


app.include_router(v1_books.router)
app.include_router(v2_books.router)
