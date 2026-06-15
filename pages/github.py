import flet as ft


COMMITS = [
    {
        "hash": "9a91ca5",
        "message": "Added forgot password flow and fix Firebase configuration",
        "description": "Added forgot-password.tsx screen with email input and success state. Added forgot-password.styles.ts. Wired Forgot Password link in login.tsx to new screen. Created .env file with Firebase credentials. Fixed Firebase auth/invalid-api-key error.",
        "files_changed": 14,
        "additions": 801,
        "deletions": 248,
        "date": "6 days ago",
        "branch": "Ngennor_1",
    },
    {
        "hash": "3e25d42",
        "message": "Updated prompt.md",
        "description": "Updated the living prompt.md coordination document. Updated Task Ledger to reflect Session 4 completion — forgot password flow done, Firebase configured, style files relocated to styles/ folder. Updated File State Map for team handoff.",
        "files_changed": 1,
        "additions": 85,
        "deletions": 70,
        "date": "6 days ago",
        "branch": "Ngennor_1",
    },
]

FIGMA_SCREENS = [
    "Password Reset", "Verify", "Forgot Password", "Login", "Sign Up",
    "Welcome", "Home", "Scan", "Map", "Search",
    "Collection", "Elements", "Saved", "Learn", "General", "Mine",
]

CONTRIBUTIONS = [
    {
        "icon": ft.Icons.LOCK,
        "title": "Forgot Password Flow",
        "description": "Built the complete forgot password screen (forgot-password.tsx) with Firebase sendPasswordResetEmail integration, inline success confirmation, and user enumeration protection.",
        "files": ["app/(auth)/forgot-password.tsx", "styles/forgot-password.styles.ts", "app/(auth)/login.tsx"],
    },
    {
        "icon": ft.Icons.SETTINGS,
        "title": "Firebase Configuration Fix",
        "description": "Diagnosed and resolved the auth/invalid-api-key crash by creating a .env file with EXPO_PUBLIC_ environment variables. Fixed Expo Router warnings by relocating style files to styles/ folder.",
        "files": [".env", "styles/login.styles.ts", "styles/explore.styles.ts", "styles/index.styles.ts"],
    },
    {
        "icon": ft.Icons.DESCRIPTION,
        "title": "Project Documentation",
        "description": "Maintained the living prompt.md document across sessions, updating the Task Ledger with completed features, file state map, and session notes to coordinate the 15-member team.",
        "files": ["prompt.md"],
    },
    {
        "icon": ft.Icons.DESIGN_SERVICES,
        "title": "Figma UI/UX Design",
        "description": "Co-designed the full OreGuide Namibia prototype in Figma covering 16 screens across authentication, core features, and utility flows. Used an orange and black color scheme targeting Android Compact dimensions. Linked all screens across 3 prototype flows (Flow 1, Flow 2, Flow 3) to demonstrate complete end-to-end user journeys from App Launch through Login, Home, Scan, Map, Search, Collection, Elements, Saved, Learn, and Mine screens.",
        "files": ["Figma: UI Design — 17 components", "Figma: Flow 1, Flow 2, Flow 3 prototype links"],
    },
]


def build_stat_chip(label, value, color):
    return ft.Container(
        padding=ft.Padding(left=16, top=12, right=16, bottom=12),
        border_radius=10,
        bgcolor=color + "15",
        border=ft.Border(
            left=ft.BorderSide(1, color + "40"),
            top=ft.BorderSide(1, color + "40"),
            right=ft.BorderSide(1, color + "40"),
            bottom=ft.BorderSide(1, color + "40"),
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
            controls=[
                ft.Text(str(value), size=22, weight=ft.FontWeight.W_800, color=color),
                ft.Text(label, size=11, color="#64748B", weight=ft.FontWeight.W_500),
            ],
        ),
    )


