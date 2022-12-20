with open("life-expectancy.csv") as life_expectancy:
  next(life_expectancy)
  year = input("Please enter the year of interest: ")
 # country = input("please enter a country: ")
  higher = 0
  lowest = 20
 
  for line in life_expectancy:
    clean_line = line.strip()
    parts = line.split(",")
    index_number = float(parts[3])
    country = parts[0]
    year = parts[2]
   
    
    if country == parts[0]:
      country = country
    
     

    if index_number > higher:
       higher = index_number
    if index_number < lowest:
          lowest = index_number
     
  print(F"The overall max life expectancy is: {higher} ")
  print(F"The overall min life expectancy is: {lowest} ")
  print()
  
  
 
  print(f"For the year {year}:")
  print(F"The overall max life expectancy was in {country} with {index_number}")
  print(F"The overall min life expectancy was in {country} with {lowest}")



print('File closed')
