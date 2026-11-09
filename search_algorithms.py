from search_support import (
    id_key,
    compare_values,
)


def linear_search(records, target, key=id_key):
    """
    Search records sequentially and return
    (position, trace).
    """

    if len(records) == 0:
        return (None, [])

    trace = []

    for position, record in enumerate(records):

        selected_value = key(record)

        trace.append(
            (
                position,
                selected_value
            )
        )

        if compare_values(
            selected_value,
            target
        ) == 0:

            return (
                position,
                trace
            )

    return (
        None,
        trace
    )


def binary_search(records, target, key=id_key):
    """
    Search a sorted record list and return
    (position, trace).
    """

    if len(records) == 0:
        return (None, [])

    low = 0
    high = len(records) - 1

    trace = []

    while low <= high:

        middle = (low + high) // 2

        selected_value = key(
            records[middle]
        )

        trace.append(
            (
                low,
                high,
                middle,
                selected_value
            )
        )

        comparison = compare_values(
            selected_value,
            target
        )

        if comparison == 0:

            return (
                middle,
                trace
            )

        if comparison < 0:
            low = middle + 1
        else:
            high = middle - 1

    return (
        None,
        trace
    )