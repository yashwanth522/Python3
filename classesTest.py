class Printer:

    __secretvariable = 0

    def __init__(self, msg):
        self.msg = msg

    def printerfunparent(self):
        print("Im in printer function")


class PrinterChild(Printer):

    def __init__(self, msg):
        self.msg = msg

    def printerfun(self):
        print("Im in child printer function")

print_Object = PrinterChild("Hello World!!")
print_Object.printerfun()
print_Object.printerfunparent()
print(print_Object._Printer__secretvariable)
