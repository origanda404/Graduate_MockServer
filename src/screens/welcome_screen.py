# src/welcome_screen.py
import flet as ft
from components.buttons import PrimaryButton

def WelcomeScreen(page: ft.Page):

    # กำหนดตัวแปรต่างๆ ที่ใช้ในหน้าจอ Welcome
    # โลโก้ข้อความ
    text_logo = ft.Container(
        content=ft.Image(src="text_logo.png"),
        margin=ft.margin.symmetric(horizontal=20) # ปรับระยะห่างด้านข้างของโลโก้ข้อความ
    )
    welcome_btn = PrimaryButton(
        text="WELCOME",
        on_click=lambda e: page.go("/login"),
        padding=ft.padding.symmetric(horizontal=30, vertical=20)
    )
    # จัดกลุ่มโลโก้และปุ่ม WELCOME เข้าด้วยกัน
    welcome_layout = ft.Container(
        content=ft.Column(
            controls=[
                text_logo,
                welcome_btn   
            ],
            spacing=150,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        margin=ft.margin.only(bottom=100)
    )
    # ข้อความด้านล่างของหน้าจอ Welcome
    welcome_txt = ft.Container(
        content=ft.Text("Graduate Student Tracking System", color="#EF3961", size=18),
        margin=ft.margin.only(bottom=50)
    )
    # return หน้าจอ Welcome
    return ft.View(
        route="/",
        bgcolor="#FFF6FE",
        vertical_alignment=ft.MainAxisAlignment.END,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            welcome_layout,  
            welcome_txt
        ]
    )
