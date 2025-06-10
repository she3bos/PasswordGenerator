import random
import string

small = "abcdefghigklmnopqrstuvxyz#@$&*!"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#@$&*!"
special = "#@$&*!"

def include_specialp(Pass):
    include_special = False
    for c in Pass:
        if c in special:
            include_special = True

    return include_special


def generate_password(n):  # n = number of characters ,
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
            print("invalid input")\


def count_special_characters(Password):
    count = 0
    for c in Password:
        if c in special:
            count +=1   
    return count     



def strong(Pass):
    if count_special_characters(Pass) > 4:
        return True
    else:
        return False
        


def combine_input(name, age , year):
    string = name + str(age) + str(year)   #combine the input of the user in one string
    password = generate_final_password() # generate random password
    print(password)
    password_list = list(password)
    num_of_replacments = min(len(password)//2, len(string))
    
    for _ in range(num_of_replacments):
        
        i = random.randint(0,len(password)-1)
        j = random.randint(0,len(string)-1)
        
        password_list[i] = string[j]
    
    return ''.join(password_list)        
        
        
        
    
    
     
        




def generate_final_password():
    
    n = get_number_of_characters()

    sc = get_include_special()
    while True:
        password = generate_password(n)
        if sc:
            if include_specialp(password):
                if strong(password):
                 break
            elif not include_specialp(password):
                continue
        elif sc is False:
            if not include_specialp(password):
                break
            elif include_specialp(password):
                continue
    
    return password       

final_password = combine_input("shawkot","20","2004")

 

#final_password = generate_final_password()
print("your password is {}".format(final_password))

