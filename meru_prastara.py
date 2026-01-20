from manim import *

class MeruPrastaraCompact(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        GOLD_TEXT = "#FFD700"  
        CONNECT_COLOR = "#FFFDD0" 
        HIGHLIGHT_COLOR = "#00FFFF" 
        
        # --- TITLE SEQUENCE (Reduced Sizes) ---
        # Sanskrit Heading: 30
        title_sanskrit = Text("मेरु प्रस्तार", font="Nirmala UI", font_size=30, color=GOLD_TEXT).to_edge(UP)
        # English Subtitle: 18
        title_english = Text("(The Mountain of Jewels)", font="Georgia", font_size=18, color=WHITE).next_to(title_sanskrit, DOWN, buff=0.1)
        
        title_group = VGroup(title_sanskrit, title_english)

        self.play(Write(title_sanskrit), FadeIn(title_english))
        self.wait(1)

        # --- HELPER: BUILD ROWS ---
        rows = []
        n_rows = 5 
        rows.append([1])
        for i in range(1, n_rows):
            prev_row = rows[-1]
            new_row = [1] 
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j+1])
            new_row.append(1) 
            rows.append(new_row)

        # --- VISUALIZATION SETUP ---
        visual_rows = VGroup()
        # COMPACT SETTINGS: Chhota Gap aur Chhota Font
        VERTICAL_GAP = 0.8
        HORIZONTAL_GAP = 1.2
        NUMBER_FONT_SIZE = 36

        for i, row_nums in enumerate(rows):
            row_mob = VGroup(*[MathTex(str(num), color=GOLD_TEXT, font_size=NUMBER_FONT_SIZE) for num in row_nums])
            row_mob.arrange(RIGHT, buff=HORIZONTAL_GAP)
            visual_rows.add(row_mob)

        visual_rows.arrange(DOWN, buff=VERTICAL_GAP)
        
        # --- POSITIONING FIX ---
        # Diagram ko title ke thoda paas rakha taaki neeche jagah bache (Buffer 0.8)
        visual_rows.next_to(title_group, DOWN, buff=0.8)

        # --- ANIMATION SEQUENCE ---
        self.play(GrowFromCenter(visual_rows[0]), run_time=1)
        self.wait(0.5)

        lines_group = VGroup()
        for i in range(len(visual_rows) - 1):
            current_row = visual_rows[i]
            next_row = visual_rows[i+1]
            self.play(FadeIn(next_row, shift=DOWN), run_time=0.8)
            
            row_lines = VGroup()
            for j in range(len(current_row)):
                parent = current_row[j]
                child_left = next_row[j]
                child_right = next_row[j+1]
                line1 = Line(parent.get_bottom(), child_left.get_top(), color=CONNECT_COLOR, stroke_width=2, stroke_opacity=0.5)
                line2 = Line(parent.get_bottom(), child_right.get_top(), color=CONNECT_COLOR, stroke_width=2, stroke_opacity=0.5)
                row_lines.add(line1, line2)
            self.play(Create(row_lines), run_time=0.5)
            lines_group.add(row_lines)

        self.wait(1)

        # --- TEXT REVEAL ---
        # Text size bhi adjust kiya
        pascal_text = Text("Known today as: Pascal's Triangle", font="Georgia", font_size=28, color=HIGHLIGHT_COLOR)
        pascal_text.next_to(visual_rows, DOWN, buff=0.5) 
        
        algo_text = Text("An Algorithmic Process", font="Courier New", font_size=20, color=GRAY)
        algo_text.next_to(pascal_text, DOWN, buff=0.15)

        self.play(Write(pascal_text))
        self.play(FadeIn(algo_text))
        self.wait(2)

        # --- GRAND FINALE ---
        self.play(FadeOut(lines_group), FadeOut(algo_text), FadeOut(pascal_text))
        
        # Scale kam kiya (1.1) taaki screen se bahar na bhage
        self.play(visual_rows.animate.scale(1.1).set_color(YELLOW))
        
        magic_rect = SurroundingRectangle(visual_rows, color=YELLOW, buff=0.3, corner_radius=0.5)
        self.play(Create(magic_rect))
        
        final_caption = Text("The Magic of Recursion", font="Georgia", font_size=32, color=WHITE)
        # Final Text Box ke neeche fit aayega
        final_caption.next_to(magic_rect, DOWN, buff=0.4)

        self.play(Write(final_caption))
        
        self.wait(3)