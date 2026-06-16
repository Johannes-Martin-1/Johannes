import os
import flet as ft

from pages.home import home_page
from pages.timeline import timeline_page
from pages.matlab import matlab_page
from pages.blog import blog_page
from pages.github import github_page
from pages.about import about_page


def main(page: ft.Page):
    page.title = "Engineering Portfolio"
    page.assets_dir = "assets"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F1F5F9"
    page.padding = 0
    page.window_width = 1400
    page.window_height = 900

    content = ft.Column(expand=True, scroll=ft.ScrollMode.ADAPTIVE)

    def load_blog():
        content.controls.clear()
        content.controls.append(blog_page(content))
        page.update()

    def change_page(e):
        idx = e.control.selected_index
        content.controls.clear()

        if idx == 0:
            content.controls.append(home_page())
        elif idx == 1:
            content.controls.append(timeline_page())
        elif idx == 2:
            content.controls.append(matlab_page())
        elif idx == 3:
            load_blog()
            return
        elif idx == 4:
            content.controls.append(github_page())
        elif idx == 5:
            content.controls.append(about_page())

        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.TIMELINE, label="Timeline"),
            ft.NavigationRailDestination(icon=ft.Icons.SCHOOL, label="MATLAB"),
            ft.NavigationRailDestination(icon=ft.Icons.ARTICLE, label="Blog"),
            ft.NavigationRailDestination(icon=ft.Icons.CODE, label="GitHub"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="About"),
        ],
        on_change=change_page,
    )

    content.controls.append(home_page())

    page.add(
        ft.Row(
            [
                nav,
                ft.VerticalDivider(width=1, color="#cbd5e1"),
                ft.Container(content=content, expand=True, padding=20),
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    # Pull the port dynamically from Render, default to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    
    # Run Flet in web server mode so Render can route live traffic to it
    ft.app(
        target=main, 
        view=ft.AppView.WEB_BROWSER, 
        port=port, 
        host="0.0.0.0"
    )