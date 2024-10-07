def interpret(filename):
    file = open(filename)
    s = dict()

    for line in file.readlines():
        if line.startswith("let "):
            definition = line.split("let ")[1]
            var, val = definition.split("=")
            s[var] = decidevalue(line, s)
        elif line.startswith("print("):
            print_text = line.split("print")[1].replace("(","").replace(")","").replace("\n","")
            if "\"" in print_text:
                print_text = print_text.replace("\"","")
                print(print_text)
            #maybe put into it's own function etc.
            elif "+" in line:
                definition = print_text.split("+")
                var1 = definition[0].replace(" ","")
                var2 = definition[1].replace(" ","")
                try:
                    num1 = int(s[var1])
                    num2 = int(s[var2])
                    val = num1 + num2
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")
            elif "-" in line:
                definition = print_text.split("-")
                var1 = definition[0].replace(" ","")
                var2 = definition[1].replace(" ","")
                try:
                    num1 = int(s[var1])
                    num2 = int(s[var2])
                    val = num1 - num2
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")
            elif "*" in line:
                definition = print_text.split("*")
                var1 = definition[0].replace(" ","")
                var2 = definition[1].replace(" ","")
                try:
                    num1 = int(s[var1])
                    num2 = int(s[var2])
                    val = num1 * num2
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")
            elif "/" in line:
                definition = print_text.split("/")
                var1 = definition[0].replace(" ","")
                var2 = definition[1].replace(" ","")
                try:
                    num1 = int(s[var1])
                    num2 = int(s[var2])
                    val = num1 / num2
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")
            elif "%" in line:
                definition = print_text.split("%")
                var1 = definition[0].replace(" ","")
                var2 = definition[1].replace(" ","")
                try:
                    num1 = int(s[var1])
                    num2 = int(s[var2])
                    val = num1 % num2
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")
            else:
                variable_name = print_text
                try:
                    val = s[variable_name]
                    print(val)
                except KeyError:
                    print("Variable(s) not defined")

def decidevalue(line, s):
    if "+" in line:
        definition = line.split("=")[1]
        nums = definition.split("+")
        if len(nums) == 2:
            num1 = nums[0].strip()
            num2 = nums[1].strip()
            #Calls addition function and stores result
            result = addition(num1, num2, s)
            var_name = line.split("=")[0].replace("let ","").strip()
            s[var_name] = result
        return s[var_name]
    elif "-" in line:
        definition = line.split("=")[1]
        nums = definition.split("-")
        if len(nums) == 2:
            num1 = nums[0].strip()
            num2 = nums[1].strip()
            #Calls subtraction function and stores result
            result = subtraction(num1, num2, s)
            var_name = line.split("=")[0].replace("let ","").strip()
            s[var_name] = result    
        return s[var_name]
    elif "*" in line:
        definition = line.split("=")[1]
        nums = definition.split("*")
        if len(nums) == 2:
            num1 = nums[0].strip()
            num2 = nums[1].strip()
            #Calls multiply function and stores result
            result = multiply(num1, num2, s)
            var_name = line.split("=")[0].replace("let ","").strip()
            s[var_name] = result
        return s[var_name]
    elif "/" in line:
        definition = line.split("=")[1]
        nums = definition.split("/")
        if len(nums) == 2:
            num1 = nums[0].strip()
            num2 = nums[1].strip()
            #Calls divide function and stores result
            result = divide(num1, num2, s)
            var_name = line.split("=")[0].replace("let ","").strip()
            s[var_name] = result
        return s[var_name]
    elif "%" in line:
        definition = line.split("=")[1]
        nums = definition.split("%")
        if len(nums) == 2:
            num1 = nums[0].strip()
            num2 = nums[1].strip()
            #Calls modulo function and stores result
            result = modulo(num1, num2, s)
            var_name = line.split("=")[0].replace("let ","").strip()
            s[var_name] = result
        return s[var_name]
    else:
        definition = line.split("let ")[1]
        var, val = definition.split("=")
        var = var.replace(" ","").replace("\n","")
        val = val.replace(" ","").replace("\n","")
        s[var] = val
    return s[var]

#Handles multiplication computation
def multiply(var1, var2, s):
    #Gets value from dictionary s
    val1 = s.get(var1, var1)
    val2 = s.get(var2, var2)
    try:
        #Attempts to change val1 and val2 from a str to float if there is a . otherwise it will change them to int
        val1 = float(val1) if "." in str(val1) else int(val1)
        val2 = float(val2) if "." in str(val2) else int(val2)
    except ValueError:
        print("Error")
    return (val1 * val2)

#Handles division computation
def divide(var1, var2, s):
    #Gets value from dictionary s
    val1 = s.get(var1, var1)
    val2 = s.get(var2, var2)
    try:
        #Attempts to change val1 and val2 from a str to float if there is a . otherwise it will change them to int
        val1 = float(val1) if "." in str(val1) else int(val1)
        val2 = float(val2) if "." in str(val2) else int(val2)
        return (val1 / val2)
    except ValueError:
        print("Error")

#Handles addition computation
def addition(var1, var2, s):
    #Gets value from dictionary s
    val1 = s.get(var1, var1)
    val2 = s.get(var2, var2)
    try:
        #Attempts to change val1 and val2 from a str to float if there is a . otherwise it will change them to int
        val1 = float(val1) if "." in str(val1) else int(val1)
        val2 = float(val2) if "." in str(val2) else int(val2)
    except ValueError:
        print("Error")
    return (val1 + val2)

#Handles subtraction computation
def subtraction(var1, var2, s):
    #Gets value from dictionary s
    val1 = s.get(var1, var1)
    val2 = s.get(var2, var2)
    try:
        #Attempts to change val1 and val2 from a str to float if there is a . otherwise it will change them to int
        val1 = float(val1) if "." in str(val1) else int(val1)
        val2 = float(val2) if "." in str(val2) else int(val2)
    except ValueError:
        print("Error")
    return (val1 - val2)

#Handles modulo computation
def modulo(var1, var2, s):
    #Gets value from dictionary s
    val1 = s.get(var1, var1)
    val2 = s.get(var2, var2)
    try:
        #Attempts to change val1 and val2 from a str to float if there is a . otherwise it will change them to int
        val1 = float(val1) if "." in str(val1) else int(val1)
        val2 = float(val2) if "." in str(val2) else int(val2)
    except ValueError:
        print("Error")
    return (val1 % val2)

interpret("2.fun")