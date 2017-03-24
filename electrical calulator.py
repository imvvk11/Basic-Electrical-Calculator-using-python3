#Electircal calculator from python command line
import math
print("Select Electrical operation")
print("1.Voltage")
print("2.Current")
print("3.Resistance")
print("4.Power")

your_choice = input("please select your choices from 1/2/3/4: ")

def Voltage(current, resistance):
		return current * resistance
def Current(voltage, resistance):
		return voltage / resistance
def Resistance(voltage, current):
		return current / resistance
def Power(voltage,current):
		return voltage * current
if your_choice == 1:
		current = float(input("Enter the value of current in Ampere: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print(Voltage(current, resistance))
elif your_choice == 2:
		voltage = float(input("Enter the value of voltage in volts: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print(Current(voltage, reistance))
elif your_choice == 3:
		current = float(input("Enter the value of current in Ampere: "))
		voltage = float(input("Enter the value of voltage in volts: "))

		print(Resistance(voltage, current))
elif your_choice == 4:
		current = float(input("Enter the value of current in Ampere: "))
		voltage = float(input("Enter the value of voltage in volts: "))
		print(Power(voltage, current))
else:
	print("invalid")
		

input("click enter to exit: " )