def build_commit_card(commit):
    return ft.Container(
        padding=ft.Padding(left=20, top=20, right=20, bottom=20),
        border_radius=12,
        bgcolor="#FFFFFF",
        border=ft.Border(
            left=ft.BorderSide(3, "#D35400"),
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
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=8,
                            controls=[
                                ft.Container(
                                    padding=ft.Padding(left=8, top=3, right=8, bottom=3),
                                    border_radius=6,
                                    bgcolor="#1A1A1A",
                                    content=ft.Text(
                                        commit["hash"],
                                        size=11,
                                        color="#FFFFFF",
                                        font_family="Courier New",
                                        weight=ft.FontWeight.W_700,
                                    ),
                                ),
                                ft.Container(
                                    padding=ft.Padding(left=8, top=3, right=8, bottom=3),
                                    border_radius=6,
                                    bgcolor="#6366F120",
                                    content=ft.Text(
                                        commit["branch"],
                                        size=11,
                                        color="#6366F1",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                            ],
                        ),
                        ft.Text(commit["date"], size=12, color="#94A3B8"),
                    ],
                ),
                ft.Text(
                    commit["message"],
                    size=15,
                    weight=ft.FontWeight.W_800,
                    color="#1A1A1A",
                ),
                ft.Text(
                    commit["description"],
                    size=13,
                    color="#475569",
                ),
                ft.Row(
                    spacing=16,
                    controls=[
                        ft.Row(
                            spacing=4,
                            controls=[
                                ft.Icon(ft.Icons.INSERT_DRIVE_FILE, size=14, color="#64748B"),
                                ft.Text(f"{commit['files_changed']} files changed", size=12, color="#64748B"),
                            ],
                        ),
                        ft.Row(
                            spacing=4,
                            controls=[
                                ft.Text(f"+{commit['additions']}", size=12, color="#10B981", weight=ft.FontWeight.W_700),
                                ft.Text(f"-{commit['deletions']}", size=12, color="#EF4444", weight=ft.FontWeight.W_700),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )


def build_contribution_card(item):
    file_chips = []
    for f in item["files"]:
        file_chips.append(
            ft.Container(
                padding=ft.Padding(left=8, top=3, right=8, bottom=3),
                border_radius=6,
                bgcolor="#F1F5F9",
                content=ft.Text(f, size=11, color="#475569", font_family="Courier New"),
            )
        )

    return ft.Container(
        padding=ft.Padding(left=20, top=20, right=20, bottom=20),
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
                    spacing=10,
                    controls=[
                        ft.Container(
                            width=36,
                            height=36,
                            border_radius=8,
                            bgcolor="#D3540015",
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(item["icon"], color="#D35400", size=18),
                        ),
                        ft.Text(
                            item["title"],
                            size=15,
                            weight=ft.FontWeight.W_800,
                            color="#1A1A1A",
                            expand=True,
                        ),
                    ],
                ),
                ft.Text(item["description"], size=13, color="#475569"),
                ft.Row(spacing=6, wrap=True, controls=file_chips),
            ],
        ),
    )


def build_figma_section():
    screen_chips = []
    for screen in FIGMA_SCREENS:
        screen_chips.append(
            ft.Container(
                padding=ft.Padding(left=10, top=5, right=10, bottom=5),
                border_radius=8,
                bgcolor="#FF6B0015",
                border=ft.Border(
                    left=ft.BorderSide(1, "#FF6B0040"),
                    top=ft.BorderSide(1, "#FF6B0040"),
                    right=ft.BorderSide(1, "#FF6B0040"),
                    bottom=ft.BorderSide(1, "#FF6B0040"),
                ),
                content=ft.Text(screen, size=12, color="#D35400", weight=ft.FontWeight.W_600),
            )
        )

    return ft.Container(
        padding=ft.Padding(left=20, top=20, right=20, bottom=20),
        border_radius=12,
        bgcolor="#FFFFFF",
        border=ft.Border(
            left=ft.BorderSide(3, "#D35400"),
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
            spacing=16,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Container(
                            width=36,
                            height=36,
                            border_radius=8,
                            bgcolor="#D3540015",
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(ft.Icons.DESIGN_SERVICES, color="#D35400", size=18),
                        ),
                        ft.Text(
                            "Figma UI/UX Prototype",
                            size=15,
                            weight=ft.FontWeight.W_800,
                            color="#1A1A1A",
                        ),
                    ],
                ),
                ft.Text(
                    "Co-designed the full OreGuide Namibia mobile prototype in Figma. "
                    "Designed 16 screens using an orange and black color scheme for Android Compact. "
                    "Linked all screens across 3 prototype flows covering the complete user journey "
                    "from app launch through authentication, ore scanning, mapping, and learning modules.",
                    size=13,
                    color="#475569",
                ),
                ft.Row(
                    spacing=8,
                    controls=[
                        build_stat_chip("Screens", "16", "#D35400"),
                        build_stat_chip("Flows", "3", "#6366F1"),
                        build_stat_chip("Components", "17", "#10B981"),
                    ],
                ),
                ft.Text("Screens Designed", size=13, weight=ft.FontWeight.W_700, color="#1A1A1A"),
                ft.Row(spacing=6, wrap=True, controls=screen_chips),
            ],
        ),
    )


