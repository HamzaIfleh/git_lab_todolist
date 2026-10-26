import pytest

from tasks import add_task, get_tasks


def test_first_task_gets_id_1():
    tasks = []
    task = add_task(tasks, "Buy milk")
    assert task == {"id": 1, "title": "Buy milk", "done": False}
    assert tasks == [task]


def test_blank_title_raises_value_error():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_get_tasks_returns_only_pending():
    tasks = []
    add_task(tasks, "Buy milk")
    add_task(tasks, "Read book")
    tasks[0]["done"] = True
    assert get_tasks(tasks, done=False) == [{"id": 2, "title": "Read book", "done": False}]
