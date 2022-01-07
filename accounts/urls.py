from django.urls import path
from .views import SignUpView, AdminView, EmployerAdminView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('<slug:slug>/admin', AdminView.as_view(), name='admin'),
    #path('<int:pk>/admin', AdminView.as_view(), name='admin'),
    path('<slug:slug>/employer_admin', EmployerAdminView.as_view(), name='employer_admin'),
    #path('<int:pk>/employer_admin', EmployerAdminView.as_view(), name='employer_admin'),
]


