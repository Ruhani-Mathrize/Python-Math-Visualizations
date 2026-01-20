from manim import *

class PingalaCinematicTableCentered(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        W = config.frame_width
        H = config.frame_height

        # --- HELPER FUNCTION ---
        def get_pingala_patterns(n):
            if n <= 0: return [""]
            if n == 1: return ["|", "S"]
            prev_patterns = get_pingala_patterns(n - 1)
            new_patterns = ["|" + p for p in prev_patterns] + ["S" + p for p in prev_patterns]
            return new_patterns

        # --- TITLE ---
        title = Title(r"Pingala's Chandahśāstra: The Binary Growth")
        self.play(Write(title))

        # --- ROW 1: n=1 ---
        row1_label = Text("1 Syllable:", font_size=36, color=BLUE).to_edge(LEFT).shift(UP*1.5)
        patterns_n1 = get_pingala_patterns(1)
        row1_patterns = VGroup(*[Text(p, font="Courier New", font_size=36) for p in patterns_n1]).arrange(RIGHT, buff=1)
        row1_patterns.next_to(row1_label, RIGHT, buff=2)
        
        # LATEX MATH
        row1_math = MathTex(r"\rightarrow 2^1 = 2", font_size=46, color=YELLOW).next_to(row1_patterns, RIGHT, buff=2)

        self.play(Write(row1_label))
        self.play(ShowIncreasingSubsets(row1_patterns), run_time=1.5)
        self.play(Write(row1_math))
        self.wait(0.5)

        # --- ROW 2: n=2 ---
        row2_label = Text("2 Syllables:", font_size=36, color=BLUE).next_to(row1_label, DOWN, buff=1.5)
        patterns_n2 = get_pingala_patterns(2)
        patterns_n2_str = ",  ".join(patterns_n2)
        row2_patterns = Text(patterns_n2_str, font="Courier New", font_size=30).next_to(row2_label, RIGHT, buff=1)
        row2_patterns.align_to(row1_patterns, LEFT)
        
        # LATEX MATH
        row2_math = MathTex(r"\rightarrow 2^2 = 4", font_size=46, color=YELLOW).next_to(row2_patterns, RIGHT, buff=1)

        self.play(Write(row2_label))
        self.play(Write(row2_patterns), run_time=2)
        self.play(Write(row2_math))
        self.wait(0.5)

        # --- ROW 3: n=3 ---
        row3_label = Text("3 Syllables:", font_size=36, color=BLUE).next_to(row2_label, DOWN, buff=1.5)
        patterns_n3 = get_pingala_patterns(3)
        patterns_n3_str = ", ".join(patterns_n3[:4]) + "\n" + ", ".join(patterns_n3[4:])
        row3_patterns = Text(patterns_n3_str, font="Courier New", font_size=24, line_spacing=1.2).next_to(row3_label, RIGHT, buff=1)
        row3_patterns.align_to(row2_patterns, LEFT)
        
        # LATEX MATH
        row3_math = MathTex(r"\rightarrow 2^3 = 8", font_size=46, color=YELLOW).next_to(row3_patterns, RIGHT, buff=1)

        self.play(Write(row3_label))
        self.play(Write(row3_patterns), run_time=1.5)
        self.play(Write(row3_math))
        self.wait(1)

        # --- SCROLLING EFFECT (n=4 to n=8) ---
        self.play(
            FadeOut(row1_label), FadeOut(row1_patterns), FadeOut(row1_math),
            FadeOut(row2_label), FadeOut(row2_patterns), FadeOut(row2_math),
            FadeOut(row3_label), FadeOut(row3_patterns), FadeOut(row3_math),
            run_time=0.5
        )

        scroll_label = Text("Explosion of Patterns...", color=RED, font_size=40).to_edge(UP).shift(DOWN*1.5)
        
        n_tracker = ValueTracker(3)
        
        n_display = Integer(number=3, font_size=60, color=BLUE).move_to(LEFT*3)
        n_label = Text("Syllables (n):", font_size=24).next_to(n_display, UP)
        
        total_display = Integer(number=8, font_size=60, color=YELLOW).move_to(RIGHT*3)
        total_label = Text("Total Patterns:", font_size=24).next_to(total_display, UP)

        # BIG LATEX FORMULA - FIXED POSITION TO CENTER
        math_display = MathTex(r"2^n", font_size=120, color=YELLOW).move_to(ORIGIN)

        n_display.add_updater(lambda d: d.set_value(n_tracker.get_value()))
        total_display.add_updater(lambda d: d.set_value(2**int(n_tracker.get_value())))

        huge_pattern_list = get_pingala_patterns(7) + get_pingala_patterns(8)
        scrolling_text_str = "\n".join(huge_pattern_list)
        # Matrix style binary column
        scrolling_column = Text(scrolling_text_str, font="Courier New", font_size=20, line_spacing=1.5, color=GRAY_B)
        
        scroll_window_box = Rectangle(width=4, height=4, color=WHITE).move_to(ORIGIN)
        scroll_window_box.set_stroke(opacity=0) 

        scrolling_column.next_to(scroll_window_box, DOWN, buff=1)
        
        mask_rect_top = Rectangle(width=W, height=H/2 + 2, fill_color=BLACK, fill_opacity=1, stroke_opacity=0)
        mask_rect_top.next_to(scroll_window_box, UP, buff=0)
        
        mask_rect_bottom = Rectangle(width=W, height=H/2 + 2, fill_color=BLACK, fill_opacity=1, stroke_opacity=0)
        mask_rect_bottom.next_to(scroll_window_box, DOWN, buff=0)
        
        self.add_foreground_mobject(mask_rect_top)
        self.add_foreground_mobject(mask_rect_bottom)

        self.play(Write(scroll_label), FadeIn(n_display), FadeIn(total_display), FadeIn(n_label), FadeIn(total_label))
        self.add(scrolling_column) 

        self.play(
            n_tracker.animate.set_value(8),
            scrolling_column.animate.move_to(UP * 20), 
            run_time=6,
            rate_func=linear 
        )

        n_display.clear_updaters()
        total_display.clear_updaters()
        n_display.set_value(8)
        total_display.set_value(256)
        self.wait(1)

        # --- FINAL REVEAL ---
        self.remove(mask_rect_top, mask_rect_bottom, scrolling_column)
        self.play(
            FadeOut(scroll_label), FadeOut(n_display), FadeOut(total_display), FadeOut(n_label), FadeOut(total_label)
        )

        final_text = Text("General Formula:", font_size=40, color=BLUE).next_to(math_display, UP)
        self.play(Write(final_text), Write(math_display))
        
        box = SurroundingRectangle(math_display, color=YELLOW, buff=0.5)
        self.play(Create(box))

        self.wait(3)