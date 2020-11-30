def List_pin_fun(i):
    k=input("please input in or out for pin_"+str(i)+" : ")
    if k == "in" :
        List_pin.append("1")
    elif k=="out":
        List_pin.append("0")
    else:
        k=input("please input in or out for pin_"+str(i)+" : ")
        List_pin_fun(i)
global List_pin 
List_pin =[]
for i in range(7):
    
    List_pin_fun(i)
f=open("trial_1.c","w")
f.writelines('void Init_PORT (void)\n')
f.writelines('{\n' )
f.writelines('    DDRA = 0b' )  
f.writelines(List_pin)
f.writelines(';' )  
f.writelines('\n}\n' )
f=open("trial_1.c")
content=f.read()
f.close()
print(content)
