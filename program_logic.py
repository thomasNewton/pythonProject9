# example of a callback function and calling qt example in the calc.py file
import calc


# this is the method called from main
def run_it():
    calc.make_it()


def callback_func(s):
    print(f"length of the text file is {s}")


def print_file_length(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)


class Person:
    age = 0
    country = 'stateless'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_info(self):
        print(f"age:{self.age} \tName:{self.name}\n")


class Student(Person):
    data_dict = {}

    def __init__(self, age, name, **kwargs):
        super().__init__(age, name)
        self.data_dict = dict(kwargs)

    def print_info(self):
        print("two ways to call super  explicitly and implicitly ")
        super(Student, self).print_info()
        super().print_info()
        print(self.data_dict)  # need self because its out of print_info scope


if __name__ == "__main__":
    print_file_length("main.py", callback_func)
    bob = Person(5, 'bobby')
    print(f"Print bob returns an object reference: {bob}")
    bob.print_info()
    tim = Student(2, "timmy")
    tim.print_info()
    tom = Student(19, "Thomas", grade=12, grad_class=2023, nick_name="Chucky the Ducky")
    tom.print_info()
    print("this is an internal class file.\nRun main.py to use this program")
    exit(42)
