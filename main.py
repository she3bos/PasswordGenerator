import random

small = "abcdefghigklmnopqrstuvxyz#@$&*!"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#@$&*!"


def include_specialp(Pass):
    special = "#@$&*!"
    include_special = False
    for c in Pass:
        if c in special:
            include_special = True

    return include_special


def generate_password(n):  # n = number of characters , include_special = True or false
    passwd = ""
    for i in range(n):
        choice = random.randint(1, 2)
        if choice == 1:
            passwd = passwd + small[random.randint(0, 30)]
        else:
            passwd = passwd + capital[random.randint(0, 30)]

    return passwd


def get_number_of_characters():
    while True:
        no = int(input("Enter number of character: 8, 12, 16, 20: "))
        if no in [8, 12, 16, 20]:
            return no
        else:
            print("invalid input")


def get_include_special():
    while True:
        message = int(input("include special character?: 1 for yes , 2 for no"))
        if message == 1:
            sc = True
            return sc
        elif message == 2:
            sc = False
            return sc
        else:
            print("invalid input")


n = get_number_of_characters()

sc = get_include_special()

while True:
    password = generate_password(n)
    if sc:
        if include_specialp(password):
            break
        elif not include_specialp(password):
            continue
    elif sc is False:
        if not include_specialp(password):
            break
        elif include_specialp(password):
            continue

print("your password is {}".format(password))
