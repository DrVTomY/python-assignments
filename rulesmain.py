from xml.dom import minidom




class Employee:
    employee_no = 1
    mydoc = minidom.parse('rules.xml')

    condition = mydoc.getElementsByTagName('condition')
    condition1 = condition[0].firstChild.data
    condition2 = condition[1].firstChild.data

    action = mydoc.getElementsByTagName('action')
    action1 = action[0].firstChild.data
    action2 = action[1].firstChild.data

    def __init__(self, name, age, tenure):
        self.status = "temporary"
        self.name = name
        self.age = age
        self.tenure = tenure
        self.id = Employee.employee_no
        Employee.employee_no += 1
        self.rule_1(Employee.condition1, Employee.action1)
        self.rule_2(Employee.condition2, Employee.action2)
        self.display()



    def rule_1(self, condition1, action1):
        if eval(condition1):
            self.status = action1
        else:
            self.status

    def rule_2(self, condition2, action2):
        if eval(condition2):
            self.status = action2
        else:
            self.status

    def display(self,):
        print("\n personal Details=", self.name, self.age, self.status)


def main():


    a = Employee('ramesh', 30, 11)
    b = Employee('suresh', 40, 21)
    c = Employee('paresh', 50, 31)
    d = Employee('sohan', 62, 40)
    e = Employee('kalpesh', 70, 40)
    f = Employee('mohan', 20, 1)


main()
