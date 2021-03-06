#Electircal calculator 
import math  

#Define a class 
class ElectricalCalculator(Object):
	#Initialize constructors
	def __init__(self):
	    self.current = 0
	    self.resistance = 0
	    self.voltage = 0
		
	def voltage(self, current, resistance):
	    self.voltage = float(current * resistance) #
        returns self.voltage
		
	def current(self,voltage, resistance):
	    self.current = float(voltage / resistance) 
		return self.current
	
	def resistance(self,voltage, current):
	    self.resistance = voltage / current #
		return self.resistance
	
	def power(self,voltage,current): 
		return voltage * current  #
		return self.power
	
	def power_factor(self, KW, KVA):
		return KW / KVA

	
def electCalculator():
	print ("Let's do some some electrical calculations")
	
	
	
print("Select Electrical operation")
print("1.Voltage")
print("2.Current")
print("3.Resistance")
print("4.Power")
print("5.Power factor")



#Make your choice from the above parameters 
your_choice = input("please select your choices from 1/2/3/4: ")

"""
def Voltage(current, resistance):
	return current * resistance #returns voltage
def Current(voltage, resistance):
	return voltage / resistance #returns current
def Resistance(voltage, current):
	return voltage / current #returns resistance
def Power(voltage,current): 
	return voltage * current  #returns power
def Power_factor(KW,KVA):
	KW = int(input("Enter value in KW: "))
	KVA = int(input("Enter value in KVA: "))
	return KW / KVA
"""

try:
	electrical_calc = ElectricalCalculator()
	if your_choice == 1:
		current = float(input("Enter the value of current in Ampere: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print("You entered current = %s Ampere and reistance = %s ohms"%(current, resistance))
		print("Now your answer in volts is: ")
		print(electrical_calc.voltage(current, research))
	
	elif your_choice == 2:
		voltage = float(input("Enter the value of voltage in volts: "))
		resistance = float(input("Enter the value of resistance in ohms: "))
		print("You entered voltage = %s volts and resistance = %s ohms"%(voltage, resistance))
		print("Now your answer in Ampere is: ")
	    print(electrical_calc.voltage(voltage, resistance))
		
	elif your_choice == 3:
		current = float(input("Enter the value of current in Ampere: "))
		voltage = float(input("Enter the value of voltage in volts: "))
		print("You entered voltage = %s volts and current = %s Ampere"%(voltage, current))
		print("Now your answer in Ohms is: ")
		print(self.resistance(current, voltage))
		
	elif your_choice == 4:
		voltage = float(input("Enter the value of voltage in volts: "))
		current = float(input("Enter the value of current in Ampere: "))
		print("You entered voltage = %s volts and current = %s Ampere"%(voltage, current))
		print("Now your answer in Watt is: ")
		print(self.power(voltage, current))
		
	elif your_choice == 5:
	    KW = int(input("Enter value in KW: "))
		KVA = int(input("Enter value in KVA: "))
		print(self.power_factor(KW, KVA))
		
	else:
		print("Please select from above Inputs")
		
except ValueError:
	print("Invalid input")
		
		
input("click enter to exit: " )


if __name__ == "__main__":
	electCalculator()





