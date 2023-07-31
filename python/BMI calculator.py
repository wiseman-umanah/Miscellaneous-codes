print("What is your name")
name = str(input())
print ("How old are you")
age = str(input())
#Lets now calculate your BMI,Please input something
print("Please input all data correctly")
weight = float(input ("Enter your weight(kg) : "))
height = float(input("Enter your height(cm) : "))
BMI = float(weight/(height**2)*10000)
print("Thank you for using this program")
print(name)
print(age)
print("You are " + str(weight) + ' kg')
print("You are " + str(height) + " cm tall")
print("Your BMI is " + str(round(BMI,1)))
if BMI < 18.5:
   print("Underweight")
   print("Eat healthy food")
elif BMI > 30:
   print("Obesity")
   print("Regular exercises, Avoid junks and Meet a doctor")
elif BMI == 25:
   print("Overweight")
   print("Regular exercises")
elif BMI >= 18.5:
   print('Normal')
   print("Your Body Mass Index(BMI) is okay")
         
