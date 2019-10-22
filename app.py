def hello():
    print("hello world")


hello()


def say_hello(name):
    print(f"Hi {name}")


say_hello('Bob')
say_hello('John')


def double(number):
    return number * 2


result_1 = double(3)

print(result_1)


# 1分課題
def str_combine(name1, name2):
    return f"{name1}{name2}"


result = str_combine('Kazuma', 'Takahashi')

print(result)
