# src/screens/login_screen.py
import flet as ft
import requests
from components.buttons import PrimaryButton
from components.inputs import AppTextField

def LoginScreen(page: ft.Page):

    print("[INFO] LoginScreen")

    baseUrl = "https://0e73cfd5-6b5f-4082-9c37-514cf7941cc1.mock.pstmn.io"
    LOGIN_API = f"{baseUrl}/login" 

    # รูปโลโก้คณะ
    siet_logo = ft.Image(src="siet_logo.png", width=150, height=150, fit=ft.ImageFit.FIT_WIDTH)
    
    # กลุ่มข้อความยืนยันตัวตน
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
    
    # ----- 2. ฟังก์ชันตรวจสอบข้อมูลและล็อกอิน -----
    def do_login(e):
        
        email = email_field.value.strip() if email_field.value else ""
        password = password_field.value.strip() if password_field.value else ""
        # 1. สร้าง "รายการตรวจเช็ค"
        fields_to_validate = [
            (email_field, "กรุณากรอกอีเมล"),
            (password_field, "กรุณากรอกรหัสผ่าน")
        ]

        has_error = False

        # 2. ลูปการตรวจสอบรายการ
        for field, error_msg in fields_to_validate:
            field.error_text = None  # ล้าง Error เก่าทิ้งก่อน
            
            # ถ้าช่องไหนไม่มีค่าหรือมีแค่ช่องว่าง
            if not field.value or not field.value.strip():
                field.error_text = error_msg
                has_error = True

        # 3. ถ้าเจอว่ามีข้อผิดพลาด (has_error = True) ให้หยุดการทำงาน
        if has_error:
            page.update()
            print(f"[ERROR]: Email: {email} กรอกอีเมลหรือรหัสผ่านไม่ครบ")
            return

        # --- ถ้าผ่านด่านทั้งหมดมาได้ แปลว่ากรอกครบถ้วน ---
        print(f"[SUCCESS] Email: {email} กรอกอีเมลและรหัสผ่านครบถ้วน")

        login_btn.content = ft.ProgressRing(width=20, height=20, color="#FFF6FE")
        login_btn.disabled = True
        page.update()

        try:
            response = requests.post(
                LOGIN_API, 
                json={"email": email, "password": password},
                headers={"x-mock-match-request-body": "true"},
                timeout=5 
            )

            if response.status_code == 200:
                print("[SUCCESS] CONNECTION SERVER: STATUS 200")
                data = response.json()
                user_data = data.get("user", {})
                print(f"[INFO] RESPONSE: {user_data}")
                
                # เก็บ Session
                page.session.set("access_token", data.get("token"))
                page.session.set("user_name", user_data.get("name", "student"))
                
                
                # เช็ค Role
                role = user_data.get("role", "student")
                page.session.set("user_role", role)
                
                # แยกหน้า
                if role == "advisor":
                    page.session.set("user_id", user_data.get("id")) 
                    print(f"[SUCCESS] LOGIN BY ADVISOR: {email}")
                    page.go("/advisor_home") 
                else:
                    page.session.set("user_id", user_data.get("id")) 
                    print(f"[SUCCESS] LOGIN BY STUDENT: {email}")
                    page.go("/student_home") 

            else:
                print("[ERROR] Not Found: อีเมลหรือรหัสผ่านไม่ถูกต้อง")
                

        except Exception as ex:
            print(f"[ERROR] CONNETION SERVER: {ex}")
            
            
            
        finally:
            login_btn.content = PrimaryButton(
                "LOG IN", 
                padding=ft.padding.symmetric(horizontal=40, vertical=20),
                on_click=do_login
            )
            login_btn.disabled = False
            page.update()

    

    # ----- 3. ปุ่มล็อกอินและจัด Layout -----
    login_btn = ft.Container(
        content=PrimaryButton(
            text="LOG IN",
            on_click=do_login, # ผูกฟังก์ชันเข้ากับปุ่ม
            padding=ft.padding.symmetric(horizontal=40, vertical=20)
        )
    )
            
    # จัดกลุ่มฟิลด์และปุ่มล็อกอิน
    field_group = ft.Container(
        content=ft.Column(
            controls=[email_field, password_field, login_btn],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        margin=ft.margin.only(top=50)
    )
   
    # กล่องล็อกอิน (กล่องเทา)
    login_box = ft.Container(
        content=ft.Column(
            controls=[txt_group, field_group]
        ),
        bgcolor="#E0E0E0",
        border_radius=20,
        padding=ft.padding.only(left=30, right=30, top=30, bottom=30)
    )
    
    # กล่องสีแดง (กล่องนอกสุด)
    red_box = ft.Container(
        content=login_box,
        bgcolor="#EF3961",
        margin=ft.margin.only(top=50),
        padding=ft.padding.only(left=25, right=25, top=50, bottom=50)
    )

    # ส่งออกหน้าจอ Login
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