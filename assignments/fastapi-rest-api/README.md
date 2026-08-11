# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating routes, handling request data, and returning JSON responses for a small in-memory book catalog.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Create a new FastAPI application that exposes endpoints for managing books.

#### Requirements
Completed program should:

- Create an instance of `FastAPI` with a descriptive title
- Define a root endpoint that returns a welcome message
- Use JSON-friendly data structures for a list of books
- Run the app locally with Uvicorn

### 🛠️ Implement CRUD Endpoints

#### Description
Add endpoints to create, read, update, and delete books from an in-memory list.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book by ID
- Implement `POST /books` to add a new book
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book
- Return appropriate status codes such as `200`, `201`, and `404`
- Validate incoming data using a Pydantic model
