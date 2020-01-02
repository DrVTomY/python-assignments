class employee:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def display(self):
        print('\n\nName = ' + self.name)
        print('Code = ' + str(self.code))
        # return str(self.__dict__)


def main():
    e1 = employee("Nisha", "12321")
    e2 = employee("Ayush", "12322")
    e1.display()
    e2.display()


main()
