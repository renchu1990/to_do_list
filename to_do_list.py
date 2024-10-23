to_do_list = []
def Addlist():
    limit = int(input("enter the limit:"))
    for i in range(limit):
       task = input("enter a new task:")
       to_do_list.append(task)
       print(f"{task} added sucessfully")
def Displaylist():
    print("to_do_list")
    if not  to_do_list:
        print("sorry! your list is empty")
    else:
        print("to_do_list")
        for index , item in enumerate(to_do_list,start=1):
            print(f"{index} - {item}")
def Removelist():
    if not to_do_list:
        return
    try:
        index = int(input("enter the index_value:"))
        if 0 <= index < len(to_do_list):
            remove=to_do_list.pop(index)
            print(f"{remove} item removed successfully")
        else:
            print("invalid index")
    except ValueError:
        print("invalid number:")
def updatelist():
    index=int(input("enter the index value:"))
    if 0 <= index < len(to_do_list):
        value = input("enter the new task:")
        to_do_list[index] = value
        print(f"{value} to_do_list updated")
    else:
        print("invalid index_number:")

while True:
    print("*****To_Do_List******")

    print("1.add to list")

    print("2.display to list")

    print("3.remove list")

    print("4.update")

    print("5.exit")

    option = input("enter the option:")

    if option == '1':

        Addlist()

    elif option == '2':

      Displaylist()


    elif option == '3':

        Removelist()

    elif option == '4':

        updatelist()

    elif option == '5':

        print("program exit Successfully")


