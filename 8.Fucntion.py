def display(greetings):
    print(greetings)


def square(num):
    return num ** 2


def add(num1, num2):
    return num1 + num2


def let_me_in(age=17):
    if age < 18:
        return "Nope!!"
    else:
        return "Awwwww"


def func_with_param_name(p1, p2):
    print("p1", p1)
    print("p2", p2)


def var_args_func(*args):
    print(len(args))
    for item in range(len(args)):
        print(item)


display("Hello World!")
print(square(3))
print(add(2, 3))
# add(2,3,4) Not allowed
print(let_me_in())
print(let_me_in(23))
print(var_args_func(1, 2, 3, 4))
func_with_param_name(p2=3, p1=6)


func_ref = let_me_in
print(func_ref())



