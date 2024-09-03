a, h, m = " ahmed   ", "huzeyfe  ", "muhammed  "  # تعريف الأسماء

names = [a, h, m]  # إنشاء قائمة بالأسماء

def say_hello(n):  # تعريف الدالة التي تطبع رسالة الترحيب
    print(f"Hello {n}!")

for name in names:  # تكرار لكل اسم في القائمة
    cleaned_name = name.strip().capitalize()  # تنظيف وتنسيق الاسم
    say_hello(cleaned_name)  # طباعة رسالة الترحيب للاسم المنسق

print ("*" * 50)

def addition (n1, n2):
    if type(n1) != int or type(n2) != int:
        print ("Only Integers Allowed")
    else:
        print (int(n1) + int (n2))
    
addition (100,200)


def full_name (first, middle, last):
    
    print (f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}" )

full_name ("huzeyfe", "abdurrahman","muhammed")