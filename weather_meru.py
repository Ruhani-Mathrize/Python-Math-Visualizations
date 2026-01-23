"""
Project: The Code of Binary / Meru Prastara Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *
import numpy as np

class WeatherMeruCone(Scene):
    def construct(self):
        # --- CINEMATIC CONFIGURATION ---
        BG_COLOR = "#000510" # Deep Ocean/Space Blue
        self.camera.background_color = BG_COLOR
        
        # Colors
        STORM_COLOR = "#00FFFF" # Cyan for the storm center
        PATH_COLOR = "#FFFFFF"  # White for prediction paths
        CONE_COLOR = "#FFD700"  # Gold for the probability cone (Meru)
        LAND_COLOR = "#2E8B57"  # Green for abstract coastline
        TEXT_COLOR = "#E0E0E0"

        # --- PART 1: THE MAP & STORM (The Setup) ---
        
        # 1. Draw Abstract Coastline (Simple Curve)
        coastline = CubicBezier(
            [-4, -2, 0],   # Start (Left-Bottom)
            [-1, 0, 0],    # Control 1
            [2, -1, 0],    # Control 2
            [4, 2, 0]      # End (Right-Top)
        ).set_color(LAND_COLOR).set_stroke(width=4)
        
        coast_label = Text("Coastline", font_size=18, color=LAND_COLOR).next_to(coastline, DOWN, buff=0.2)

        # 2. Create the Storm (Spinning Spiral)
        storm_center = Dot(point=[-3, -2, 0], color=STORM_COLOR, radius=0.15).set_glow_factor(1)
        storm_spirals = VGroup()
        for i in range(3):
            spiral = Circle(radius=0.3 + i*0.1, color=STORM_COLOR).set_opacity(0.5 - i*0.1)
            storm_spirals.add(spiral)
        
        storm_group = VGroup(storm_center, storm_spirals)
        
        # Animate Setup
        self.play(Create(coastline), Write(coast_label), FadeIn(storm_group))
        self.play(Rotate(storm_spirals, angle=2*PI, run_time=2, rate_func=linear))
        
        current_text = Text("Current Location", font_size=18, color=STORM_COLOR).next_to(storm_group, LEFT)
        self.play(Write(current_text))
        self.wait(0.5)

        # --- PART 2: THE CHAOS (Simulation Paths) ---
        # Weather supercomputers run 50+ simulations. We show this as "Chaos".
        
        paths = VGroup()
        start_point = storm_center.get_center()
        
        # Create 15 random paths fanning out
        np.random.seed(10)
        for _ in range(15):
            # Create a jagged path
            points = [start_point]
            curr = start_point
            for step in range(5):
                # Move Generally Right and Up, but with randomness
                dx = 1.2
                dy = np.random.uniform(-0.5, 1.0) # Bias towards up-right
                curr = curr + np.array([dx, dy, 0])
                points.append(curr)
            
            path = VMobject().set_points_as_corners(points)
            path.set_color(PATH_COLOR).set_stroke(width=1, opacity=0.3)
            paths.add(path)

        path_label = Text("Forecasting Models (Chaos)", font_size=18, color=PATH_COLOR).to_edge(UP, buff=1.0)
        
        self.play(
            FadeOut(current_text),
            Write(path_label),
            Create(paths, lag_ratio=0.1, run_time=3)
        )
        self.wait(1)

        # --- PART 3: THE ORDER (Meru Prastara Overlay) ---
        # Now we show how the "Cone" is actually Pascal's Triangle
        
        self.play(
            paths.animate.set_opacity(0.1), # Dim the chaotic paths
            FadeOut(path_label)
        )

        meru_group = VGroup()
        dots_group = VGroup()
        
        # Build a visual cone using Meru Logic (5 steps)
        # We manually place dots to match the storm's trajectory direction (Up-Right)
        
        steps = 5
        # We need to rotate the triangle logic to match the storm path (approx 30 degrees)
        # Base vector for the grid
        vec_a = np.array([1.0, 0.4, 0]) # Move Right-ish
        vec_b = np.array([1.0, -0.2, 0]) # Move Right-Down-ish (widening the cone)
        
        # To make it look like a cone, we spread out from start_point
        
        row_5_vals = [1, 5, 10, 10, 5, 1] # Pascal Row 5
        final_dots = VGroup()

        for step in range(steps + 1):
            # In weather, steps branch out. 
            # We will just show the outline and the nodes
            
            # Create a row of dots
            for k in range(step + 1):
                # Position logic: mixture of vec_a and vec_b
                # P = Start + (step-k)*vec_a + k*vec_b
                # We adjust vectors to make a nice cone shape
                
                # Simplified Cone Logic for Visuals:
                x_pos = start_point[0] + step * 1.2
                # y spreads out based on step
                spread = step * 0.8
                y_start = start_point[1] + (step * 0.5) # General trend up
                y_pos = y_start + (k * -0.6) # Spread down
                
                # Correction to center the spread
                y_pos += (spread / 2) * 0.5 # Shift slightly
                
                pos = np.array([x_pos, y_pos, 0])
                
                dot = Dot(pos, radius=0.06, color=CONE_COLOR)
                dots_group.add(dot)
                
                # If it's the last step, save for numbers
                if step == steps:
                    final_dots.add(dot)
                    
                # Draw lines connecting to previous (implied grid)
                if step > 0:
                   # Visual lines only to show structure
                   line = Line(start_point, pos, stroke_width=1, color=CONE_COLOR).set_opacity(0.2)
                   meru_group.add(line)

        cone_title = Text("The Cone of Uncertainty (Meru Structure)", font_size=18, color=CONE_COLOR).to_edge(UP, buff=1.0)

        self.play(
            Write(cone_title),
            FadeIn(dots_group, lag_ratio=0.1),
            Create(meru_group, run_time=2)
        )

        # --- PART 4: THE PROBABILITY (Center is Safest Prediction) ---
        
        # Highlight the center of the final row
        center_dots = VGroup(final_dots[2], final_dots[3]) # The middle ones (10, 10)
        edge_dots = VGroup(final_dots[0], final_dots[-1])  # The edge ones (1, 1)
        
        # Text for probabilities
        high_prob = Text("High Probability Zone", font_size=18, color=CONE_COLOR)
        high_prob.next_to(center_dots, RIGHT, buff=0.5)
        
        low_prob = Text("Low Probability", font_size=18, color=PATH_COLOR).set_opacity(0.7)
        low_prob.next_to(edge_dots, RIGHT, buff=0.5)
        
        # Connecting lines for labels
        line_high = Line(center_dots.get_center(), high_prob.get_left(), color=CONE_COLOR)
        
        self.play(
            center_dots.animate.set_color(STORM_COLOR).set_glow_factor(0.8).scale(1.5),
            edge_dots.animate.set_opacity(0.4),
            Write(high_prob),
            Create(line_high),
            Write(low_prob)
        )
        
        # Final Statement
        conclusion = Text("Prediction works on Binomial Distribution.", font_size=18, color=TEXT_COLOR).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))


        self.wait(3)
