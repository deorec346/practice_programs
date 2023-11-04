def finalValueAfterOperations(operations) -> int:
    test = 0  # Initialize the test variable to 0

    # Iterate through each operation in the list
    for i in operations:
        if i == "--X":
            test = test - 1  # Decrement by 1 if operation is "--X"
        elif i == "X++" or i == "++X":
            test = test + 1  # Increment by 1 if operation is "X++" or "++X"
        elif i == "X--":
            test = test - 1  # Decrement by 1 if operation is "X--"

    return test  # Print the final value after all operations


""" this is optimized code

# def finalValueAfterOperations(self, operations: List[str]) -> int:
#     test = 0
#     for i in operations:
#         if i=="++X" or i=="X++":
#             test+=1
#         else:
#             test-=1   
#     return test

"""

operations = ["X++","++X","--X","X--"]
finalValueAfterOperations(operations)