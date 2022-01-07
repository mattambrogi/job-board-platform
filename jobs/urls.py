# jobs/urls.py
from django.urls import path
from .views import ( JobListView, JobUpdateView, EmployerUpdateView, JobDetailView, 
    JobDeleteView, JobCreateView, JobBoardView, 
    JobBoardListView )

urlpatterns = [
    path('<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'), 
    path('<int:pk>/edit_employer/', EmployerUpdateView.as_view(), name='job_edit_employer'), 
    path('<int:pk>/detail', JobDetailView.as_view(), name='job_detail'), 
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/new/', JobCreateView.as_view(), name='new_job'),
    #path('<int:pk>/', JobBoardView.as_view(), name='job_board'),
    path('all_job_boards/', JobBoardListView.as_view(), name='job_board_list'),
    path('<slug:slug>/', JobBoardView.as_view(), name='job_board'),
    path('', JobListView.as_view(), name='job_list'),
]


 