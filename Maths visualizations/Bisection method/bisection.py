import sympy as sym
import numpy as np
import json

def bisection(f, a, b, accuracy):
    x = sym.Symbol('x')
    A, B = a, b
    steps = [str(f)]

    while True:
        p = (A + B) / 2
        f_p = f.subs(x, p)

        # Store the current step
        steps.append({"a": float(A), "b": float(B), "p": float(p)})

        print(f"a={A}, b={B}, p={p}, f(p)={f_p}")

        if abs(f_p) < accuracy:
            break
        elif f.subs(x, A) * f_p > 0:
            A = p
        else:
            B = p

    # Save steps for Manim animation
    with open(r"D:\\MORA ACADEMICS\SEM2\\Methods of Mathematics\\bisection_steps.json", "w+") as file:
        json.dump(steps, file)
    
    with open("bisection_steps.json","r") as file:
        
        f = file.read()
        print(f)

    return p

x = sym.Symbol('x')
f = x**4 - (2*x**3) - (4*x**2) + (4*x) +4
root = bisection(f, 1, 2, 0.001)
print("Root found at:", root)
