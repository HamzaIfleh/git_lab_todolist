
"""Filtering and search features for the To-Do List."""


def search_tasks(tasks, keyword):
    """Return tasks whose titles contain the keyword."""
    keyword = keyword.strip().lower()

    if not keyword:
        return tasks.copy()

    return [
        task for task in tasks
        if isinstance(task.get("title"), str)
        and keyword in task["title"].lower()
    ]


def filter_tasks(tasks, status="all"):
    """Filter tasks by completion status."""
    if status == "all":
        return tasks.copy()

    if status == "completed":
        return [task for task in tasks if task["completed"]]

    if status == "pending":
        return [task for task in tasks if not task["completed"]]

    raise ValueError(
        "Status must be 'all', 'completed', or 'pending'."
    )


def search_and_filter(tasks, keyword="", status="all"):
    """Search by title and filter by completion status."""
    matching_tasks = search_tasks(tasks, keyword)
    return filter_tasks(matching_tasks, status)
