import flet as ft

def main(page: ft.Page):
    page.title = "My IP"
    page.window.width = 425
    page.window.height = 275
    page.window.resizable = False
    page.add(ft.Text(""))

ft.app(target=main)