import flet as ft


WEEKS = [
    {
        "week": 1,
        "dates": "02 – 06 Mar 2026",
        "phase": "Phase 0",
        "phase_color": "#6366F1",
        "title": "Group Formation & Environment Setup",
        "status": "completed",
        "contributions": [
            "Joined Group 11 and confirmed role assignment",
            "Installed Node.js 18 LTS, Expo CLI, and VS Code with React Native Tools",
            "Installed Expo Go on personal Android device and tested with npx expo start",
            "Created a free Expo account at expo.dev",
            "Confirmed GitHub access to: UNAM-I3691CP-PixelPebble-OreGuide",
        ],
    },
    {
        "week": 2,
        "dates": "09 – 13 Mar 2026",
        "phase": "Phase 0",
        "phase_color": "#6366F1",
        "title": "Idea Brainstorming & Firebase Setup",
        "status": "completed",
        "contributions": [
            "Participated in internal brainstorming sessions for three pitch ideas",
            "Contributed to the OreGuide concept: AI-powered mineral identification",
            "Set up Firebase project configuration and tested Authentication initialization",
            "Committed initial folder structure to GitHub repository",
            "Verified Expo Go hot-reload working on personal device",
        ],
    },
    {
        "week": 3,
        "dates": "16 – 20 Mar 2026",
        "phase": "Phase 1",
        "phase_color": "#F59E0B",
        "title": "Pitch Week — Preparation & Presentation",
        "status": "completed",
        "contributions": [
            "Co-prepared the OreGuide pitch deck covering problem, users, and core features",
            "Presented Group 11's three app ideas to Mr. Mathew Abisai at JEDS Campus",
            "Contributed to the Firebase feasibility discussion during Q&A",
            "OreGuide (Metallurgical domain) was selected and officially registered",
            "Signed the Idea Registration Form confirming domain and feature set",
        ],
    },
    {
        "week": 4,
        "dates": "23 – 27 Mar 2026",
        "phase": "Phase 1",
        "phase_color": "#F59E0B",
        "title": "Post-Pitch Planning & Role Confirmation",
        "status": "completed",
        "contributions": [
            "Confirmed development role responsibilities following idea lock-in",
            "Began planning the React Native screen architecture",
            "Reviewed the signed Idea Registration Form and mapped features to FR IDs",
            "Set up initial project scaffolding using Expo Router file-based routing",
            "Committed initial app structure to GitHub with meaningful commit messages",
        ],
    },
    {
        "week": 5,
        "dates": "30 Mar – 03 Apr 2026",
        "phase": "Phase 2",
        "phase_color": "#10B981",
        "title": "SRS — Problem Statement & System Overview",
        "status": "completed",
        "contributions": [
            "Contributed to SRS Section 1: project title, group members, and roles",
            "Drafted the system description and target user profiles",
            "Defined Firebase data model: users/, ores/, identifications/, locations/",
            "Began writing FR-001 (user registration) and FR-002 (login/logout)",
            "Committed SRS draft sections to GitHub /docs folder",
        ],
    },
    {
        "week": 6,
        "dates": "06 – 10 Apr 2026",
        "phase": "Phase 2",
        "phase_color": "#10B981",
        "title": "SRS — Functional Requirements",
        "status": "completed",
        "contributions": [
            "Wrote functional requirements FR-001 through FR-016",
            "Defined AI inference requirements FR-AI-001 and FR-AI-002",
            "Contributed to Firestore collection schema with field types and access patterns",
            "Reviewed and gave feedback on team members SRS sections",
            "Committed updated SRS with all functional requirements to GitHub",
        ],
    },
    {
        "week": 7,
        "dates": "13 – 17 Apr 2026",
        "phase": "Phase 2",
        "phase_color": "#10B981",
        "title": "SRS — Non-Functional Requirements & Use Cases",
        "status": "completed",
        "contributions": [
            "Authored non-functional requirements: performance, security, offline resilience",
            "Contributed to UML Use Case Diagram for ore identification and auth flows",
            "Defined API contract for the FastAPI YOLOv8 inference endpoint",
            "Reviewed Firestore security rules requiring request.auth != null",
            "Committed finalized requirements and use case diagrams to /docs",
        ],
    },
    {
        "week": 8,
        "dates": "20 – 25 Apr 2026",
        "phase": "Phase 2",
        "phase_color": "#10B981",
        "title": "SRS Final Review & Submission",
        "status": "completed",
        "contributions": [
            "Performed final review pass on the complete SRS document",
            "Ensured all 10+ functional requirements were testable and Firebase-referenced",
            "Submitted the SRS to the UNAM portal before 25 April 23:59 deadline",
            "Committed the final SRS PDF to GitHub /docs as required",
            "Verified the repository was public and accessible to Mr. Abisai",
        ],
    },
    {
        "week": 9,
        "dates": "27 Apr – 01 May 2026",
        "phase": "Phase 3",
        "phase_color": "#8B5CF6",
        "title": "Prototype — Onboarding & Auth Screens",
        "status": "completed",
        "contributions": [
            "Built the login screen (login.tsx) with email/password and Google Sign-In",
            "Set up the useAuth hook with Firebase Authentication integration",
            "Implemented the auth layout guard redirecting authenticated users to tabs",
            "Styled auth screens using a centralized THEME object (Namibian colour palette)",
            "Committed auth screens with descriptive commit messages to main branch",
        ],
    },
    {
        "week": 10,
        "dates": "04 – 08 May 2026",
        "phase": "Phase 3",
        "phase_color": "#8B5CF6",
        "title": "Prototype — Forgot Password & Firebase Config",
        "status": "completed",
        "contributions": [
            "Implemented forgot-password.tsx with Firebase sendPasswordResetEmail",
            "Built inline success confirmation state with user enumeration protection",
            "Resolved Firebase auth/invalid-api-key by configuring .env with EXPO_PUBLIC_ variables",
            "Moved style files to styles/ folder to fix Expo Router routing warnings",
            "Updated task ledger in prompt.md and committed Session 4 changes",
        ],
    },
    {
        "week": 11,
        "dates": "11 – 15 May 2026",
        "phase": "Phase 3",
        "phase_color": "#8B5CF6",
        "title": "Prototype — Remaining Screens & Testing",
        "status": "completed",
        "contributions": [
            "Completed register screen (FR-001) and persistent login (FR-016)",
            "Built services/firestore.ts data layer for ore search and favorites",
            "Fixed React.ComponentState type issue in types/ore.ts",
            "Tested full authentication flow end-to-end on physical Android device",
            "Committed all remaining screen implementations to main branch",
        ],
    },
    {
        "week": 12,
        "dates": "18 – 30 May 2026",
        "phase": "Phase 3",
        "phase_color": "#8B5CF6",
        "title": "Prototype Refinement & Submission",
        "status": "completed",
        "contributions": [
            "Refined all auth and ore identification screens based on team feedback",
            "Exported all Figma screen designs as PNG to GitHub /designs folder",
            "Submitted prototype link and design rationale to UNAM portal",
            "Presented prototype walkthrough to Mr. Abisai",
            "Committed final prototype assets and rationale document to repository",
        ],
    },
    {
        "week": 13,
        "dates": "01 – 06 Jun 2026",
        "phase": "Phase 4A",
        "phase_color": "#EF4444",
        "title": "Progress Demonstration",
        "status": "completed",
        "contributions": [
            "Presented live OreGuide app to Mr. Mathew Abisai at JEDS Campus",
            "Demonstrated Firebase Authentication: register, login, and logout working",
            "Showed AI ore identification pipeline via YOLOv8 inference on Render",
            "GitHub repository with full multi-author commit history reviewed and approved",
        ],
    },
    {
        "week": 14,
        "dates": "08 – 13 Jun 2026",
        "phase": "Phase 4B",
        "phase_color": "#DC2626",
        "title": "Final Sprint & Submission",
        "status": "in_progress",
        "contributions": [
            "Implementing all remaining feedback from the Week 13 progress demonstration",
            "Finalising all functional requirements from the SRS",
            "Building final APK via EAS Build for submission",
            "Completing the User Manual (minimum 5 pages)",
            "Final submission due: 15 June 2026 at 23:59",
        ],
    },
]

