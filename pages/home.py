import flet as ft

def home_page():

    return ft.Container(
        expand=True,
        padding=30,

        gradient=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
            colors=[
                "#0F172A",
                "#1E3A8A",
            ],
        ),

        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[

                ft.Container(
                    padding=30,
                    border_radius=20,
                    bgcolor="#2563EB",

                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[

                            # ── PROFILE PICTURE ──
                            ft.Container(
    content=ft.Image(
        src="profile.jpg",
        width=140,
        height=140,
        fit="cover",
    ),
    border_radius=70,        # ← just a number
    border=ft.Border.all(4, "white"),
    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    shadow=ft.BoxShadow(
        blur_radius=20,
        color="#00000066",
        offset=ft.Offset(0, 6),
    ),
),

                            ft.Container(height=12),

                            ft.Text(
                                "ENGINEERING PORTFOLIO",
                                size=50,
                                weight=ft.FontWeight.BOLD,
                                color="white",
                                text_align=ft.TextAlign.CENTER,
                            ),

                            ft.Text(
                                "Computer Programming I",
                                size=24,
                                color="white",
                                text_align=ft.TextAlign.CENTER,
                            ),

                            ft.Divider(color="white"),

                            ft.Text(
                                "Welcome to my portfolio. Here you can explore my engineering projects, MATLAB achievements, technical blogs, and GitHub contributions.",
                                size=16,
                                color="white",
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                    ),
                ),

                ft.Container(height=20),

                ft.Row(
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[

                        ft.Card(
                            content=ft.Container(
                                width=300,
                                padding=20,
                                content=ft.Column(
                                    [
                                        ft.Icon(ft.Icons.PERSON, size=50, color="blue"),
                                        ft.Text("Student Information", size=22, weight=ft.FontWeight.BOLD),
                                        ft.Text("Name: Johannes N Martin"),
                                        ft.Text("Student Number: 225047403"),
                                        ft.Text("Mechanical Engineering"),
                                    ]
                                ),
                            )
                        ),

                        ft.Card(
                            content=ft.Container(
                                width=300,
                                padding=20,
                                content=ft.Column(
                                    [
                                        ft.Icon(ft.Icons.ENGINEERING, size=50, color="green"),
                                        ft.Text("Portfolio Goals", size=22, weight=ft.FontWeight.BOLD),
                                        ft.Text("✔ Project Contributions"),
                                        ft.Text("✔ MATLAB Certifications"),
                                        ft.Text("✔ Technical Blogs"),
                                        ft.Text("✔ GitHub Evidence"),
                                    ]
                                ),
                            )
                        ),

                        ft.Card(
                            content=ft.Container(
                                width=300,
                                padding=20,
                                content=ft.Column(
                                    [
                                        ft.Icon(ft.Icons.CODE, size=50, color="orange"),
                                        ft.Text("Skills", size=22, weight=ft.FontWeight.BOLD),
                                        ft.Text("Python"),
                                        ft.Text("MATLAB"),
                                        ft.Text("GitHub"),
                                        ft.Text("Engineering Analysis"),
                                    ]
                                ),
                            )
                        ),
                    ],
                ),

                ft.Container(height=20),

                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Column(
                            [
                                ft.Text("About This Portfolio", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "This portfolio demonstrates my programming, engineering, MATLAB and GitHub skills developed throughout the semester."
                                ),
                            ]
                        ),
                    )
                ),
            ],
        ),
    )