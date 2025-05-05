import numpy as np
import matplotlib.pyplot as plt
from manim import *

def g(x):
    return x+(x-1)*(x+1)**2 # A possible fixed-point iteration function

def fixed_point_iteration(g, p0, tol, max_iter=5):
    iterations = [p0]
    for _ in range(max_iter):
        p = g(p0)
        iterations.append(p)
        if abs(p - p0) < tol:
            break
        p0 = p
    return iterations

# Parameters
p0 = 0.25  # Initial guess
tol = 1e-6
iterations = fixed_point_iteration(g, p0, tol)

# Plot g(x)
x_vals = np.linspace(0, 2, 400)
y_vals = g(x_vals)

'''
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, label='$g(x)$')
plt.plot(x_vals, x_vals, linestyle='dashed', color='gray', label='$y=x$')
plt.scatter(iterations, g(np.array(iterations)), color='blue', zorder=3)
for i in range(len(iterations) - 1):
    plt.plot([iterations[i], iterations[i]], [iterations[i], iterations[i+1]], 'r-')
    plt.plot([iterations[i], iterations[i+1]], [iterations[i+1], iterations[i+1]], 'r-')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.title('Fixed Point Iteration')
plt.show()


'''


# Manim animation
class FixedPointIteration(Scene):
    def construct(self):
        
        
        gfunc_tex = MathTex("g(x) = x+(x-1)(x+1)^{2}").to_edge(UP)
        func_tex = MathTex("f(x) = (x-1)(x+1)^{2}").to_edge(LEFT)
        self.play(Write(func_tex),Write(gfunc_tex))


        axes = Axes(
            x_range=[-2,2, 0.5], y_range=[-2, 2, 0.5],
            axis_config={"color": BLUE}
        )
        g_curve = axes.plot(lambda x: g(x), color=GREEN)
        y_equals_x = axes.plot(lambda x: x, color=GRAY)
        
        self.play(Create(axes), Create(g_curve), Create(y_equals_x))
        
        
        zoomed_axes = Axes(
            x_range = [0.5, 2.0,0.05],
            y_range=[-2, 2],
            axis_config={"color": BLUE}
        )
        #self.play(Transform(axes, zoomed_axes))
        self.play(Transform(g_curve, axes.plot(lambda x: g(x), color=GREEN)))
        self.play(Transform(y_equals_x, axes.plot(lambda x: x, color=GRAY)))

        for j in range(1,len(iterations)):
            x_prev  = iterations[j-1]
            x_j = iterations[j]
            y_prev = g(x_prev)

            dot_label = MathTex(fr"p_{{{j-1}}} = {x_j:.4f}") \
            .next_to(axes.c2p(x_j, g(x_j)), UP)
            
            self.play(FadeIn(dot_label))
            dot = Dot(axes.c2p(iterations[j], g(iterations[j])), color=BLUE)
            self.play(FadeIn(dot))
            if j > 0:
                line1 = Line(axes.c2p(x_prev, y_prev), axes.c2p(x_j, y_prev), color=RED)
                line2 = Line(axes.c2p(x_j,y_prev), axes.c2p(x_j, g(x_j)), color=RED)
                self.play(Create(line1),Create(line2))
            
            self.play(FadeOut(dot_label))
            
            
