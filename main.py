import flet as ft

def main(page: ft.Page):
    page.title = "My IP"
    page.window.width = 425
    page.window.height = 275
    page.window.resizable = False
    page.window.maximizable = False
    page.window.left = 560 # center x position for a 1920 value
    page.window.top = 240 # center y position for a 1080 value
    page.add(ft.Text(""))

ft.app(target=main)