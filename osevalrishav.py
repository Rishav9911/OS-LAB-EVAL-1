def mark_present(str,presentlist):
    if str in presentlist:
        print("already present\n")
        return
    
    presentlist.append(str)
    print(" updated student list\n")
    for x in presentlist:
        print(x + " ")
    print("\n")
    return
    
def remove_student(str,presentlist):
    if str not in presentlist:
        prit("already marked absent\n")
        return

    presentlist.remove(str)
    print("student removed\n")
    return


def is_present(str,presentlist):
    
    if str in presentlist:
        return True
    return False


def display_attendance(presentlist):
    print("the list is: ")
    for x in presentlist:
        print(x + " ")

    return
    

presentlist=[]

mark_present("rohit",presentlist)
mark_present("kartik",presentlist)
mark_present("rishav",presentlist)

remove_student("rohit",presentlist)

print(is_present("rishav",presentlist))

display_attendance(presentlist)

sortedlist(presentlist)



