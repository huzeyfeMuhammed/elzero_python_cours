def show_skills (**skills):
    print (type(skills))
    for skill, value in skills.items():
        print (f"{skill} => {value}")

# show_skills (Html = "80%", CSS= "20%", Python= "30%")

my_skills = {
    "Html" : "80%",
    "CSS": "20%",
    "Python": "30%"
}

my_skills_2 = {
    "JS" : "80%",
    "Java": "20%",
    "C": "10%",
    "C#": "30%"
    
}

show_skills (**my_skills)
show_skills (**my_skills_2)