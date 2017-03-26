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
		return voltage / current
def Power(voltage,current):
		return voltage * current
if your_choice == 1:
		current = float(input("Enter the value of current in Ampere: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print("You entered current = %s Ampere and reistance = %s ohms"%(current, resistance))
		print("Now your answer in volts is: ")
		print(Voltage(current, resistance))
	
elif your_choice == 2:
		voltage = float(input("Enter the value of voltage in volts: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print("You entered voltage = %s volts and resistance = %s ohms"%(voltage, resistance))
		print("Now your answer in Ampere is: ")
		print(Current(voltage, reistance))
		
elif your_choice == 3:
		current = float(input("Enter the value of current in Ampere: "))
		voltage = float(input("Enter the value of voltage in volts: "))
		print("You entered voltage = %s volts and current = %s Ampere"%(voltage, current))
		print("Now your answer in Ohms is: ")
		print(Resistance(voltage, current))
		
elif your_choice == 4:
		voltage = float(input("Enter the value of voltage in volts: "))
		current = float(input("Enter the value of current in Ampere: "))
		print("You entered voltage = %s volts and current = %s Ampere"%(voltage, current))
		print("Now your answer in Watt is: ")
		print(Power(voltage, current))
		
else:
	print("invalid")
		

input("click enter to exit: " )








