import flet as ft
import requests

def LoginScreen(page: ft.Page):
    # --- 1. กำหนดค่า API URL ---
    # ✅ เปลี่ยนมาใช้ Local Server ของเรา เพื่อให้ระบบแยก Role ทำงานได้
    baseUrl = "https://0e73cfd5-6b5f-4082-9c37-514cf7941cc1.mock.pstmn.io"
    LOGIN_API = f"{baseUrl}/login"

    # --- 2. UI Components ---
    logo_image = ft.Image(
        src="logo_1.jpeg", 
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(75) 
    )

    email_field = ft.TextField(
        label="E-mail Account",
        border_radius=10,
        bgcolor="white",
        border_color="transparent",
        height=50,
        text_size=14,
        color="black"
    )
    password_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        border_radius=10,
        bgcolor="white",
        border_color="transparent",
        height=50,
        text_size=14,
        color="black"
    )

    # ✅ สร้างปุ่มไว้ก่อน เพื่อให้ฟังก์ชัน do_login รู้จักตัวแปรนี้
    login_btn = ft.ElevatedButton(
        content=ft.Text("Login"),
        bgcolor="#e91e63",
        color="white",
        width=300,
        height=50,
    )
    
    # --- 3. Logic การล็อกอิน ---
    def do_login(e):
        email = email_field.value.strip()
        password = password_field.value.strip()
        
        if not email or not password:
            page.snack_bar = ft.SnackBar(ft.Text("กรุณากรอก E-mail และ Password"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        login_btn.content = ft.ProgressRing(width=20, height=20, color="white")
        login_btn.disabled = True
        page.update()

        try:
            response = requests.post(
                LOGIN_API, 
                json={"email": email, "password": password},
                timeout=5 
            )

            if response.status_code == 200:
                data = response.json()
                user_data = data.get("user", {})
                
                # เก็บ Session
                page.session.set("user_email", user_data.get("email"))
                page.session.set("user_full_name", user_data.get("full_name"))
                
                # เช็ค Role
                user_role = user_data.get("role", "student")
                page.session.set("user_role", user_role)
                
                # แยกหน้า
                if user_role == "teacher":
                    page.session.set("user_id", user_data.get("teacher_id")) 
                    print(f"✅ Teacher Login: {email}")
                    page.go("/teacher_home") 
                else:
                    page.session.set("user_id", user_data.get("student_id")) 
                    print(f"✅ Student Login: {email}")
                    page.go("/home") 

            else:
                page.snack_bar = ft.SnackBar(ft.Text("อีเมลหรือรหัสผ่านไม่ถูกต้อง"), bgcolor="red")
                page.snack_bar.open = True

        except Exception as ex:
            print(f"⚠️ Connection Error: {ex}")
            page.snack_bar = ft.SnackBar(ft.Text("ไม่สามารถเชื่อมต่อระบบได้ (อย่าลืมเปิด Local Server นะ!)"), bgcolor="orange")
            page.snack_bar.open = True
            
        finally:
            login_btn.content = ft.Text("Login")
            login_btn.disabled = False
            page.update()

    # ✅ ผูกฟังก์ชันการคลิกเข้ากับปุ่ม
    login_btn.on_click = do_login

    # --- 4. Layout ---
    top_content = ft.Container(
        height=250,
        alignment=ft.alignment.center,
        content=logo_image
    )

    bottom_content = ft.Container(
        expand=True,
        bgcolor="#fce4ec",
        border_radius=ft.border_radius.vertical(top=30),
        padding=ft.padding.only(top=40),
        alignment=ft.alignment.top_center,
        content=ft.Container(
            width=350,
            bgcolor="#e0e0e0",
            border_radius=20,
            padding=30,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Text("ยืนยันตัวตนด้วยบริการของสถาบันฯ", size=16, weight=ft.FontWeight.BOLD, color="black"),
                    ft.Text("โดยใช้ E-mail Account ของสถาบันฯ", size=12, color="black"),
                    email_field,
                    password_field,
                    ft.Container(height=10), 
                    login_btn,
                ]
            )
        )
    )

    return ft.View(
        route="/login",
        padding=0,
        bgcolor="white",
        appbar=ft.AppBar(
            # ✅ แก้ไข Icon ตรงนี้ให้ถูกต้อง
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: page.go("/")
            ),
            title=ft.Text("KMITL", color="black"),
            center_title=True,
            bgcolor="white",
            elevation=0
        ),
        controls=[
            ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    top_content,
                    bottom_content
                ]
            )
        ]
    )