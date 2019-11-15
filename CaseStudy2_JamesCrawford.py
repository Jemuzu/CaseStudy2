print("XXXXXXXXXXXXXXXXXXXXXX")
print("XX                  XX")
print("XX    ByteStop      XX") 
print("XX                  XX")
print("XXXXXXXXXXXXXXXXXXXXXX")
print("                      ")
name= input("Enter your name: ")
print("Hello"  , name + ".")

cpu_Num= float(input("Enter quantity of CPU: "))
hdd_Num= float(input("Enter quantity of HDD: "))
ram_Num= float(input("Enter quantity of RAM: "))
psu_Num= float(input("Enter quantity of PSU: "))
print("=====","Item Costs","=========")
cpu_Tot = 125.75 * cpu_Num
hdd_Tot = 76.25 * hdd_Num
ram_Tot = 35.50 * ram_Num
psu_Tot = 85.45 * psu_Num
print("Total cost of CPU:    "  ,cpu_Tot) 
print("Total cost of HDD:    "  ,hdd_Tot)
print("Total cost of RAM:    "  ,ram_Tot)
print("Total cost of PSU:    "  ,psu_Tot)
print("                        =======")
subtotal= (cpu_Tot + hdd_Tot + ram_Tot + psu_Tot)
print("Subtotal of items:   " , subtotal)
amount_Due = float(input("Enter the amount due: ")) 
amount_Entered = amount_Due
print("Amount Entered:     " , amount_Due)
print("                     ======")
owed = (amount_Due - subtotal)
print("Change Due         ", owed)
