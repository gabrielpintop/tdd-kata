class Calculator:
    def add(self, string):
        if string == "":
            return 0
        elif "," in string:
            return int(string[0]) + int(string[2])
        else:
            return int(string)
