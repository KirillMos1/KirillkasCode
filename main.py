vars = {}

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
    printer(["Commands of KKC: \ninfo - this message \nprint <arg1> <arg2> <arg_n> - print a args \nsetvar <name> <value> - create a var with name <name> and value <value> \ngetvar <name> - print a var <name> \ndelvar <name> - delete var <name> \nexit - exit from KKC \nmath <exp> - complete expression <exp>"])

def math_func(exp):
    try:
        printer([str(eval(exp))])
    except:
        printer(["Error. Prosess: main/math_func"])

print("KirillkasCode v.0.0.2_alpha for x64")
while True:
    com = input(">> ")
    if com == "print":
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
    else:
        printer(["I can`t do this!"])
