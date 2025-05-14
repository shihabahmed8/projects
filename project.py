frist_number =float(input("Pleas enter the first number: "))
secons_number =float(input("Pleas enter the second number: "))
choose_calculation = input("Choose the way of calculation that you need -,+,*, /, mod(%), pow()or abs(): ")


if choose_calculation == "-":
     result= frist_number - secons_number
elif choose_calculation=="+":
     result= frist_number + secons_number
elif choose_calculation == "*":
      result= frist_number * secons_number
elif choose_calculation == "/":
      result= frist_number / secons_number
elif choose_calculation == "%":
       result= frist_number % secons_number
elif choose_calculation == "pow()":
       result= pow(frist_number, secons_number)
elif choose_calculation == "abs()":
       result= abs(frist_number - secons_number)

print(f"The result is= {result}")

print("THE END OF CALCULATION")
