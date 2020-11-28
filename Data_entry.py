global o
for i in range(1):
    o={}
def new_Mem (Name):
    i=str(Name["Name"])
    o[i]=Name.copy()
    
    return Name


while 1 :
    print('''                              *******************************************************
                             |        To Add New Empolyee Press  1                  |
                             |        To Print Empolyee data press  2               |
                             |        To delet Empolyee Press  3                    |
                             ********************************************************               ''')
    choice = input("Please inter your choice  ")
    if choice == "1":
        n= input("Please Inter Name  ")
        i= input("Please Inter ID ")
        j= input("Please Inter JOb ")
        s= input("Please Inter Salary ")
        Name={"Name":n,
        "ID":i,
        "JOb":j,
        "Salary":s
        }
        new_Mem (Name)
    elif choice == "2":
        n=input("Please input the name:  ")
        print(o.get(n))
    elif choice == "3":
        n=input("Please input the name:  ")
        if n in o :
            remove=input("please print Y if you really want to remove  ")
            if remove == "Y":
                o.pop(n)
            else:
                pass
        else:
            print("Name not included")
            
    else:
        print("Wrong Input ") 