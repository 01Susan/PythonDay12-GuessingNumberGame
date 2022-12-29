########## Scope ############

number = 1  # Here number is Global variable


def increase_number():
    # This is the local variable
    # number is the new local varible for this function
    global number
    number += 1
    print(f"number inside the function: {number}")


increase_number()
print(f"number outside the function: {number}")


# --------Local Scope -------------


def my_home():
    area = 100
    print(area)


my_home()
# print(area) -->It gives an name error beacuse
# area variable is only accessible in my_home function


# -----------Global Scope ---------------

land_area = 100


def my_home1():
    area = 101
    print(land_area)


# here land_area is the global variable which can be used outside and inside any function
my_home1()


# There is no Block scope in the python

game_level = 3
enemy = ["Susan", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemy[0]

# here new_enemy is not counted as the local scope new_enemy can be accessible outside the block
# That means block scope is applicable only in Functions
# new_enemy is acting like a global varibale if that if statement was inside the function
# then case would be different new_enemy var would be local varibale
print(new_enemy)


# _______Global Constant-------------

# Constant are varibale that you dont want to change it
# Constant are always represent in the uppecase
# example
PI = 3.14


##


def bar():
    my_variable = 9
    print(my_variable)
    if 16 > 9:
        my_variable = 16
    print(my_variable)


bar()
