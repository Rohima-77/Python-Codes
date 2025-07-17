class GrandFather:
    def __init__(self, colour, first_name):
        self.colour = colour
        self.first_name = first_name

class Father(GrandFather):  
    def __init__(self, hobby, colour, first_name):
        super().__init__(colour, first_name)
        self.hobby = hobby

gf = GrandFather("red", "Khan")
fd = Father("cricket", "red", "Khan")

print(fd.colour)
print(gf.colour)
