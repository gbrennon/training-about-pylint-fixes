"""Repository for managing tasks in JSON file."""

import json
import os


class TaskRepository:
    """Repository for managing tasks in JSON file."""

    def __init__(self, filename='tasks.json'):
        """Initialize a new task repository.

        Args:
            filename (str): Path to the JSON file storing tasks.
        """
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create the storage file if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def get_all(self):
        """Retrieve all tasks from storage."""
        with open(self.filename, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        return tasks

    def get_by_id(self, task_id):
        """Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            dict: Task data or None if not found.
        """
        tasks = self.get_all()
        for task in tasks:
            if task['id'] == task_id:
                return task
        return None

    def save(self, task):
        """Save a task to storage, updating if exists.

        Args:
            task (task.Task): The task object to save.
        """
        tasks = self.get_all()
        found = False
        for t in tasks:
            if t['id'] == task.id:
                t['description'] = task.description
                t['completed'] = task.completed
                found = True
                break
        if not found:
            tasks.append({
                'id': task.id,
                'description': task.description,
                'completed': task.completed
            })
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)

    def delete(self, task_id):
        """Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete.
        """
        tasks = self.get_all()
        tasks = [t for t in tasks if t['id'] != task_id]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)
