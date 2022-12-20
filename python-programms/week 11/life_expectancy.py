with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    year_0 = input("Please enter the year of interest: ")
    #country = input("please enter a country: ")
    higher = 0
    lowest = 20
    country_of = ''
    year_of = ""
    year_2 = ''
    country_2 = ""
    
    average = 54.59
    high = 0
    country_3 = ''
    low = 1000

    for line in life_expectancy:
        clean_line = line.strip()
        parts = line.split(",")

        entity = (parts[0])
        code = parts[1]
        year = parts[2]
        expectancy = float(parts[3])

        if expectancy > higher:
            higher = expectancy
            country_of = entity
            year_of = year

        if expectancy < lowest:
            lowest = expectancy
            country_2 = entity
            year_2 = year

        if expectancy > average:
            average = expectancy

            if expectancy < high:
                high = expectancy
                country_1 = entity
                year_0 = year

            if expectancy < low:
                low = expectancy
                country_3 = entity

    print(
        F"The overall max life expectancy is: {higher} from {country_of} in {year_of} ")
    print(
        F"The overall min life expectancy is: {lowest} from {country_2} in {year_2} ")
    print()

    print(f"For the year {year_0}:")
    print(
        f'The average life expectancy across all countries was {low}')
    print(F"The overall max life expectancy was in {entity} with {higher}")
    print(
        F"The overall min life expectancy was in {country_3} with {expectancy}")


print('File closed')

