"""REST API for user management."""

from flask import Flask, jsonify, request
from composition_root import user_service
from core.user import User

app = Flask(__name__)


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id: str):
    """Get a user by ID."""
    try:
        user = user_service.get_user(user_id)
        return jsonify(user.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user."""
    data = request.get_json()
    user = User(
        user_id=data["id"],
        name=data.get("name"),
        email=data.get("email")
    )
    user_service.save_user(user)
    return jsonify(user.to_dict()), 201


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id: str):
    """Delete a user by ID."""
    user_service.delete_user(user_id)
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(debug=True)
