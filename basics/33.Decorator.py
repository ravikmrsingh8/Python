# decorator wraps a function to modify its behaviour

def func_needs_decorator():
    print("This function needs a decorator")


def new_decorator(func):
    def wrap_function():
        print("Some Code befor executing function")
        func()
        print("Some code after executing function")

    return wrap_function

func_needs_decorator()
print()

print("After Decorating this function")
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

print(func_needs_decorator)



print()
@new_decorator
def func_with_decorator():
    print("I am decorated with new_decorarator")

func_with_decorator()
print(func_with_decorator)


