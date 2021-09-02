import sys


class args:
    totalArguments = ""
    expectedArguments = None
    receivedArguments = None
    pythonScript_CLI = ""

    def __self__(self):
        # check the identified script name
        self.pythonScript_CLI = sys.argv[0]
        self.totalArguments = len(sys.argv)
        self.receivedArguments = sys.argv

    def getAllArguments(self):
        self.receivedArguments = sys.argv

    def printAllArguments(self):
        for i in range(1, len(self.receivedArguments)):
            print(f"Argument[{i}] {self.receivedArguments[i]}")
