"""FastAPI application with a simple ping endpoint."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping() -> dict[str, str]:
    """Return a pong message when called."""
    return {"message": "pong"}
