"""Function examples."""


# func()
def func():
    print("I´m inside the function")

# my_name_is(name)
def my_name_is(name):
    print ("My name is " + name)
    
# sum_six(num)`
def sum_six(num):
    return 6 + num

# sum_numbers()
def sum_numbers(a, b):
    return a + b

# usd_to_eur()
def usd_to_eur(num):
    return (num * 0.8)

print(func())
my_name_is("Mari")
print(sum_six(6))
print (sum_numbers(1, 2))
print (usd_to_eur(100))