def main_function(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function

def normal_function():
    print("Normal")

checking = main_function(normal_function)
print(checking)



