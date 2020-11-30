
f=open("trial.c","a")

F=f.writelines('void Init_PORT (void)\n' )
F=f.writelines('{\n' )
F=f.writelines('    DDRA = ob' )

def check_pin(Pin_state,i):
    if "in" in Pin_state:
        F=f.write("1")
    elif "out" in Pin_state :
        F=f.write("0")
    else:
        Pin_state = input("please input in or out for pin_"+str(i)+" : ")
        check_pin(Pin_state,i)

for i in range(7):
   
    Pin_state = input("please input in or out for pin_"+str(i)+" : ")
    
    check_pin(Pin_state,i)
    
F=f.writelines('\n}\n' )
f.close()
          
