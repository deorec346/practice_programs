# Define a function to defang an IP address
def defangIPaddr(address: str) -> str:
    # Create an empty string to store the defanged address
    new_add = ""

    # Iterate through each character in the input address
    for i in address:
        # Check if the character is a dot (".")
        if i == ".":
            # If it's a dot, replace it with "[.]" and add to the new address
            new_add = new_add + "[.]"
        else:
            # If it's not a dot, simply add the character to the new address
            new_add += i

    # Return the defanged IP address
    return new_add    

# Example usage
address = "1.1.1.1"
defanged_address = defangIPaddr(address)
print(defanged_address)



"""
by using the replace method.
"""
# return address.replace(".","[.]")
