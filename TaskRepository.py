import json
import os

class TaskRepository:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def get_all(self):
        with open(self.filename, 'r') as f:
            tasks = json.load(f)
        return tasks

    def get_by_id(self, id):
        tasks = self.get_all()
        for task in tasks:
            if task['id'] == id:
                return task
        return None

    def save(self, task):
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
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=4)

    def delete(self, id):
        tasks = self.get_all()
        tasks = [t for t in tasks if t['id'] != id]
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=4)
