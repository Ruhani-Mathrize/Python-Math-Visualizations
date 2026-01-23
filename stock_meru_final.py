"""
Project: The Code of Binary / Meru Prastara Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *
import random
import numpy as np

class StockMeruFinal(Scene):
    def construct(self):
        # --- CINEMATIC CONFIGURATION ---
        BG_COLOR = "#000814"
        self.camera.background_color = BG_COLOR
        
        STOCK_NEON = "#00FFAA"   
        MERU_GOLD = "#FFD700"    
        AXIS_COLOR = "#334455"   
        TEXT_COLOR = "#E0E0E0"   

        # --- PART 1: THE COMPACT STOCK CHART ---
        
        # 1. Create Axes
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[40, 80, 10],
            x_length=7,
            y_length=4,
            axis_config={"color": AXIS_COLOR, "stroke_width": 2, "include_tip": False},
            x_axis_config={"font_size": 18},
            y_axis_config={"font_size": 18},
        ).move_to(ORIGIN).shift(DOWN*0.5)

        x_label = axes.get_x_axis_label(Text("Time", font_size=18, color=AXIS_COLOR))
        y_label = axes.get_y_axis_label(Text("Price", font_size=18, color=AXIS_COLOR))
        labels = VGroup(x_label, y_label)

        # 2. Generate Random Stock Path
        start_price = 60
        prices = [start_price]
        np.random.seed(42) 
        for _ in range(6):
            change = np.random.uniform(-5, 7) 
            next_price = prices[-1] + change
            prices.append(next_price)
        
        stock_line = VMobject(color=STOCK_NEON, stroke_width=3)
        stock_line.set_points_as_corners(
            [axes.coords_to_point(i, p) for i, p in enumerate(prices)]
        )
        stock_line.set_glow_factor(0.5)

        # Animate Stock Chart
        self.play(Create(axes), Write(labels), run_time=1.5)
        self.play(Create(stock_line), run_time=2.5, rate_func=linear)
        
        chart_title = Text("Stock Market Movement (Randomness)", font_size=18, color=STOCK_NEON)
        chart_title.next_to(axes, UP, buff=0.5)
        self.play(Write(chart_title))
        self.wait(1)

        # --- PART 2: THE MERU PRASTARA OVERLAY ---
        
        tree_group = VGroup()
        nodes_group = VGroup()
        terminal_nodes_data = {} 
        
        steps = 5 
        start_point = axes.coords_to_point(0, start_price)
        start_node = Dot(start_point, color=MERU_GOLD, radius=0.08).set_glow_factor(1)
        
        def build_tree_visuals(current_point, current_step):
            if current_step >= steps:
                return

            dx = 1.4  
            dy = 0.6  
            
            next_up = current_point + np.array([dx, dy, 0])
            next_down = current_point + np.array([dx, -dy, 0])

            line_up = Line(current_point, next_up, color=MERU_GOLD, stroke_width=2).set_opacity(0.7)
            line_down = Line(current_point, next_down, color=MERU_GOLD, stroke_width=2).set_opacity(0.7)
            tree_group.add(line_up, line_down)

            node_up = Dot(next_up, color=MERU_GOLD, radius=0.05)
            node_down = Dot(next_down, color=MERU_GOLD, radius=0.05)
            nodes_group.add(node_up, node_down)
            
            if current_step == steps - 1:
                y_key = round(next_up[1], 2)
                terminal_nodes_data[y_key] = next_up
                y_key_down = round(next_down[1], 2)
                terminal_nodes_data[y_key_down] = next_down

            build_tree_visuals(next_up, current_step + 1)
            build_tree_visuals(next_down, current_step + 1)

        
        # ERROR FIX: 'FadeOut' opacity error fixed by using '.animate.set_opacity'
        self.play(
            stock_line.animate.set_opacity(0.2), # Dim the line instead of fading out incorrectly
            FadeOut(chart_title),
            axes.animate.set_opacity(0.3), # Dim axes
            FadeIn(start_node)
        )
        
        overlay_title = Text("The Underlying Structure: Binomial Tree", font_size=18, color=MERU_GOLD)
        overlay_title.next_to(axes, UP, buff=0.5)
        self.play(Write(overlay_title))

        build_tree_visuals(start_point, 0)
        
        self.play(
            Create(tree_group, lag_ratio=0.1),
            GrowFromCenter(nodes_group, lag_ratio=0.1),
            run_time=3,
            rate_func=smooth
        )

        # --- PART 3: THE REVEAL (Pascal Numbers) ---
        
        sorted_y_keys = sorted(terminal_nodes_data.keys(), reverse=True)
        pascal_values = [1, 5, 10, 10, 5, 1] 
        
        numbers_group = VGroup()

        for i, y_key in enumerate(sorted_y_keys):
            if i < len(pascal_values):
                pos = terminal_nodes_data[y_key]
                val = pascal_values[i]
                
                num_text = Text(str(val), color=MERU_GOLD, font_size=18, font="Georgia")
                num_text.next_to(pos, RIGHT, buff=0.2)
                numbers_group.add(num_text)
            
        final_label = Text("Probabilities (Bell Curve)", font_size=18, color=STOCK_NEON)
        final_label.to_edge(DOWN, buff=0.5)

        self.play(
            Write(numbers_group),
            FadeIn(final_label),
            nodes_group.animate.set_glow_factor(0.8).set_color(STOCK_NEON)
        )
        

        self.wait(4)
