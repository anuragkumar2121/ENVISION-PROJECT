from django.urls import path

from.import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("getStarted", views.getStarted,name = "getStarted"),
    path("<int:schedule_id>",views.bus, name="bus"),
    path("<int:schedule_id>/book",views.book, name= "book"),
    path("search", views.Search, name = "search"),
    path("form",views.form, name= "form"),
    path("form2",views.form, name= "form2"),
    path("register",views.register, name="register"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.index2, name="profile")



#    path("login", views.login_view, name = "login"),
#   path("logout", views.logout_view, name="logout"),
    
]