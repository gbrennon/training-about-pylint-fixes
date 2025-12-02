# User Management API

## Running the Application

1. Install Poetry (if not already installed):
   ```sh
   pip install poetry
   ```

2. Install dependencies:
   ```sh
   poetry install
   ```

3. Start the API server:
   ```sh
   poetry run python src/api.py
   ```

## Testing with curl

### Get a user
```sh
curl http://localhost:5000/users/your_user_id
```

### Create a user
```sh
curl -X POST -H "Content-Type: application/json" -d '{"id":"1","name":"John Doe","email":"john@example.com"}' http://localhost:5000/users
```

### Delete a user
```sh
curl -X DELETE http://localhost:5000/users/your_user_id
