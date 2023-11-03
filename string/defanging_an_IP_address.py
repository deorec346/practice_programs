def defangIPaddr( address: str) -> str:

    new_add = ""
    for i in address:
        if i == ".":
            new_add = new_add +  "[.]"
        else:
            new_add +=i 
    return new_add    

address = "1.1.1.1"
defangIPaddr(address)



"""
by using the replace method.
"""
# return address.replace(".","[.]")