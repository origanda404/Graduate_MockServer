#src/main.py --> This is Application!!!
import flet as ft
from screens.welcome_screen import WelcomeScreen
from screens.login_screen import LoginScreen
from screens.advisor.advisor_home import AdvisorHome
from screens.student.student_home import StudentHome


# Setup App 
def main(page: ft.Page):
    print("[Info] Graduate Student Tracking System Starting...")
    page.title = "Graduate Student Tracking System"
    page.window.width = 402
    page.window.height = 874

    # Setup Navigation and Routing
    def route_change(route):
        t_route = ft.TemplateRoute(page.route)

        if t_route.match("/"):
            page.views.clear()
            page.views.append(WelcomeScreen(page))

        elif t_route.match("/login"):
            page.views.append(LoginScreen(page))
        
        elif t_route.match("/advisor_home"):
            page.views.append(AdvisorHome(page))
        
        elif t_route.match("/student_home"):
            page.views.append(StudentHome(page))

        
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")


ft.app(target=main, assets_dir="assets")