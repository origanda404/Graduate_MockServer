# src/screens/login_screen.py
import flet as ft
import requests
from components.buttons import PrimaryButton
from components.inputs import AppTextField

# LoginScreen(page) --> main.py
def LoginScreen(page: ft.Page):
    
    # ----- func login -----
    def do_login(e):
        pass


    # ----- UI LoginScreen -----
    # กำหนดตัวแปร widget ที่ใช้ในหน้าจอ Login
    #รูปโลโก้คณะ
    siet_logo = ft.Container(
        content=ft.Image(src="siet_logo.png"),
        margin=ft.margin.only(bottom=30) # ปรับระยะห่างด้านล่างของโลโก้
    )
    # กลุ่มข้อความยืนยันตัวตนและคำอธิบาย
    txt_group = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", size=16, weight=ft.FontWeight.BOLD, color="#000000"),
                ft.Text("โดยใช้ E-mail Account ของสถาบันฯ", color="#000000"),
            ]
        )
    )

    # ฟิลด์สำหรับกรอกอีเมลและรหัสผ่าน
    email_field = AppTextField(label="E-mail Account")
    password_field = AppTextField(label="Password", is_password=True)
    
    # ปุ่มล็อกอิน (ยังไม่ทำงาน)
    login_btn = ft.Container(
        content=PrimaryButton(
            text="LOG IN",
            on_click=lambda e: print("Login button clicked!"), # Placeholder for login action
            padding=ft.padding.symmetric(horizontal=40, vertical=20)
        ),
        margin=ft.margin.only(top=30) # ปรับระยะห่างด้านบนของปุ่มล็อกอิน
    )
    
    # จัดกลุ่มฟิลด์และปุ่มล็อกอินเข้าด้วยกัน
    field_group = ft.Container(
        content=ft.Column(
            controls=[email_field, password_field, login_btn],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        margin=ft.margin.only(top=50)
    )
   
    # กล่องล็อกอิน
    login_box = ft.Container(
        content=ft.Column(
            controls=[txt_group, field_group]
        ),
        bgcolor="#E0E0E0",
        border_radius=20,
        margin=ft.margin.only(left=25, right=25,top=50, bottom=50),
        padding=ft.padding.only(left=30, right=30, top=30, bottom=100) # ปรับระยะห่างภายในกล่องล็อกอิน
    )
    
    # กล่องสีแดง
    red_box = ft.Container(
        content=login_box,
        bgcolor="#EF3961"
    )
    
    # แสดงหน้าจอ Login
    return ft.View(
        route="/login",
        bgcolor="#FFF6FE",
        appbar=ft.AppBar(
            title=ft.Text("KMITL"), 
            center_title=True,
            color="#FFF6FE", 
            bgcolor="#EF3961"
        ),
        controls=[
            siet_logo,
            red_box    
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.END,
        padding=0
    )