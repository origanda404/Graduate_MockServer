import flet as ft

def StudentHome(page: ft.Page):

    return ft.View(
        route="/student_home",
        controls=[
            ft.Text("HOME STUDENT", color="#000000")
        ]
    )