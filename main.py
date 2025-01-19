vars = {}

def printer(args: list):
    try:
        com_list.remove(0)
        returned = ""
        for arg in args:
            returned += agr + " "
        print(returned)
    except:
        printer("Error. Prosess: main/print")

def setvar(name: str, value: any):
    global vars
    try:
        
        vars[name] = value
    except:
        printer("Error. Prosess: main/setvar")

def getvar(name: str):
    global vars
    try:
        if name in vars.keys():
            printer([vars[name]])
        else:
            printer(["Error. Prosess: main/getvar. Description: var not found"])
    except:
        printer("Error. Prosess: main/getvar")

def delvar(name: str):
    global vars
    try:
        if name in vars.keys():
            del vars[name]
        else:
            printer(["Error. Prosess: main/delvar. Description: var not found"])
    except:
        printer("Error. Prosess: main/delvar")

print("KirillkasCode v.0.0.1_alpha for x64")
while True:
    com = input(">> ")
    com_list = com.split(" ")
    if com_list[0] == "print":
        printer(com_list)
    elif com_list[0] == "setvar":
        com_list.remove(0)
        setvar(com_list[0], com_list[1])
    elif com_list[0] == "getvar":
        com_list.remove(0)
        getvar(com_list[0])
    elif com_list[0] == "delvar":
        com_list.remove(0)
        delvar(com_list[0])
    else:
        print("I can`t do this!")
