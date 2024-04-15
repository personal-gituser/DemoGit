# Sample data
data = [
    {"name": "Alice", "age": 29},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 40}
]

# Initialize an empty list to store the results
output = []

# Test each item in the data
for item in data:
    # Test case: Check if age is greater than or equal to 30
    test_passed = item["age"] >= 30
    
    # Determine test result
    if test_passed:
        result = "Pass"
    else:
        result = "Fail"
    
    # Create a dictionary representing the item with its test result
    item_result = {"name": item["name"], "age": item["age"], "test_result": result}
    
    # Append the item's result to the output list
    output.append(item_result)
print(output)
# Output the list of dictionarie
