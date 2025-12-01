# Task API

This API provides CRUD operations for managing tasks using FastAPI and stores data in a JSON file.

## Installation

First, install Poetry if you haven't already:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Then, install the project dependencies:

```sh
poetry install
```

## Running the API

Start the FastAPI server with:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### List all tasks

```sh
curl http://127.0.0.1:8000/tasks/
```

### Get a single task by ID

```sh
curl http://127.0.0.1:8000/tasks/1
```

### Create a new task

```sh
curl -X POST http://127.0.0.1:8000/tasks/ -H "Content-Type: application/json" -d '{"description": "New task"}'
```

### Update a task by ID

```sh
curl -X PUT http://127.0.0.1:8000/tasks/1 -H "Content-Type: application/json" -d '{"description": "Updated task"}'
```

### Delete a task by ID

```sh
curl -X DELETE http://127.0.0.1:8000/tasks/1
