unit = input ("is this temperature in Celsius or Fahrenheit  (C/F)")
temp = float(input("Enter the Temperature :  "))

if unit =="C" :
    temp = round((9 * temp) / 5 +32 , 1)
    print(f"The Temperature in Fehranheit is : {temp} F")
elif unit =="F":
    temp =round((temp -32 ) * 5/9,1) 
    print(f"The Temperature in Celsius is : {temp} C")
else:
    print(f"unit {unit} is an invaid unit of measurement")