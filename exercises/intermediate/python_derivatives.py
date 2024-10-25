from sympy import symbols, diff

x = symbols('x')
f = 4*x**4 + 5*x**3 - 4*x**2 + 2*x

f_prime = diff(f, x)

print(f_prime)