"""
Module for Task class
"""

class Task:
    """
    Represents a task with an ID, description, and completion status.
    """

    def __init__(self, task_id, description, completed=False):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task.
            description (str): Description of the task.
            completed (bool): Whether the task is completed.
        """
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        """
        Mark the task as completed.
        """
        self.completed = True

    def get_details(self):
        """
        Get a formatted string representing the task details.

        Returns:
            str: Formatted task details.
        """
        return f"Task({self.task_id}): {self.description} [{'Completed' if self.completed else 'Pending'}]"
