from sys import *


vars = {}


def open_file(filename):
    data = open(filename, "r").read()
    data = data.replace("\n", "")
    data = data.split(";")
    data = data[:-1]
    return data

def parse(filecontents):
    for i in filecontents:
        if i[0:5] == "print":
            text = i.replace("print", "")
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
            try:
                print(text[quotes[0]+1:quotes[1]])
            except IndexError:
                print(vars[len(text)-len(text.lstrip()):])

        elif i[0:3] == "var":
            var = i.replace("var", "")
            varType = "str"

            try:
                firstquote = var.index("\"")
            except ValueError:
                varType = "int"
            
            equals = var.index("=")
            varname = var[:equals].replace(" ", "")

            if varType == "str":
                varvalue = var[firstquote+1:-1]
                vars[varname] = varvalue
            elif varType == "int":
                varvalue = var[equals+1:].replace(" ", "")
                vars[varname] = int(varvalue)

            varType = "str"
            print(vars)


def run():
    data = open_file(input("File to execute: "))
    parse(data)

run()