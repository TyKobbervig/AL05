# AL05 - Sorting, Searching, and Pipelines

## Student

Ty Kobbervig

## Pipeline

Source Records -> Open Ticket Filter -> Display View (Days Open Order) -> Search View (ID Order) -> Lookup

The program starts with the original ticket list. Open tickets meeting the minimum age requirement are selected, then separate display and search views are created. Searches are performed using the appropriate view.

## Stability Observation

Insertion sort is stable because records with equal days_open values keep their original relative order. For example, T403 remains before T405 when both tickets have 7 days open.

## Changed and Preserved Behavior

When the minimum_days requirement changed from 4 to 7, the views were rebuilt from the original ticket list. The sorting algorithm, searching algorithms, key functions, and comparison logic did not need to be rewritten.

## Workload Comparison

### Single Request

For a single ticket request, the program must:

1. Filter the source records.
2. Build the display view.
3. Build the search view.
4. Perform the search.

### Repeated Requests

For repeated searches on the same ticket selection, the previously built ID-ordered search view can be reused. If the filtering rule changes, the views must be rebuilt from the source records.

## Testing

I tested:

- Empty input
- Singleton input
- Ordered input
- Reverse-order input
- Stable sorting behavior
- Minimum days of 4
- Minimum days of 7
- Empty selection at 8 days
- Completed-ticket exclusion
- Linear search found and missing cases
- Binary search found and missing cases
- Input non-mutation
- Shared record identity
