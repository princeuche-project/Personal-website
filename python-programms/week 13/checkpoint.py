def main():
    get = display_regular()
    print(f'{get.capitalize()}')
    print(f'{get.upper()}')
    print(f'{get.lower()}')

    # for i in range(4):
    #     i = get
    #     print(f'{i}')

def display_regular():
    name = input('What is your name? ')
    return name
main()

