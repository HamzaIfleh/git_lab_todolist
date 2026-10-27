
import pytest

from filter_search import search_tasks, filter_tasks, search_and_filter


@pytest.fixture
def sample_tasks():
    return [
        {"title": "Study Python", "completed": False},
        {"title": "Finish report", "completed": True},
        {"title": "Study databases", "completed": False},
    ]


def test_search_finds_matching_titles(sample_tasks):
    result = search_tasks(sample_tasks, "Study")
    assert len(result) == 2


def test_search_ignores_letter_case(sample_tasks):
    result = search_tasks(sample_tasks, "PYTHON")
    assert result[0]["title"] == "Study Python"


def test_search_with_no_matches(sample_tasks):
    assert search_tasks(sample_tasks, "Shopping") == []


def test_filter_completed_tasks(sample_tasks):
    result = filter_tasks(sample_tasks, "completed")
    assert len(result) == 1
    assert result[0]["title"] == "Finish report"


def test_filter_pending_tasks(sample_tasks):
    result = filter_tasks(sample_tasks, "pending")
    assert len(result) == 2
    assert all(not task["completed"] for task in result)


def test_search_and_filter_together(sample_tasks):
    result = search_and_filter(sample_tasks, "Study", "pending")
    assert len(result) == 2


def test_invalid_filter_status_raises_error(sample_tasks):
    with pytest.raises(ValueError):
        filter_tasks(sample_tasks, "unknown")
def test_search_skips_tasks_without_string_titles():
    tasks = [
        {"title": "Study Python", "completed": False},
        {"title": None, "completed": False},
        {"completed": True},
    ]

    result = search_tasks(tasks, "python")

    assert result == [
        {"title": "Study Python", "completed": False}
    ]