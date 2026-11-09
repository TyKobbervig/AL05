"""
AL05 Tests
"""

from copy import deepcopy

from ticket_data import TICKETS

from search_support import (
    id_key,
    days_key,
)

from main import (
    insertion_sort,
    build_views,
)

from search_algorithms import (
    linear_search,
    binary_search,
)


def test_insertion_sort_empty():

    ordered, comparisons, moves, trace = (
        insertion_sort([], days_key)
    )

    assert ordered == []
    assert comparisons == 0
    assert moves == 0
    assert trace == []


def test_insertion_sort_singleton():

    sample = [TICKETS[0]]

    ordered, comparisons, moves, trace = (
        insertion_sort(sample, days_key)
    )

    assert ordered == sample
    assert comparisons == 0
    assert moves == 0
    assert trace == []


def test_insertion_sort_order():

    selected, display_view, _ = (
        build_views(TICKETS, 4)
    )

    ids = [record["id"] for record in display_view]

    assert ids == [
        "T406",
        "T402",
        "T403",
        "T405",
    ]


def test_stability():

    records = [
        {"id": "A", "days_open": 7},
        {"id": "B", "days_open": 7},
        {"id": "C", "days_open": 5},
    ]

    ordered, _, _, _ = insertion_sort(
        records,
        lambda record: record["days_open"]
    )

    ids = [record["id"] for record in ordered]

    assert ids == ["C", "A", "B"]


def test_sorted_input():

    records = sorted(
        TICKETS,
        key=days_key
    )

    ordered, _, _, _ = insertion_sort(
        records,
        days_key
    )

    assert ordered == records


def test_reverse_input():

    records = sorted(
        TICKETS,
        key=days_key,
        reverse=True
    )

    ordered, _, _, _ = insertion_sort(
        records,
        days_key
    )

    expected = sorted(
        records,
        key=days_key
    )

    assert ordered == expected


def test_input_not_modified():

    original = deepcopy(TICKETS)

    insertion_sort(
        TICKETS,
        days_key
    )

    assert TICKETS == original


def test_shared_record_identity():

    ordered, _, _, _ = insertion_sort(
        TICKETS,
        days_key
    )

    assert ordered[0] is TICKETS[4]


def test_build_views_minimum_four():

    selected, _, _ = (
        build_views(TICKETS, 4)
    )

    ids = [
        record["id"]
        for record in selected
    ]

    assert ids == [
        "T403",
        "T405",
        "T402",
        "T406",
    ]


def test_build_views_minimum_seven():

    selected, _, _ = (
        build_views(TICKETS, 7)
    )

    ids = [
        record["id"]
        for record in selected
    ]

    assert ids == [
        "T403",
        "T405",
    ]


def test_display_view_minimum_seven():

    _, display_view, _ = (
        build_views(TICKETS, 7)
    )

    ids = [
        record["id"]
        for record in display_view
    ]

    assert ids == [
        "T403",
        "T405",
    ]


def test_search_view_order():

    _, _, search_view = (
        build_views(TICKETS, 4)
    )

    ids = [
        record["id"]
        for record in search_view
    ]

    assert ids == [
        "T402",
        "T403",
        "T405",
        "T406",
    ]


def test_completed_ticket_excluded():

    selected, _, _ = build_views(
        TICKETS,
        0
    )

    ids = [
        record["id"]
        for record in selected
    ]

    assert "T404" not in ids


def test_empty_selection():

    selected, display_view, search_view = (
        build_views(TICKETS, 8)
    )

    assert selected == []
    assert display_view == []
    assert search_view == []


def test_linear_search_found():

    selected, _, _ = (
        build_views(TICKETS, 4)
    )

    position, trace = linear_search(
        selected,
        "T403"
    )

    assert position == 0
    assert len(trace) > 0


def test_linear_search_missing():

    selected, _, _ = (
        build_views(TICKETS, 4)
    )

    position, trace = linear_search(
        selected,
        "T499"
    )

    assert position is None


def test_binary_search_found():

    _, _, search_view = (
        build_views(TICKETS, 4)
    )

    position, trace = binary_search(
        search_view,
        "T403"
    )

    assert position is not None
    assert len(trace) > 0


def test_binary_search_missing():

    _, _, search_view = (
        build_views(TICKETS, 4)
    )

    position, trace = binary_search(
        search_view,
        "T499"
    )

    assert position is None


def test_empty_searches():

    position, trace = linear_search(
        [],
        "T403"
    )

    assert position is None
    assert trace == []

    position, trace = binary_search(
        [],
        "T403"
    )

    assert position is None
    assert trace == []


def test_t403_view_positions():

    selected, _, search_view = (
        build_views(TICKETS, 4)
    )

    linear_position, _ = linear_search(
        selected,
        "T403"
    )

    binary_position, _ = binary_search(
        search_view,
        "T403"
    )

    assert linear_position == 0
    assert binary_position == 1


if __name__ == "__main__":

    test_insertion_sort_empty()
    test_insertion_sort_singleton()
    test_insertion_sort_order()
    test_stability()
    test_sorted_input()
    test_reverse_input()
    test_input_not_modified()
    test_shared_record_identity()
    test_build_views_minimum_four()
    test_build_views_minimum_seven()
    test_display_view_minimum_seven()
    test_search_view_order()
    test_completed_ticket_excluded()
    test_empty_selection()
    test_linear_search_found()
    test_linear_search_missing()
    test_binary_search_found()
    test_binary_search_missing()
    test_empty_searches()
    test_t403_view_positions()

    print("All tests passed.")