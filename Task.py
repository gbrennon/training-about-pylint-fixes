class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def get_details(self):
        return f"Task({self.id}): {self.description} [{'Completed' if self.completed else 'Pending'}]"
