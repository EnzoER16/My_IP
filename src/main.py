from src.get_ip import get_ip
import flet as ft

def main(page: ft.Page):
    page.title = "My IP"

    # window properties
    page.window.width = 425
    page.window.height = 275
    page.window.resizable = False
    page.window.maximizable = False
    page.window.left = 560 # center x position for a 1920 value
    page.window.top = 240 # center y position for a 1080 value

    # window icon
    page.window.icon = "src/assets/icon.ico"

    # window alignment
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # add text to page
    page.add(ft.Text(f"IP: {get_ip()}", size=30, weight=ft.FontWeight.BOLD))

ft.app(target=main)