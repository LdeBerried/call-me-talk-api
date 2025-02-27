# Call Me! Creando APIs que dicen *muchas* cosas con Python

This repository contains the FastAPI project used for the live demo of the Call Me! Creating APIs that say a lot of 
things with Python.
The project contains 6 branches exemplifying the different changes the API undergoes throughout the presentation.

## Branches
### 1-basic-api
Contains a simple api with a single endpoint.
### 2-spicy-api
Contains descriptions for the api, the endpoint and documentation is generated from a pydantic BaseModel.

### 3-naming-api
Contains descriptions for the api, the initial endpoint and adds a second endpoint for singleton resource retrieval.

### 4-versioning-api
Contains the previous endpoints and a new version of the singleton resource retrieval endpoint, organized with versioning.

### 5-extra-responses
Contains a resource creation endpoint that uses examples.

### 6-openapi-extra
Contains a modification of the swagger ui css.