class Task:
    def __init__(self, title, description="", deadline=None):
        self.title = title
        self.description = description if description != "" else None
        self.deadline = deadline if deadline != "" else None