STATUS_CONFIG = {
    "completed":   {"icon": ft.Icons.CHECK_CIRCLE,           "color": "#10B981", "label": "Completed"},
    "in_progress": {"icon": ft.Icons.TIMELAPSE,              "color": "#F59E0B", "label": "In Progress"},
    "pending":     {"icon": ft.Icons.RADIO_BUTTON_UNCHECKED, "color": "#94A3B8", "label": "Pending"},
}


def build_week_card(week_data):
    status = week_data["status"]
    cfg = STATUS_CONFIG[status]

    bullet_color = "#D35400" if status == "completed" else "#F59E0B" if status == "in_progress" else "#94A3B8"
    text_color   = "#475569" if status != "pending" else "#94A3B8"

    bullet_controls = []
    for point in week_data["contributions"]:
        bullet_controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        width=6,
                        height=6,
                        border_radius=3,
                        bgcolor=bullet_color,
                        margin=ft.Margin(left=0, top=7, right=6, bottom=0),
                    ),
                    ft.Text(
                        point,
                        size=13,
                        color=text_color,
                        expand=True,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
        )

    border_color = "#D35400" if status == "in_progress" else "#E2E8F0"
    border_width = 1.5 if status == "in_progress" else 1.0

    return ft.Container(
        padding=ft.Padding(left=20, top=20, right=20, bottom=20),
        border_radius=12,
        bgcolor="#FFFFFF",
        border=ft.Border(
            left=ft.BorderSide(border_width, border_color),
            top=ft.BorderSide(border_width, border_color),
            right=ft.BorderSide(border_width, border_color),
            bottom=ft.BorderSide(border_width, border_color),
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
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Container(
                                    padding=ft.Padding(left=10, top=4, right=10, bottom=4),
                                    border_radius=20,
                                    bgcolor=week_data["phase_color"] + "20",
                                    content=ft.Text(
                                        week_data["phase"],
                                        size=11,
                                        weight=ft.FontWeight.W_700,
                                        color=week_data["phase_color"],
                                    ),
                                ),
                                ft.Text(
                                    week_data["dates"],
                                    size=12,
                                    color="#94A3B8",
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=4,
                            controls=[
                                ft.Icon(cfg["icon"], color=cfg["color"], size=16),
                                ft.Text(
                                    cfg["label"],
                                    size=12,
                                    color=cfg["color"],
                                    weight=ft.FontWeight.W_600,
                                ),
                            ],
                        ),
                    ],
                ),
                ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=40,
                            height=40,
                            border_radius=8,
                            bgcolor="#FEF3E2",
                            alignment=ft.Alignment(0, 0),
                            content=ft.Text(
                                f"W{week_data['week']}",
                                size=13,
                                weight=ft.FontWeight.W_800,
                                color="#D35400",
                            ),
                        ),
                        ft.Text(
                            week_data["title"],
                            size=15,
                            weight=ft.FontWeight.W_700,
                            color="#1A1A1A",
                            expand=True,
                        ),
                    ],
                ),
                ft.Divider(height=1, color="#F1F5F9"),
                ft.Column(spacing=6, controls=bullet_controls),
            ],
        ),
    )


