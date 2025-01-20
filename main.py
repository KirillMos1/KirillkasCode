vars = {}

def compiler(path):
    try:
        file_opened = open(path, "r")
        for line in file_opened.read().split("\n"):
            if line.startswith("#"):
                continue
            else:
                line_list = line.split("|")
                func = line_list[0]
                args = line_list[1].split("_")
                if func == "print":
                    printer(args)
                elif func == "setvar":
                    setvar(args[0], args[1])
                elif func == "getvar":
                    getvar(args[0])
                elif func == "delvar":
                    delvar(args[0])
                elif func == "info":
                    info()
                elif func == "exit":
                    raise SystemExit(0)
                elif func == "math":
                    math_func(args[0])
                elif func == "math_vars":
                    math_vars(args[0], args[1], args[2])
                elif func == "input":
                    if len(args) == 2:
                        inputing(args[0], args[1])
                    else:
                        inputing(args[0])
                elif func == "equals_vars":
                    equals_to_vars(args[0], args[1])
                elif func == "":
                    continue
                else:
                    printer(["I can`t do this!"])
    except FileNotFoundError:
        printer(["Error. Prosess: main/compiler: Description: file not found!"])
    except Exception as e:
        printer([f"Error. Prosess: main/compiler. {e}"])
            


def printer(args: list):
    try:
        returned = ""
        for arg in args:
            returned += arg + " "
        print(returned)
    except Exception as e:
        print([f"Error. Prosess: main/print. Description - {e}"])

def setvar(name: str, value: any):
    global vars
    try:
        if " " in name or name == "":
            printer(["Error. Prosess: main/setvar. Description: the name can`t be empty or contain a space"])
        else:
            vars[name] = value
    except:
        printer(["Error. Prosess: main/setvar"])

def getvar(name: str):
    global vars
    try:
        if name in vars.keys():
            printer([vars[name]])
        else:
            printer(["Error. Prosess: main/getvar. Description: var not found"])
    except:
        printer(["Error. Prosess: main/getvar"])

def delvar(name: str):
    global vars
    try:
        if name in vars.keys():
            del vars[name]
        else:
            printer(["Error. Prosess: main/delvar. Description: var not found"])
    except:
        printer(["Error. Prosess: main/delvar"])

def info():
    printer(["Commands of KKC: \ncompiler <path> - run compile on file <path>\ninfo - this message \nprint <arg1> <arg2> <arg_n> - print a args \nsetvar <name> <value> - create a var with name <name> and value <value> \ngetvar <name> - print a var <name> \ndelvar <name> - delete var <name> \nexit - exit from KKC \nmath <exp> - complete expression <exp> \nmath_vars <var1> <var2> <symbol> - math operation <symbol> with <var1> and <var2> \nequals_vars <var1> <var2> - equaling of vars (true / false)"])

def math_func(exp):
    try:
        printer([str(eval(exp))])
    except:
        printer(["Error. Prosess: main/math_func"])

def math_vars(var1, var2, symbol):
    try:
        returned = str(vars[var1]) + str(symbol) + str(vars[var2])
        printer([eval(returned)])
    except:
        printer(["Error. Prosess: main/math_vars"])

def inputing(text, var_save = "input_result"):
    try:
        vars[var_save] = input(f"({text})>> ")
    except:
        printer(["Error. Prosess: main/input"])

def equals_to_vars(var1, var2):
    try:
        if vars[var1] == vars[var2]:
            printer(["True"])
        else:
            printer(["False"])
    except:
        printer(["Error. Prosess: main/equals_vars"])

print("KirillkasCode v.0.1.0_alpha for x64")
while True:
    com = input(">> ")
    if com == "compile":
        path = input("path (replace \\ to \\\\)>> ")
        compiler(path)
    elif com == "print":
        args = []
        arg = "n"
        while arg != "":
            arg = input("arg>> ")
            args.append(arg)
        printer(args)
    elif com == "setvar":
        name = input("name>> ")
        val = input("val>> ")
        setvar(name, val)
    elif com == "getvar":
        name = input("name>> ")
        getvar(name)
    elif com == "delvar":
        name = input("name>> ")
        delvar(name)
    elif com == "info":
        info()
    elif com == "exit":
        raise SystemExit(0)
    elif com == "math":
        for_eval = input("expression>> ")
        math_func(for_eval)
    elif com == "math_vars":
        var1 = input("var1>> ")
        var2 = input("var2>> ")
        symbol = input("symbol>> ")
        math_vars(var1, var2, symbol)
    elif com == "input":
        text = input("text>> ")
        var_save = input("var (if you want save result in standart var, press enter)>> ")
        if var_save != "":
            inputing(text, var_save)
        else:
            inputing(text)
    elif com == "equals_vars":
        var1 = input("var1>> ")
        var2 = input("var2>> ")
        equals_to_vars(var1, var2)
    elif com == "":
        continue
    else:
        printer(["I can`t do this!"])
