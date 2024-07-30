from collections import Counter


def parse_custom_set(input_list):
    # Convert a list of sets into a list of sorted tuples
    return [tuple(sorted(s)) for s in input_list]


def compare_sets(set1, set_gold):
    # Parse the custom sets
    set1_converted = parse_custom_set(set1)
    set_gold_converted = parse_custom_set(set_gold)

    # Count the occurrences of each set in set1
    set1_counter = Counter(set1_converted)

    # Convert list to set for comparison
    set1_converted_set = set(set1_converted)
    set_gold_converted_set = set(set_gold_converted)

    # Compute the intersection
    intersection = set1_converted_set.intersection(set_gold_converted_set)

    # Find errors (in set1 but not in set_gold)
    errors = set1_converted_set.difference(set_gold_converted_set)

    # Find missing (in set_gold but not in set1)
    missing = set_gold_converted_set.difference(set1_converted_set)

    # Print the intersection
    print("Intersection:")
    for s in intersection:
        print(s)

    # Print errors
    if errors:
        print("\nErrors:")
        for error in errors:
            print(error)
    else:
        print("\nNo Errors")

    # Print missing
    if missing:
        print("\nMissing:")
        for miss in missing:
            print(miss)
    else:
        print("\nNo Missing")

    # Print duplicates
    duplicates = [item for item, count in set1_counter.items() if count > 1]
    if duplicates:
        print("\nDuplicates in set1:")
        for duplicate in duplicates:
            print(f"{duplicate} - {set1_counter[duplicate]} times")
    else:
        print("\nNo Duplicates in set1")


# Example usage:
set1 = [{"something"}]

set_gold = [{"something"}]

compare_sets(set1, set_gold)
