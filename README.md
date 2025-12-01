# FastAPI Ping Example

This repository contains a simple FastAPI application with a single endpoint `/ping` that responds with a "pong" message.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   uv venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   uv pip install fastapi uvicorn pylint
   ```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

Or, if port 8000 is in use:
```bash
uvicorn main:app --reload --port 8001
```

The application will be available at `http://127.0.0.1:8000/ping` (or port 8001 if specified).

## Linting

To ensure code quality, use `pylint`:
```bash
pylint main.py
```

## License

MIT
