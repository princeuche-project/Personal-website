import math
('--------------------------------------------')
print()

print('Welcome to the velocity calculation. Please enter the fellowing:/n ')
m = float(input('Mass (in kg) '))
print()
g = float(input('Gravity (in m/s^2, 9.8 for earth, 24 for jupiter): '))
print()
t = float(input('Time (in seconds): '))
print()
p = float(input('Density of the fluid (in kg/m^3 for air, 1000 for water): '))
print()
a = float(input('Cross sectional area (in m^20; '))
print()
c = float(input('Drag consant (0.5 for sphere, 1.1 for cylinder): '))

print()

c = (1/2)* p * a * c
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)/ m) * t))
print()
print(f'The inner value of c is: {c:.3f}')
print(f'The velosity  after {t} seconds is: {v:.3f} m/s')
t_velocity = math.sqrt(m*g/c)
print(t_velocity)