def github_page():
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                padding=ft.Padding(left=32, top=32, right=32, bottom=32),
                content=ft.Column(
                    spacing=32,
                    controls=[

                        # ── Header ──────────────────────────────────────────
                        ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text("GitHub Evidence", size=30, weight=ft.FontWeight.BOLD, color="#1A1A1A"),
                                ft.Text("Johannes Martin  |  225047403  |  @Johannes-Martin-1", size=14, color="#64748B"),
                                ft.Text("Repository: UNAM-I3691CP-PixelPebble-OreGuide", size=13, color="#94A3B8"),
                            ],
                        ),

                        # ── Stats ────────────────────────────────────────────
                        ft.Row(
                            spacing=12,
                            controls=[
                                build_stat_chip("Commits", "2", "#D35400"),
                                build_stat_chip("Branch", "Ngennor_1", "#6366F1"),
                                build_stat_chip("Files Changed", "15", "#10B981"),
                                build_stat_chip("Lines Added", "886+", "#F59E0B"),
                            ],
                        ),

                        ft.Divider(height=1, color="#E2E8F0"),

                        # ── Commit History ───────────────────────────────────
                        ft.Column(
                            spacing=12,
                            controls=[
                                ft.Text("Commit History", size=20, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                                ft.Text(
                                    "Individual commits made to the OreGuide Namibia repository on branch Ngennor_1.",
                                    size=13,
                                    color="#64748B",
                                ),
                                *[build_commit_card(c) for c in COMMITS],
                            ],
                        ),

                        ft.Divider(height=1, color="#E2E8F0"),

                        # ── Figma Section ────────────────────────────────────
                        ft.Column(
                            spacing=12,
                            controls=[
                                ft.Text("Figma Design Contribution", size=20, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                                ft.Text(
                                    "UI/UX screens designed in Figma for the OreGuide Namibia mobile application.",
                                    size=13,
                                    color="#64748B",
                                ),
                                build_figma_section(),
                            ],
                        ),

                        ft.Divider(height=1, color="#E2E8F0"),

                        # ── Impact Summary ───────────────────────────────────
                        ft.Column(
                            spacing=12,
                            controls=[
                                ft.Text("Impact Summary", size=20, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                                ft.Container(
                                    padding=ft.Padding(left=20, top=20, right=20, bottom=20),
                                    border_radius=12,
                                    bgcolor="#FFFFFF",
                                    border=ft.Border(
                                        left=ft.BorderSide(3, "#10B981"),
                                        top=ft.BorderSide(1, "#E2E8F0"),
                                        right=ft.BorderSide(1, "#E2E8F0"),
                                        bottom=ft.BorderSide(1, "#E2E8F0"),
                                    ),
                                    content=ft.Column(
                                        spacing=12,
                                        controls=[
                                            ft.Text(
                                                "My contribution to OreGuide Namibia spanned both design and development. "
                                                "In Figma, I co-designed 16 screens covering the full user journey — "
                                                "from authentication through ore scanning, mine mapping, and the learning "
                                                "module — using an orange and black color scheme with 3 linked prototype flows.",
                                                size=14,
                                                color="#475569",
                                            ),
                                            ft.Text(
                                                "On the development side, I designed and implemented the complete forgot "
                                                "password flow using Firebase sendPasswordResetEmail, allowing field "
                                                "geologists to securely recover accounts without exposing user enumeration "
                                                "vulnerabilities.",
                                                size=14,
                                                color="#475569",
                                            ),
                                            ft.Text(
                                                "I also diagnosed and resolved a critical Firebase auth/invalid-api-key "
                                                "crash that was blocking the entire team from running the app, and "
                                                "maintained the living prompt.md coordination document to keep all "
                                                "15 team members in sync across sessions.",
                                                size=14,
                                                color="#475569",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),

                        ft.Divider(height=1, color="#E2E8F0"),

                        # ── Key Contributions ────────────────────────────────
                        ft.Column(
                            spacing=12,
                            controls=[
                                ft.Text("Key Contributions", size=20, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                                ft.Text(
                                    "Features I personally designed, built, and committed to the repository.",
                                    size=13,
                                    color="#64748B",
                                ),
                                ft.Column(
                                    spacing=12,
                                    controls=[build_contribution_card(c) for c in CONTRIBUTIONS],
                                ),
                            ],
                        ),

                        ft.Divider(height=1, color="#E2E8F0"),

                        # ── GitHub Link ──────────────────────────────────────
                        ft.Column(
                            spacing=12,
                            controls=[
                                ft.Text("Repository Link", size=20, weight=ft.FontWeight.W_800, color="#1A1A1A"),
                                ft.Container(
                                    padding=ft.Padding(left=20, top=16, right=20, bottom=16),
                                    border_radius=12,
                                    bgcolor="#FFFFFF",
                                    border=ft.Border(
                                        left=ft.BorderSide(1, "#E2E8F0"),
                                        top=ft.BorderSide(1, "#E2E8F0"),
                                        right=ft.BorderSide(1, "#E2E8F0"),
                                        bottom=ft.BorderSide(1, "#E2E8F0"),
                                    ),
                                    content=ft.Row(
                                        spacing=12,
                                        controls=[
                                            ft.Icon(ft.Icons.CODE, color="#D35400", size=24),
                                            ft.Column(
                                                spacing=2,
                                                expand=True,
                                                controls=[
                                                    ft.Text(
                                                        "UNAM-I3691CP-PixelPebble-OreGuide",
                                                        size=14,
                                                        weight=ft.FontWeight.W_700,
                                                        color="#1A1A1A",
                                                    ),
                                                    ft.Text(
                                                        "github.com/SWIF1Bl4D3/UNAM-I3691CP-PixelPebble-OreGuide",
                                                        size=12,
                                                        color="#6366F1",
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ],
    )