def interpret(filename):
    file = open(filename)
    s = dict()
    counter = 1

    for line in file.readlines():
        line = line.replace("\n","")
        if line.startswith("let "):
            definition = line.split("let ")[1].replace(" ","")
            var, val = definition.split("=")
            try:
                s[var] = evalExpression(val, s)
            except:
                print("Error on line: " + str(counter))
                print(line)
                break
        elif line.startswith("print("):
            print_text = line.split("print")[1].replace("(","").replace(")","")
            if "\"" in print_text:
                print_text = print_text.replace("\"","")
                print(print_text)
            else:
                try:
                    print(evalExpression(print_text, s))
                except:
                    print("Not a value")
        counter += 1


#takes in an expression and returns the value of the
def evalExpression(val, s):
    if "+" in val:
        return parseString(val, "+", s)
    elif "-" in val:
        return parseString(val, "-", s)
    elif "*" in val:
        return parseString(val, "*", s)
    elif "/" in val:
        return parseString(val, "/", s)
    elif "%" in val:
        return parseString(val, "%", s)
    else:
        return checkValue(val, s)


def parseString(definition, operand, s):
    nums = definition.split(operand)
    if len(nums) == 2:
        num1 = nums[0].strip()
        num2 = nums[1].strip()
        return doMath(num1, num2, operand, s)
        

def checkValue(var, s):
    var = s[var] if var in s else var
    
    if var == "True":
        return True
    elif var == "False":
        return False
    else:
        return float(var) if "." in str(var) else int(var)

def doMath(var1, var2, operand, s):

    val1 = checkValue(var1, s)
    val2 = checkValue(var2, s)

    match operand:
        case "+":
            return (val1 + val2)
        case "-":
            return (val1 - val2)
        case "*":
            return (val1 * val2)
        case "/":
            return (val1 / val2)
        case "%":
            return (val1 % val2)
    raise ValueError

interpret("2.fun")