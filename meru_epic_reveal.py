from manim import *

class MeruEpicReveal(Scene):
    def construct(self):
        # --- CINEMATIC CONFIGURATION ---
        # Ultra Deep Space Background
        BG_COLOR = "#00020A" 
        self.camera.background_color = BG_COLOR
        
        # Colors
        ANCIENT_GOLD = "#C5B358"  
        NEON_CYAN = "#00FFFF"     
        FADED_BLUE = "#001F3F"    

        # --- BUILD ROWS (8 Rows) ---
        rows = []
        n_rows = 8 
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
        VERTICAL_GAP = 0.65 
        HORIZONTAL_GAP = 0.9
        NUMBER_FONT_SIZE = 28 

        for i, row_nums in enumerate(rows):
            row_mob = VGroup()
            for num in row_nums:
                is_odd = num % 2 != 0
                # Using Tex for Cinematic Look
                t = Tex(str(num), font_size=NUMBER_FONT_SIZE, color=ANCIENT_GOLD)
                t.is_odd = is_odd 
                row_mob.add(t)
                
            row_mob.arrange(RIGHT, buff=HORIZONTAL_GAP)
            visual_rows.add(row_mob)

        visual_rows.arrange(DOWN, buff=VERTICAL_GAP)
        
        # --- PERFECT CENTERING ---
        visual_rows.move_to(ORIGIN)

        # --- ANIMATION PHASE 1: ANCIENT STRUCTURE ---
        self.wait(0.5)
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=UP*0.3, scale=1.1) for row in visual_rows],
                lag_ratio=0.2
            ),
            run_time=2.5
        )
        self.wait(1)

        # --- ANIMATION PHASE 2: EPIC REVEAL ---
        anims = []
        for row in visual_rows:
            for num_mob in row:
                if num_mob.is_odd:
                    # Neon Burst for Odd Numbers
                    anims.append(
                        num_mob.animate
                        .set_color(NEON_CYAN)
                        .scale(1.35) 
                        .set_opacity(1)
                    )
                else:
                    # Fade out Even Numbers
                    anims.append(
                        num_mob.animate
                        .set_color(FADED_BLUE)
                        .set_opacity(0.1) 
                        .scale(0.7)
                    )
        
        # FIX 1: Corrected Rate Function
        self.play(*anims, run_time=3, rate_func=rate_functions.ease_in_out_expo)
        
        # FIX 2: Instead of Camera Zoom, we Scale the Object (Safer & Error-free)
        self.play(
            visual_rows.animate.scale(1.2), # Zoom in effect
            run_time=2
        )

        self.wait(4)