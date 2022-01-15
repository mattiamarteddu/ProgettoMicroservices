from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Borrowing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BorrowingList.as_view()),
    path('<int:borrowing_id>/', views.BorrowingGet.as_view()),
    path("create/", views.BorrowingCreate.as_view(), name="Borrowing_create"),
    path("update/<int:pk>/", views.BorrowingUpdate.as_view(), name="update_Borrowing"),
    path("delete/<int:pk>/", views.BorrowingDelete.as_view(), name="delete_Borrowing"),
]


urlpatterns = format_suffix_patterns(urlpatterns)