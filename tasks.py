"""Add and list tasks."""


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": new_id, "title": title, "done": False}
    tasks.append(task)
    return task


def get_tasks(tasks, done=None):
    if done is None:
        return list(tasks)
    return [t for t in tasks if t["done"] == done]
