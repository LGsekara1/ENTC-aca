from manim import *
import numpy as np
import json

class BisectionMethodGraph(Scene):
    def construct(self):
        # Load saved bisection steps
        with open("bisection_steps.json", "r") as file:
            steps = json.load(file)
        
        # Debugging: Print type and content of 'steps' to verify it is a list
        #print("Type of steps:", type(steps))
        #print("Loaded steps:", steps)
        
        # Check if steps are loaded correctly
        if not steps:
            print("Error: No steps found in the JSON file!")
            return  # Exit the method early if no steps are found
        
        # Define the function
        def func(x):
            return x**3 - 25

        # Axes setup (initial full range for visualization)
        axes = Axes(
            x_range=[0, 4, 1],  # Full x-range initially
            y_range=[-30, 30, 10],
            axis_config={"color": WHITE}
        ).add_coordinates()

        # Initial function graph
        graph = axes.plot(func, color=YELLOW)

        # Labels
        func_label = MathTex("f(x) = x^3 - 25").to_edge(UP)

        # Initial a, b, p markers (create initial lines for a, b, p)
        a_line = Line(start=axes.c2p(steps[0]["a"], 20), end=axes.c2p(steps[0]["a"], -20), color=RED)
        b_line = Line(start=axes.c2p(steps[0]["b"], 20), end=axes.c2p(steps[0]["b"], -20), color=BLUE)
        p_line = Line(start=axes.c2p(steps[0]["p"], 20), end=axes.c2p(steps[0]["p"], -20), color=GREEN)

        

        # Create the initial scene with axes, graph, and lines

        self.play(Create(axes), Write(func_label))
        self.play(Create(graph))
        self.play(Create(a_line), Create(b_line), Create(p_line))

        p = steps[0]["p"]
        p_label0 = Tex(str(p),color=GREEN).next_to(axes.c2p(p, 0), UP)
        
        # Iterate through steps and update axes and lines
        self.play(Write(p_label0))
        a,b = step[0]["a"], step[0]["b"]

        for step in steps[1:]:
            # Debugging: print each step
            #print("Step:", step)
            
            # Zoom in to the interval [2, 3] for x-range (x-range zoom)
            zoomed_axes = Axes(
                x_range=[a, b, 0.1],  # Zoom into the range between 2 and 3 for x-axis
                y_range=[-30, 30, 10],  # Keep y-range unchanged
                axis_config={"color": WHITE}
            ).add_coordinates()

            # Create the function graph with the zoomed axes
            zoomed_graph = zoomed_axes.plot(func, color=YELLOW)

            # Update lines for a, b, p at this iteration
            new_a_line = Line(start=zoomed_axes.c2p(step["a"], 20), end=zoomed_axes.c2p(step["a"], -20), color=RED)
            new_b_line = Line(start=zoomed_axes.c2p(step["b"], 20), end=zoomed_axes.c2p(step["b"], -20), color=BLUE)
            new_p_line = Line(start=zoomed_axes.c2p(step["p"], 20), end=zoomed_axes.c2p(step["p"], -20), color=GREEN)
            p = step["p"]
            p_label = Tex(f"p={p}", color=GREEN).move_to(np.array([2.5, -3, 0]))
  
            

            # Transition to the zoomed axes and graph
            self.play(
                Transform(axes, zoomed_axes),  
                Transform(graph, zoomed_graph),
                Transform(a_line, new_a_line),  
                Transform(b_line, new_b_line),  
                Transform(p_line, new_p_line),
                Transform(p_label0,p_label),  

                run_time=0.7  # Adjust run time for smoother animation
            )
        

        self.wait(2)  



