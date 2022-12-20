def main():
    #Read the contents of the file into a list where each line of text in the file 
    # is stored in a separate element in the list.
    province_list = read_list('provinces.txt')
    #Print the entire list.
    print(province_list)
    #Remove the first element from the list.
    province_list.pop(0)
    #Remove the last element from the list.
    province_list.pop()
    #Count the number of elements that are "Alberta" and print that number.
    count = province_list.count('Alberta')
    print(f'The number of Alberta in the list is {count}')

def read_list(province_list):
    province_list = []
    # To open the CSV file
    with open('provinces.txt', 'rt') as provinces_file:
        for line in provinces_file:
            clean_line = line.strip()
            province_list.append(clean_line)
    #Replace all occurrences of "AB" in the list with "Alberta".       
            for i in range(len(province_list)):
                if province_list [i] == 'AB':
                    province_list [i] = 'Alberta'

    return province_list
if __name__ == "__main__":
    main()

