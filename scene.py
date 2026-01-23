"""
Project: The Code of Binary / Meru Prastara Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class PingalaDecoding(Scene):
    def construct(self):
        # 1. Title Setup
        title = Text("Chandah-shastra (200 BC)", font_size=40, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Setup Words
        # YA (Laghu)
        text_ya = Text("YA", font_size=80, color=WHITE).shift(LEFT*2)
        sub_ya = Text("Short", font_size=24, color=GRAY).next_to(text_ya, DOWN)

        # MA (Guru)
        text_ma = Text("MA", font_size=80, color=WHITE).shift(RIGHT*2)
        sub_ma = Text("Long", font_size=24, color=GRAY).next_to(text_ma, DOWN)

        self.play(FadeIn(text_ya), FadeIn(sub_ya), FadeIn(text_ma), FadeIn(sub_ma))
        self.wait(1)

        # 3. Symbols Appear
        sym_laghu = Text("|", font_size=100, color=GOLD).next_to(text_ya, UP)
        sym_guru = Text("S", font_size=100, color=GOLD).next_to(text_ma, UP)

        self.play(Write(sym_laghu), Write(sym_guru))
        self.wait(1)

        # 4. The Morph (Magic Step)
        # | becomes 1
        num_one = Text("1", font_size=100, color=BLUE).move_to(sym_laghu.get_center())
        # S becomes 0
        num_zero = Text("0", font_size=100, color=BLUE).move_to(sym_guru.get_center())

        self.play(
            Transform(sym_laghu, num_one),
            Transform(sym_guru, num_zero),
            run_time=2
        )

        # 5. Final Result
        final_text = Text("BINARY DETECTED", font_size=36, color=BLUE).next_to(title, DOWN)
        self.play(Write(final_text))

        self.wait(2)
