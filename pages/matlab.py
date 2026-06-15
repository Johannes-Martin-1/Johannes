import flet as ft


def certificate_card(title, image_file):
    return ft.Card(
        elevation=8,
        content=ft.Container(
            width=350,
            padding=15,
            border_radius=15,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[

                    ft.Image(
                        src=image_file,
                        height=220,
                    ),

                    ft.Divider(),

                    ft.Text(
                        title,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    ft.Text(
                        "Completed",
                        color="green",
                        size=14,
                    ),
                ],
            ),
        ),
    )


def matlab_page():

    return ft.Container(
        expand=True,
        padding=30,

        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Text(
                    "MATLAB ACHIEVEMENT HUB",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color="#1E40AF",
                ),

                ft.Text(
                    "MathWorks Certifications and Professional Development",
                    size=18,
                    color="grey",
                ),

                ft.Divider(),

                ft.Container(
                    padding=20,
                    border_radius=15,
                    bgcolor="#EFF6FF",

                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Overview",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Text(
                                "This section showcases MATLAB and Simulink "
                                "certifications completed through MathWorks. "
                                "These demonstrate programming, data analysis, "
                                "and engineering problem-solving skills."
                            ),
                        ]
                    ),
                ),

                ft.Container(height=20),

                ft.ResponsiveRow(
    controls=[

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "MATLAB Onramp",
                "MATLAB Onramp.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "Simulink Onramp",
                "Simulink Onramp.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "Machine Learning Onramp",
                "Machine Learning Onramp.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "Make and Manipulate Matrices",
                "Make and Manipulate Matrices.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "Explore Data with MATLAB Plots",
                "Explore Data with MATLAB Plots.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "Calculations with Vectors and Matrices",
                "Calculations with Vectors and Matrices.png"
            ),
        ),

        ft.Container(
            col={"sm": 12, "md": 6, "xl": 4},
            content=certificate_card(
                "MATLAB Desktop Tools and Troubleshooting Scripts",
                "MATLAB Desktop Tools and Troubleshooting Scripts.png"
            ),
        ),

    ]
),

                ft.Container(height=20),

                ft.Card(
                    content=ft.Container(
                        padding=20,

                        content=ft.Column(
                            controls=[

                                ft.Text(
                                    "Skills Developed",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Text("• MATLAB Programming"),
                                ft.Text("• Data Analysis"),
                                ft.Text("• Engineering Computation"),
                                ft.Text("• Simulation and Modelling"),
                                ft.Text("• Machine Learning Fundamentals"),
                                ft.Text("• Matrix Operations"),
                                ft.Text("• Problem Solving"),
                            ]
                        ),
                    )
                ),
            ],
        ),
    )