import flet as ft


POSTS = [
    {
        "id": 1,
        "title": "Building an Engineering Mechanics Calculator in MATLAB App Designer",
        "date": "June 2026",
        "category": "MATLAB",
        "category_color": "#D35400",
        "read_time": "5 min read",
        "video_path": "demo.mp4",  # ← change this to your actual filename
        "summary": "How I built a multi-panel GUI calculator in MATLAB App Designer that computes Kinetic Energy, Potential Energy, Engineering Strain, and Work Done — with a live velocity vs energy graph.",
        "sections": [
            {
                "heading": "What the App Does",
                "body": (
                    "The Engineering Mechanics Calculator is a MATLAB App Designer GUI that solves "
                    "three core mechanics problems in one interface: Energy Calculation (kinetic and "
                    "potential), Strain Calculation (engineering strain), and Work Calculation (work done "
                    "by a force at an angle). It also plots a Velocity vs Kinetic Energy graph in real time."
                ),
            },
            {
                "heading": "Energy Calculation — Kinetic and Potential Energy",
                "body": (
                    "Kinetic Energy is the energy an object has due to its motion. "
                    "The formula used in the app is:\n\n"
                    "    KE = 0.5 x m x v^2\n\n"
                    "Where m is mass in kilograms and v is velocity in metres per second. "
                    "Potential Energy is the energy stored due to an object height:\n\n"
                    "    PE = m x g x h\n\n"
                    "The app supports three gravity values: "
                    "Earth (9.81 m/s2), Moon (1.62 m/s2), and Mars (3.71 m/s2)."
                ),
            },
            {
                "heading": "Strain Calculation — Engineering Strain",
                "body": (
                    "Engineering strain measures how much a material deforms relative to its original length. "
                    "It is a dimensionless ratio:\n\n"
                    "    e = dL / L0\n\n"
                    "Where dL is the change in length and L0 is the original length in metres. "
                    "This is a fundamental concept in Metallurgical Engineering."
                ),
            },
            {
                "heading": "Work Calculation — Work Done by a Force",
                "body": (
                    "Work is done when a force moves an object over a distance at an angle:\n\n"
                    "    W = F x d x cos(angle)\n\n"
                    "The MATLAB function cosd() accepts degrees directly, "
                    "avoiding manual conversion to radians."
                ),
            },
            {
                "heading": "The Plot Button — Visualising Kinetic Energy",
                "body": (
                    "The Plot button uses linspace() to generate 100 velocity values "
                    "then plots KE = 0.5 x m x v^2 on UIAxes. This shows how kinetic energy "
                    "grows quadratically with velocity — doubling speed quadruples energy."
                ),
            },
            {
                "heading": "What I Learned",
                "body": (
                    "Building this app taught me how MATLAB App Designer separates UI definition "
                    "(createComponents) from event logic (callbacks). I learned the importance "
                    "of input validation — checking values are greater than zero before "
                    "calculating prevents division by zero errors."
                ),
            },
        ],
        "formulas": [
            ("Kinetic Energy",     "KE = 0.5 x m x v^2"),
            ("Potential Energy",   "PE = m x g x h"),
            ("Engineering Strain", "e  = dL / L0"),
            ("Work Done",          "W  = F x d x cos(angle)"),
        ],
    },
]


def build_formula_card(label, formula):
    return ft.Container(
        padding=ft.Padding(left=16, top=12, right=16, bottom=12),
        border_radius=8,
        bgcolor="#FEF3E2",
        border=ft.Border(
            left=ft.BorderSide(3, "#D35400"),
            top=ft.BorderSide(1, "#F5CBA7"),
            right=ft.BorderSide(1, "#F5CBA7"),
            bottom=ft.BorderSide(1, "#F5CBA7"),
        ),
        content=ft.Column(
            spacing=4,
            controls=[
                ft.Text(label, size=11, color="#92400E", weight=ft.FontWeight.W_700),
                ft.Text(formula, size=15, color="#1A1A1A", weight=ft.FontWeight.W_800),
            ],
        ),
    )


def build_video_player(path):
    return ft.Container(
        border_radius=10,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Video(
            playlist=[ft.VideoMedia(path)],
            playlist_mode=ft.PlaylistMode.NONE,
            width=600,
            height=340,
            autoplay=False,
            show_controls=True,
        ),
    )


