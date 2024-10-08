def interpret(filename):
    file = open(filename)
    s = dict()
    inIfStatement = False #Used to detect when beginning if statement
    inElseStatement = False
    ifBlock = [] #Stores block of if statement
    elseBlock = []
    ifOrElse = False
    counter = 1

    for line in file.readlines():
        if line.startswith("if:"):
            condition = line.split(":")[1].strip()
            ifOrElse = evalExpression(condition, s)
            inIfStatement = True
            continue
        
        if inIfStatement:
            if line.startswith("else:"):
                inIfStatement = False
                inElseStatement = True
                continue
            else:
                ifBlock.append(line)
                continue

        if inElseStatement:
            if line.startswith(";"):
                inElseStatement = False
            else:
                elseBlock.append(line)
                continue
        
        if ifOrElse:
            #run ifBlock
            for line in ifBlock:
                line = line.strip()
                evalAction(line, s)
                line = ""
                            
        else:
            #run elseBlock
            for line in elseBlock:
                line = line.strip()
                evalAction(line, s)
                line = ""
                     
        line = line.replace("\n","")
        if not line.strip():
            counter += 1
            continue

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
                print(evalExpression(print_text, s))

        else:
            print("Statement is not defined on line: " + str(counter))
        counter += 1

def doIfStatement(line, s):
    #Get the condition and actions
    condition = line[line.index("if:") + len("if:"):line.index(",")].strip()
    action = line[line.index(",") + 1:line.index(".")].strip()
    elseAction = None

    #Check for else within if statement
    if 'else:' in line:
        elseAction = line[line.index('else:') + len('else:'):line.index(';')].strip()

    #Evaluate the condition
    if evalExpression(condition, s):
        evalAction(action, s)
    elif elseAction:
        evalAction(elseAction, s)

def evalAction(action, s):
    #Execute the action in the same way as the print statement
    if action.startswith("print("):
        print_text = action.split("print")[1].replace("(", "").replace(")", "")
        if "\"" in print_text:
            print_text = print_text.replace("\"", "")
            print(print_text)
        else:
            print(evalExpression(print_text, s))
    else:
        print("Action not recognized: " + action)

#takes in an expression and returns the value
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
    elif "<=" in val:
        return parseString(val, "<=", s)
    elif "<" in val:
        return parseString(val, "<", s)
    elif ">=" in val:
        return parseString(val, ">=", s)
    elif ">" in val:
        return parseString(val, ">", s)
    elif "==" in val:
        return parseString(val, "==", s)
    else:
        try:
            return checkValue(val, s)
        except ValueError:
            return("value not found")

def parseString(definition, operand, s):
    nums = definition.split(operand)
    if len(nums) == 2:
        num1 = nums[0].strip()
        num2 = nums[1].strip()
        #Checks for relational operators
        if operand in ["<=", "<", ">=", ">", "=="]:
            val1 = checkValue(num1, s)
            val2 = checkValue(num2, s)
            match operand:
                case "<=":
                    return (val1 <= val2)
                case "<":
                    return (val1 < val2)
                case ">=":
                    return (val1 >= val2)
                case ">":
                    return (val1 > val2)
                case "==":
                    return (val1 == val2)
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