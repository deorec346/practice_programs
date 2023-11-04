def interpret(command):
    # command = command.replace("()","o").replace("(al)","al") 
    # with python bydefault function

    """
    without function and by using loop 
    """
    test = ""
    i = 0
    while i < len(command):
        if command[i] == "G":
            test = test + "G"
            i=i+1
        elif command[i:i+2] == "()":
            test = test + "o"
            i = i + 2
        elif command[i:i+4] == "(al)":
            test = test + "al"
            i = i + 4
        else:
            i=i+1
    print(test)
    print(command)
command = "G()(al)"    
interpret(command)