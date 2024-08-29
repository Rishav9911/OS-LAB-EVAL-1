
def mark_present(day,str,presentdic):
    for i,obj in presentdic:
        if str in obj:
            print("already present\n")
            return
        
    presentdic[day].append(str)

    for i,obj in presentdic:
        print("for day: ",i)
        for x in obj:
            print(x + " ")

        print("\n")
    return

def remove_student(day,str,presentdic):
    for i,obj in presentdic:
        if str not in obj:
            print("not present\n")
            return
        
    presentdic[day].remove(str)
    print("studnet removed")
    return

def is_present(day,str,presentdic):
     for i,obj in presentdic:
        if str in obj:
            return True
        return False

def display(presentdic):
    for i,obj in presentdic:
        print("for day: ",i)
        for x in obj:
            print(x + " ")

        print("\n")

    return


presentdic={}

n=int(input("enter no of students: "))

for i in range(n):
    str=input("enter student: ")
    day=int(input("enter day: "))
    mark_present(day,str,presentdic)

str2=input("enter student: ")
day2=int(input("enter day: "))
remove_student(day2,str2,presentdic)

str3=input("enter student: ")
day3=int(input("enter day: "))
print(is_present(day2,str2,presentdic))

display(presentdic)



