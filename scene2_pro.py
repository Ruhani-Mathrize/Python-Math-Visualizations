from manim import *

class MeruPrastaraPro(Scene):
    def construct(self):
        # 1. Background Setup (Dark Grey for Cinematic look)
        self.camera.background_color = "#111111"

        # Title with Glow Effect
        title = Text("Meru Prastara (The Mountain of Jewels)", font_size=36, color=GOLD)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT, color=GOLD).next_to(title, DOWN)
        self.play(Write(title), Create(underline), run_time=2)

        # 2. Row 0 (Top Jewel)
        row0 = Text("1", font_size=48, color=WHITE).shift(UP*2)
        self.play(DrawBorderThenFill(row0)) # Cool effect

        # 3. Row 1 (Flowing Animation)
        # 1s come out of the top 1
        r1_left = Text("1", font_size=48).move_to(UP*0.5 + LEFT)
        r1_right = Text("1", font_size=48).move_to(UP*0.5 + RIGHT)
        
        self.play(
            TransformFromCopy(row0, r1_left), # Copy hokar niklega
            TransformFromCopy(row0, r1_right),
            run_time=1.5
        )

        # 4. Row 2 (The Magic Addition)
        # Side ke 1s
        r2_left = Text("1", font_size=48).move_to(DOWN*1 + LEFT*2)
        r2_right = Text("1", font_size=48).move_to(DOWN*1 + RIGHT*2)
        
        # Middle Number (Calculation Visualized)
        r2_mid = Text("2", font_size=60, color=YELLOW).move_to(DOWN*1) # Bada size
        
        self.play(
            TransformFromCopy(r1_left, r2_left),
            TransformFromCopy(r1_right, r2_right),
        )
        
        # "2" bante hue dikhana (Left 1 + Right 1 -> merge into 2)
        self.play(
            TransformFromCopy(r1_left, r2_mid),
            TransformFromCopy(r1_right, r2_mid),
            run_time=2
        )
        # Flash effect on 2
        self.play(Indicate(r2_mid, color=RED, scale_factor=1.5))

        # 5. Conclusion
        final_text = Text("1 + 1 = 2", font_size=30, color=YELLOW).next_to(r2_mid, DOWN)
        self.play(Write(final_text))
        
        self.wait(2)