def build_list_view(on_read):
    post_cards = []
    for p in POSTS:
        post_cards.append(
            ft.Container(
                padding=ft.Padding(left=24, top=24, right=24, bottom=24),
                border_radius=12,
                bgcolor="#FFFFFF",
                border=ft.Border(
                    left=ft.BorderSide(1, "#E2E8F0"),
                    top=ft.BorderSide(1, "#E2E8F0"),
                    right=ft.BorderSide(1, "#E2E8F0"),
                    bottom=ft.BorderSide(1, "#E2E8F0"),
                ),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=8,
                    color="#1A1A1A0D",
                    offset=ft.Offset(0, 2),
                ),
                content=ft.Column(
                    spacing=12,
                    controls=[
                        ft.Row(
                            spacing=8,
                            controls=[
                                ft.Container(
                                    padding=ft.Padding(left=10, top=4, right=10, bottom=4),
                                    border_radius=20,
                                    bgcolor=p["category_color"] + "20",
                                    content=ft.Text(
                                        p["category"],
                                        size=11,
                                        weight=ft.FontWeight.W_700,
                                        color=p["category_color"],
                                    ),
                                ),
                                ft.Text(p["date"], size=12, color="#94A3B8"),
                                ft.Text("·", size=12, color="#94A3B8"),
                                ft.Text(p["read_time"], size=12, color="#94A3B8"),
                            ],
                        ),
                        ft.Text(p["title"], size=18, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                        ft.Text(p["summary"], size=14, color="#475569"),
                        ft.Container(
                            padding=ft.Padding(left=16, top=10, right=16, bottom=10),
                            border_radius=8,
                            bgcolor="#D35400",
                            on_click=lambda e, post=p: on_read(post),
                            content=ft.Text("Read Post", size=13, color="#FFFFFF", weight=ft.FontWeight.W_700),
                        ),
                    ],
                ),
            )
        )

    return ft.Container(
        padding=ft.Padding(left=32, top=32, right=32, bottom=32),
        content=ft.Column(
            spacing=24,
            controls=[
                ft.Text("Technical Blog", size=30, weight=ft.FontWeight.BOLD, color="#1A1A1A"),
                ft.Text("Confidence in Concepts — Johannes Martin · 225047403", size=14, color="#64748B"),
                ft.Text("Written technical explanations of core programming and engineering concepts.", size=13, color="#94A3B8"),
                ft.Divider(height=1, color="#E2E8F0"),
                ft.Column(spacing=16, controls=post_cards),
            ],
        ),
    )


def build_detail_view(post, on_back):
    section_controls = []
    for section in post["sections"]:
        section_controls.append(
            ft.Column(
                spacing=8,
                controls=[
                    ft.Text(section["heading"], size=16, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                    ft.Text(section["body"], size=14, color="#475569"),
                    ft.Divider(height=1, color="#F1F5F9"),
                ],
            )
        )

    return ft.Container(
        padding=ft.Padding(left=32, top=32, right=32, bottom=32),
        content=ft.Column(
            spacing=24,
            controls=[
                ft.Container(
                    on_click=lambda e: on_back(),
                    content=ft.Row(
                        spacing=6,
                        controls=[
                            ft.Icon(ft.Icons.ARROW_BACK, color="#D35400", size=18),
                            ft.Text("Back to Blog", size=13, color="#D35400", weight=ft.FontWeight.W_600),
                        ],
                    ),
                ),
                ft.Container(
                    padding=ft.Padding(left=24, top=24, right=24, bottom=24),
                    border_radius=12,
                    bgcolor="#FFFFFF",
                    border=ft.Border(
                        left=ft.BorderSide(1, "#E2E8F0"),
                        top=ft.BorderSide(1, "#E2E8F0"),
                        right=ft.BorderSide(1, "#E2E8F0"),
                        bottom=ft.BorderSide(1, "#E2E8F0"),
                    ),
                    content=ft.Column(
                        spacing=16,
                        controls=[
                            ft.Row(
                                spacing=8,
                                controls=[
                                    ft.Container(
                                        padding=ft.Padding(left=10, top=4, right=10, bottom=4),
                                        border_radius=20,
                                        bgcolor=post["category_color"] + "20",
                                        content=ft.Text(
                                            post["category"],
                                            size=11,
                                            weight=ft.FontWeight.W_700,
                                            color=post["category_color"],
                                        ),
                                    ),
                                    ft.Text(post["date"], size=12, color="#94A3B8"),
                                    ft.Text("·", size=12, color="#94A3B8"),
                                    ft.Text(post["read_time"], size=12, color="#94A3B8"),
                                ],
                            ),
                            ft.Text(post["title"], size=22, weight=ft.FontWeight.W_900, color="#1A1A1A"),
                            ft.Divider(height=1, color="#F1F5F9"),

                            # ── Video Section ──────────────────────────────
                            ft.Text("Demo Video", size=16, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                            build_video_player(post["video_path"]),
                            ft.Divider(height=1, color="#F1F5F9"),
                            # ───────────────────────────────────────────────

                            ft.Text("Key Formulas", size=16, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                            ft.Column(
                                spacing=10,
                                controls=[build_formula_card(l, f) for l, f in post["formulas"]],
                            ),
                            ft.Divider(height=1, color="#F1F5F9"),
                            *section_controls,
                        ],
                    ),
                ),
            ],
        ),
    )


def blog_page(parent_content=None):
    list_view = build_list_view(lambda post: show_detail(post))

    def show_detail(post):
        if parent_content:
            parent_content.controls.clear()
            parent_content.controls.append(build_detail_view(post, show_list_again))
            parent_content.update()

    def show_list_again():
        if parent_content:
            parent_content.controls.clear()
            parent_content.controls.append(blog_page(parent_content))
            parent_content.update()

    return list_view