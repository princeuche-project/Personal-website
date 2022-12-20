import math
def main():
   print()

   temperature = float(input("What is the temperature? "))
   fahrenheit_celsuis = input ("Fahrenheit or Celsius (F/C)? " ).upper() 
   #wind_chill = temperature_and_wind_speed(temperature, 1)
   calculation = fahrenheit_to_celsuis(temperature)
   print()
   print(f'The Celsuis temperature is: {calculation}')
  # print(wind_chill)

   for x in range (0, 60, 5 ):
        x += 5  
        if fahrenheit_celsuis == "C":
            temperature_new = (temperature *9/5) + 32
            Wind_Chill = 35.74 + (0.6215*temperature_new) - 35.75*(x**0.16) + (0.4275*temperature_new *(x**0.16))
            print (f"At temperature {temperature_new}F, wind speed at {x}mph. The windchill is: {Wind_Chill:.2f}F")
        elif fahrenheit_celsuis == "F":
            Wind_Chill = 35.74 + (0.6215*temperature) - (35.75* (x**0.16)) + (0.4275*temperature*(x**0.16))
            print (f"At temperature {temperature}F, and wind speed at {x}mph. The windchill is: {Wind_Chill:.2f}F. ")
        
def  fahrenheit_to_celsuis(temperature):

    temperature_new = (temperature *9/5) + 32
    return temperature_new

def temperature_and_wind_speed(temperature, Wind_chill):
        
        Wind_Chill = 35.74 + (0.6215*temperature) - 35.75* math.pow(Wind_chill, 0.16) + (0.4275*temperature * math.pow(Wind_chill, 0.16))
        return Wind_Chill

main()