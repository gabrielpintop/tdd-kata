class Calculator:
    def add(self, string):
        if string == "":
            return 0
        elif "," in string or "&" in string or ":" in string:
            string = string.replace("&", ",")
            string = string.replace(":", ",")
            numbers = string.split(",")
            sum = 0
            for num in numbers:
                sum = sum + int(num)
            return sum
        else:
            return int(string)
