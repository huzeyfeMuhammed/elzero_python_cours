# print (1, 2, 3, 4)
# numbers = [1, 2, 3, 4]
# print (numbers)
# print (*numbers)


# def say_hello (*peoples):

#     for name in peoples:
#         print (f"Hello {name}")
        
# say_hello ("ali", "huzeyfe", "Seyit", "Mahmut")
# print ("#" * 30)
# say_hello ("wael", "cemil", "halit", "salah", "cuma", "huzeyfe")

# def show_deltails (skill_1, skill_2, skill_3,):
    
#     print (f"Hello Huzeyfe. Your Skilles is:")
    
#     print (f"- {skill_1}")
#     print (f"- {skill_2}")
#     print (f"- {skill_3}")

# show_deltails ("Html", "CSS", "JS")


# def show_deltails (*skills):
    
#     print (f"Hello Huzeyfe. Your Skilles is:")
#     for skill in skills:
        
#         print (f"- {skill}")

# show_deltails ("Html", "CSS", "JS", "Python")

 
def show_deltails (name, *skills):
    
    print (f"Hello {name}. Your Skilles is:")
    for skill in skills:
        
        print (f"- {skill}")

show_deltails (" Ali", "Html", "CSS")
show_deltails (" Huzeyfe", "Html", "CSS", "JS", "Python")