def timeline_page():
    completed   = sum(1 for w in WEEKS if w["status"] == "completed")
    in_progress = sum(1 for w in WEEKS if w["status"] == "in_progress")
    pending     = sum(1 for w in WEEKS if w["status"] == "pending")

    def stat_chip(label, value, color):
        return ft.Container(
            padding=ft.Padding(left=16, top=10, right=16, bottom=10),
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

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                padding=ft.Padding(left=32, top=32, right=32, bottom=32),
                content=ft.Column(
                    spacing=24,
                    controls=[
                        ft.Text(
                            "Project Timeline",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color="#1A1A1A",
                        ),
                        ft.Text(
                            "Johannes Martin  |  225047403  |  Group 11 — OreGuide Namibia",
                            size=14,
                            color="#64748B",
                        ),
                        ft.Text(
                            "14-Week Semester: 02 March 2026 — 13 June 2026  |  Lecturer: Mr. Mathew Abisai",
                            size=13,
                            color="#94A3B8",
                        ),
                        ft.Row(
                            spacing=12,
                            controls=[
                                stat_chip("Completed",   completed,   "#10B981"),
                                stat_chip("In Progress", in_progress, "#F59E0B"),
                                stat_chip("Pending",     pending,     "#94A3B8"),
                                stat_chip("Total Weeks", len(WEEKS),  "#D35400"),
                            ],
                        ),
                        ft.Divider(height=1, color="#E2E8F0"),
                        ft.Column(
                            spacing=16,
                            controls=[build_week_card(w) for w in WEEKS],
                        ),
                    ],
                ),
            )
        ],
    )