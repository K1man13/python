def sort_by_key(list_of_dicts, key):
    """
    Sorts a list of dictionaries based on a specified key.
    
    :param list_of_dicts: List of dictionaries to sort
    :param key: Key on which to sort the dictionaries
    :return: A new list of dictionaries sorted by the specified key
    """
    return sorted(list_of_dicts, key=lambda x: x[key])

# Driver code
if __name__ == "__main__":
    # Example list of dictionaries
    data = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"},
        {"name": "Charlie", "age": 22, "city": "Chicago"}
    ]
    
    # Sort by 'age'
    sorted_by_age = sort_by_key(data, "age")
    print("Sorted by age:")
    for entry in sorted_by_age:
        print(entry)
    
    # Sort by 'name'
    sorted_by_name = sort_by_key(data, "name")
    print("\nSorted by name:")
    for entry in sorted_by_name:
        print(entry)
