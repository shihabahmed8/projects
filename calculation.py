list_number=[]



#number= (input("Enter the numbe/ FOR FINSH ENTER DONE: "))

while True:
    number= (input("Enter the numbe/ FOR FINSH ENTER DONE: "))
    #list_number.append(number)

    if number.lower() == "done":
        break 

    else: list_number.append(number)



for i in list_number:

    print(F"Your Number That You Enterd:{i}")