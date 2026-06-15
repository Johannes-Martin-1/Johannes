import flet as ft


def about_page():
    return ft.Container(
        expand=True,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                ft.Text(
                    "About Me",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color="#0F172A",
                ),

                ft.Container(height=10),

                ft.CircleAvatar(
                    foreground_image_src="profile.jpg",  # put image in assets folder
                    radius=80,
                ),

                ft.Container(height=20),

                ft.Text(
                    "Johannes Martin",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Engineering Student | Python Developer | MATLAB Learner",
                    size=16,
                    color="#64748B",
                ),

                ft.Container(height=20),

                ft.Container(
                    width=800,
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    shadow=ft.BoxShadow(
                        blur_radius=15,
                        spread_radius=1,
                        offset=ft.Offset(0, 3),
                    ),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Biography",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Text(
                                """
I am an Engineering student passionate about programming,
engineering problem solving, MATLAB, Python development,
and software design.

This portfolio showcases my project contributions,
MATLAB certifications, technical blog posts, and GitHub
activity throughout the semester.

My goal is to combine engineering knowledge with software
development to build practical solutions for real-world
problems.
                                """,
                                size=16,
                            ),
                        ]
                    ),
                ),

                ft.Container(height=20),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        stat_card("Projects", "10+"),
                        stat_card("MATLAB Courses", "7"),
                        stat_card("Blog Articles", "15+"),
                    ],
                ),

                ft.Container(height=20),

                ft.Container(
                    width=800,
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Skills",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Chip(label=ft.Text("Python")),
                            ft.Chip(label=ft.Text("MATLAB")),
                            ft.Chip(label=ft.Text("Flet")),
                            ft.Chip(label=ft.Text("GitHub")),
                            ft.Chip(label=ft.Text("Engineering Mechanics")),
                            ft.Chip(label=ft.Text("Problem Solving")),
                        ]
                    ),
                ),

                ft.Container(height=20),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.EMAIL),
                        ft.Text("johannesngenokesho615martin@gmail.com"),

                        ft.VerticalDivider(),

                        ft.Icon(ft.Icons.CODE),
                        ft.Text("Johannes-Martin-1"),
                    ],
                ),

                ft.Container(height=50),
            ],
        ),
    )


def stat_card(title, value):
    return ft.Container(
        width=180,
        padding=15,
        margin=10,
        bgcolor="white",
        border_radius=15,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value,
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#2563EB",
                ),
                ft.Text(title),
            ],
        ),
    )