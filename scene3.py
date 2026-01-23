"""
Project: The Code of Binary / Meru Prastara Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class CinematicCombinatorics(Scene):
    def construct(self):
        # 1. CINEMATIC SETUP
        self.camera.background_color = "#000510" 

        # 2. INTRO TITLE
        title = Text("The Logic of Combinatorics", font_size=40, color=TEAL)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=TEAL).next_to(title, DOWN, buff=0.1).set_width(title.width)
        self.play(Write(title), Create(underline), run_time=1)

        # -----------------------------------------
        # Function to create "2 to the power of n" manually
        # -----------------------------------------
        def create_power(base_num, exp_num, result_num):
            # Base "2"
            base = Text(str(base_num), font_size=60, color=GOLD)
            # Exponent (Thoda chhota aur upar)
            exponent = Text(str(exp_num), font_size=35, color=GOLD)
            exponent.next_to(base, UP + RIGHT, buff=0.05).shift(DOWN*0.2)
            
            # Equal sign
            eq = Text("=", font_size=60, color=GOLD).next_to(base, RIGHT, buff=0.8)
            
            # Result
            res = Text(str(result_num), font_size=60, color=GOLD).next_to(eq, RIGHT, buff=0.5)
            
            # Group them together
            return VGroup(base, exponent, eq, res)

        # -----------------------------------------
        # CASE 1: n = 1
        # -----------------------------------------
        input_text = Text("n = 1", font_size=60, color=BLUE).shift(LEFT*4)
        beat_text = Text("(1 Beat)", font_size=24, color=GRAY).next_to(input_text, DOWN)
        self.play(DrawBorderThenFill(input_text), FadeIn(beat_text))

        # Patterns
        group1 = VGroup(Text("|"), Text("S", color=YELLOW)).arrange(DOWN, buff=0.5)
        
        # FIX: Manual Power Creation (2^1 = 2)
        math_1 = create_power(2, 1, 2).shift(RIGHT*3)

        self.play(LaggedStart(FadeIn(group1, shift=UP), run_time=1))
        self.play(TransformFromCopy(group1, math_1))
        self.play(Indicate(math_1))
        self.wait(1)

        # -----------------------------------------
        # CASE 2: n = 2
        # -----------------------------------------
        new_input = Text("n = 2", font_size=60, color=BLUE).move_to(input_text)
        new_beat = Text("(2 Beats)", font_size=24, color=GRAY).next_to(new_input, DOWN)

        self.play(
            Transform(input_text, new_input),
            Transform(beat_text, new_beat),
            FadeOut(group1),
            FadeOut(math_1)
        )

        patterns_2 = VGroup(
            Text("| |"), Text("| S", color=TEAL),
            Text("S |", color=TEAL), Text("S S", color=YELLOW)
        ).arrange_in_grid(rows=2, cols=2, buff=1)

        # FIX: Manual Power Creation (2^2 = 4)
        math_2 = create_power(2, 2, 4).shift(RIGHT*3)

        self.play(ShowIncreasingSubsets(patterns_2), run_time=1.5)
        self.play(Write(math_2))
        self.wait(1)

        # -----------------------------------------
        # CASE 3: n = 3
        # -----------------------------------------
        new_input_3 = Text("n = 3", font_size=60, color=BLUE).move_to(input_text)
        self.play(
            Transform(input_text, new_input_3),
            FadeOut(beat_text),
            FadeOut(patterns_2),
            FadeOut(math_2)
        )

        patterns_3 = VGroup(
            Text("|||"), Text("||S"), Text("|S|"), Text("|SS"),
            Text("S||"), Text("S|S"), Text("SS|"), Text("SSS")
        ).arrange_in_grid(rows=4, cols=2, buff=0.5).scale(0.8)

        # FIX: Manual Power Creation (2^3 = 8)
        math_3 = create_power(2, 3, 8).shift(RIGHT*3)

        self.play(FadeIn(patterns_3, shift=UP))
        self.play(TransformFromCopy(patterns_3, math_3))
        self.wait(1)

        # -----------------------------------------
        # FINAL: 2^n
        # -----------------------------------------
        self.play(FadeOut(patterns_3), FadeOut(math_3), FadeOut(input_text), FadeOut(title), FadeOut(underline))

        # Big 2^n manually
        base = Text("2", font_size=150, color=GOLD)
        exponent = Text("n", font_size=80, color=GOLD).next_to(base, UP + RIGHT, buff=0.1).shift(DOWN*0.3)
        hero_text = VGroup(base, exponent).move_to(ORIGIN)
        
        box = SurroundingRectangle(hero_text, color=YELLOW, buff=0.4)
        desc = Text("Binary Possibilities", font_size=36, color=WHITE).next_to(box, DOWN)

        self.play(DrawBorderThenFill(hero_text), run_time=2)
        self.play(Create(box), FadeIn(desc))
        self.play(Indicate(hero_text, color=RED, scale_factor=1.2))

        self.wait(2)
