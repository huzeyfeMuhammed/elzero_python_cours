
my_tuble = ("Python", "Java", "c#")

my_skills = {
    "Html" : "80%",
    "CSS": "20%",
    "Python": "30%"
}

def show_skills (name, *skills, **Skills_with_progress):
    print (f"Hello {name}. \nSkills without progress is: ")
    
    for skill in skills:
        print (f"- {skill} ")
    
    print ("Skills with progress is: ")
    
    for skill_key, skill_value in Skills_with_progress.items():
        print (f"- {skill_key} => {skill_value}")

    
# show_skills("Huzeyfe", "Python", "Java", "c#")



show_skills ("Huzeyfe", *my_tuble, **my_skills)