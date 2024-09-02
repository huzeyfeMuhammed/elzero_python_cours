# def say_hello (name, age, country):
#     print (f"Hello {name} Your age is: {age} and your Country is: {country}")
    
# say_hello("Huzeyfe", 31, "Syria")
# say_hello("Ali", 25, "Egypt")


def say_hello (name, age="Unknown", country="Unknown"): 
    print (f"Hello {name}. Your age is: {age} and your country is: {country}")
    
say_hello("Huzeyfe", 31, "Syria")
say_hello("Ali", 25, "Egypt") 
say_hello("Semih", 18 ) 