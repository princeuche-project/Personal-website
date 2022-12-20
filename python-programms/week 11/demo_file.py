with open("demo.txt")as demo_file:

    for line in demo_file:

       clean_line = line.strip() 
       parts = line.split(',')
       name = parts[0]
       grade = float(parts[1])
       grade_bouns = grade + 5
       print(f"{name} - {grade} and grade bouns is: {grade_bouns}")
    print("the file continues")
    
print("now the file closed")

colors = 'red blue green yellow brown'

colors_parts = colors.split()
print(colors)

print(colors_parts)


