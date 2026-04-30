from manim import *
import math

class MeruSciFiHologram(ThreeDScene):
    def construct(self):
        # 1. DEEP SPACE BACKGROUND
        self.camera.background_color = "#020202"

        # High-Tech Cyberpunk Colors
        COLOR_NEON_CYAN = "#00FFFF"
        COLOR_NEON_GOLD = "#FFD700"
        COLOR_NEON_ORANGE = "#FF3300"
        COLOR_DARK_GRID = "#1A1A1A"

        # ---------------------------------------------------------
        # HELPER: Custom Sci-Fi HUD Box (Replaces boring rectangles)
        # ---------------------------------------------------------
        def get_hud_box(value="", is_empty=True, color=COLOR_NEON_CYAN):
            w, h = 0.85, 0.65
            # Base faint glass background
            base_bg = Rectangle(width=w, height=h).set_stroke(color, width=1, opacity=0.2).set_fill(BLACK, opacity=0.8)
            
            # Thick targeting corners (The sci-fi look)
            c_len = 0.15
            thick = 3
            corners = VGroup(
                # Top Left
                Line(base_bg.get_corner(UL), base_bg.get_corner(UL) + RIGHT*c_len).set_stroke(color, thick),
                Line(base_bg.get_corner(UL), base_bg.get_corner(UL) + DOWN*c_len).set_stroke(color, thick),
                # Top Right
                Line(base_bg.get_corner(UR), base_bg.get_corner(UR) + LEFT*c_len).set_stroke(color, thick),
                Line(base_bg.get_corner(UR), base_bg.get_corner(UR) + DOWN*c_len).set_stroke(color, thick),
                # Bottom Left
                Line(base_bg.get_corner(DL), base_bg.get_corner(DL) + RIGHT*c_len).set_stroke(color, thick),
                Line(base_bg.get_corner(DL), base_bg.get_corner(DL) + UP*c_len).set_stroke(color, thick),
                # Bottom Right
                Line(base_bg.get_corner(DR), base_bg.get_corner(DR) + LEFT*c_len).set_stroke(color, thick),
                Line(base_bg.get_corner(DR), base_bg.get_corner(DR) + UP*c_len).set_stroke(color, thick),
            )
            
            box_group = VGroup(base_bg, corners)
            
            if not is_empty:
                txt = Text(str(value), font="monospace", weight=BOLD, color=COLOR_NEON_GOLD).scale(0.5)
                box_group.add(txt)
                
            return box_group

        # ---------------------------------------------------------
        # BUILD THE HOLOGRAPHIC PYRAMID (7 Rows)
        # ---------------------------------------------------------
        num_rows = 7
        mountain_empty = VGroup()
        mountain_filled = VGroup()
        
        for n in range(num_rows):
            row_empty = VGroup()
            row_filled = VGroup()
            for k in range(n + 1):
                row_empty.add(get_hud_box(is_empty=True, color="#333333"))
                val = math.comb(n, k)
                row_filled.add(get_hud_box(is_empty=False, value=val, color=COLOR_NEON_CYAN))
                
            row_empty.arrange(RIGHT, buff=0.1)
            row_filled.arrange(RIGHT, buff=0.1)
            mountain_empty.add(row_empty)
            mountain_filled.add(row_filled)
            
        mountain_empty.arrange(DOWN, buff=0.15).move_to(ORIGIN)
        
        # Align filled mountain
        for i in range(num_rows):
            for j in range(len(mountain_filled[i])):
                mountain_filled[i][j].move_to(mountain_empty[i][j].get_center())

        # ---------------------------------------------------------
        # ACTION 1: INITIAL SCANNING SHOT (Table 22.1)
        # ---------------------------------------------------------
        # Dramatic low angle, starting close
        self.set_camera_orientation(phi=75 * DEGREES, theta=-80 * DEGREES, zoom=1.8, focal_point=mountain_empty[3].get_center())
        
        self.play(Create(mountain_empty, lag_ratio=0.02), run_time=2)
        
        # Scanning laser sweep across the empty grid
        scan_line = Line(LEFT*5, RIGHT*5, color=COLOR_NEON_CYAN).set_stroke(width=4, opacity=0.5).move_to(mountain_empty.get_top())
        self.play(scan_line.animate.move_to(mountain_empty.get_bottom()), run_time=1.5, rate_func=there_and_back)
        self.remove(scan_line)

        # ---------------------------------------------------------
        # ACTION 2: POPULATING THE DATA (Table 22.2 & 22.3)
        # ---------------------------------------------------------
        # Drone pulls up and rotates for a better tactical view
        self.move_camera(phi=60 * DEGREES, theta=-90 * DEGREES, focal_point=mountain_empty.get_center(), zoom=1.2, run_time=2)
        
        # The borders light up first
        border_anims = [FadeIn(mountain_filled[0][0], scale=1.2)]
        for i in range(1, num_rows):
            border_anims.append(FadeIn(mountain_filled[i][0], scale=1.2))
            border_anims.append(FadeIn(mountain_filled[i][i], scale=1.2))
            
        self.play(LaggedStart(*border_anims, lag_ratio=0.05), run_time=1)
        
        # The inner core calculates and fills rapidly
        inner_anims = []
        for i in range(2, num_rows):
            for j in range(1, i):
                inner_anims.append(FadeIn(mountain_filled[i][j], scale=0.5))
                
        self.play(LaggedStart(*inner_anims, lag_ratio=0.05), run_time=1)
        
        # System locked flash
        self.play(mountain_filled.animate.set_opacity(1), Flash(mountain_filled.get_center(), color=COLOR_NEON_CYAN, flash_radius=4), run_time=0.8)

        # ---------------------------------------------------------
        # ACTION 3: THE Z-AXIS HOLOGRAPHIC REVEAL (Table 22.4)
        # ---------------------------------------------------------
        target_box = mountain_filled[6][1] # The '6'
        
        # Extreme close up on the '6'
        self.move_camera(phi=50 * DEGREES, focal_point=target_box.get_center(), zoom=2.5, run_time=1.5)

        # Lock-on animation (turns Orange)
        self.play(target_box.animate.set_color(COLOR_NEON_ORANGE), run_time=0.5)
        
        hud = Text("EXTRACTING 6-COMBINATION MATRIX...", font="monospace", color=COLOR_NEON_ORANGE).scale(0.15)
        hud.next_to(target_box, DOWN, buff=0.2)
        self.play(Write(hud), run_time=0.8)

        # Build Table 22.4 using the sci-fi HUD boxes (Error fixed here)
        grid_data = [
            ["G", "L", "L", "L", "L", "L"],
            ["L", "G", "L", "L", "L", "L"],
            ["L", "L", "G", "L", "L", "L"],
            ["L", "L", "L", "G", "L", "L"],
            ["L", "L", "L", "L", "G", "L"],
            ["L", "L", "L", "L", "L", "G"]
        ]
        
        table_22_4 = VGroup()
        for row in grid_data:
            row_col = COLOR_NEON_GOLD if "G" in row else COLOR_NEON_CYAN
            row_grp = VGroup(*[get_hud_box(is_empty=False, value=c, color=COLOR_NEON_ORANGE) for c in row]).arrange(RIGHT, buff=0.08)
            table_22_4.add(row_grp)
        table_22_4.arrange(DOWN, buff=0.08)
        
        # Spawning the table IN FRONT OF the mountain (Z-axis OUT)
        table_22_4.scale(0.6).move_to(mountain_filled.get_bottom() + DOWN * 2)
        table_22_4.shift(OUT * 1.5) # Lifts it off the ground into the air

        # Camera pulls back to show both layers (Mountain in back, 6x6 Grid floating in front)
        self.move_camera(phi=55 * DEGREES, focal_point=mountain_filled.get_bottom() + DOWN*0.5, zoom=1.3, run_time=2)

        # Data Projection Laser connecting the '6' to the floating grid
        projection_beam = Line(target_box.get_center(), table_22_4.get_center(), color=COLOR_NEON_ORANGE).set_stroke(width=2, opacity=0.6)
        
        self.play(Create(projection_beam), run_time=0.5)
        
        # The grid materializes out of the laser beam
        self.play(
            TransformFromCopy(target_box.copy().set_opacity(0), table_22_4),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Add a floating bounding box around the hologram
        hologram_frame = SurroundingRectangle(table_22_4, color=COLOR_NEON_ORANGE, buff=0.2, stroke_width=2).set_opacity(0.5)
        self.play(Create(hologram_frame), run_time=0.8)

        # Slow cinematic drift to end the scene
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(table_22_4.animate.shift(UP*0.1), run_time=2, rate_func=there_and_back)
        self.wait(3)