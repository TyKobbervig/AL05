"""
AL05 - Sorting, Searching, and Pipelines
"""

from ticket_data import TICKETS
from Al05.search_support import (
    id_key,
    days_key,
)

from pipeline_support import select_open_tickets


from search_algorithms import (
    linear_search,
    binary_search,
)


def insertion_sort(records, key):
    """
    Return (ordered, comparisons, moves, trace).

    ordered is a new list sorted ascending under key.
    comparisons counts key comparisons in the shifting loop.
    moves counts right-shifts only.
    trace contains ticket ID order after each insertion.
    """

    ordered = list(records)

    comparisons = 0
    moves = 0
    trace = []

    for index in range(1, len(ordered)):
        current = ordered[index]

        position = index - 1

        while position >= 0:
            comparisons += 1

            if key(ordered[position]) > key(current):
                ordered[position + 1] = ordered[position]
                moves += 1
                position -= 1
            else:
                break

        ordered[position + 1] = current

        trace.append(
            [record["id"] for record in ordered]
        )

    return (
        ordered,
        comparisons,
        moves,
        trace,
    )


def build_views(records, minimum_days=4):
    """
    Return (selected, display_view, search_view).

    selected:
        Open tickets meeting the minimum age requirement.

    display_view:
        Tickets ordered by days_open.

    search_view:
        Tickets ordered by ID.
    """

    selected = select_open_tickets(
        records,
        minimum_days
    )

    display_view, _, _, _ = insertion_sort(
        selected,
        days_key
    )

    search_view = sorted(
        selected,
        key=id_key
    )

    return (
        selected,
        display_view,
        search_view,
    )


def display_ids(label, records):
    """Display ticket IDs."""

    ids = [record["id"] for record in records]
    print(label, ids)


def main():

    print("\n=== MINIMUM DAYS = 4 ===")

    selected, display_view, search_view = build_views(
        TICKETS,
        4
    )

    display_ids("Selected:", selected)
    display_ids("Display View:", display_view)
    display_ids("Search View:", search_view)

    print("\n=== INSERTION SORT TRACE ===")

    ordered, comparisons, moves, trace = (
        insertion_sort(
            selected,
            days_key
        )
    )

    print("Comparisons:", comparisons)
    print("Moves:", moves)

    for step in trace:
        print(step)

    print("\n=== LINEAR SEARCH FOR T403 ===")

    position, trace = linear_search(
        selected,
        "T403"
    )

    print("Position:", position)

    if position is not None:
        print(
            "Found Ticket:",
            selected[position]["id"]
        )

    print("Trace:", trace)

    print("\n=== BINARY SEARCH FOR T403 ===")

    position, trace = binary_search(
        search_view,
        "T403"
    )

    print("Position:", position)

    if position is not None:
        print(
            "Found Ticket:",
            search_view[position]["id"]
        )

    print("Trace:", trace)

    print("\n=== SEARCH FOR T499 ===")

    position, trace = binary_search(
        search_view,
        "T499"
    )

    if position is None:
        print("Ticket T499 not found.")

    print("Trace:", trace)

    print("\n=== EMPTY SELECTION ===")

    selected, display_view, search_view = build_views(
        TICKETS,
        8
    )

    if not selected:
        print(
            "No tickets qualify when minimum_days = 8."
        )

    print("\n=== INVALID BINARY SEARCH ===")

    selected, display_view, search_view = build_views(
        TICKETS,
        4
    )

    position, trace = binary_search(
        display_view,
        "T406"
    )

    print("Position:", position)
    print("Trace:", trace)

    print(
        "This is deliberate invalid use. "
        "Binary search requires an ID-ordered view, "
        "but display_view is ordered by days_open."
    )

    print("\n=== RULE CHANGE TO 7 DAYS ===")

    selected, display_view, search_view = build_views(
        TICKETS,
        7
    )

    display_ids(
        "Selected:",
        selected
    )

    display_ids(
        "Display View:",
        display_view
    )

    display_ids(
        "Search View:",
        search_view
    )


if __name__ == "__main__":
    main()