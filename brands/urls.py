from django.urls import path
from . import views


urlpatterns = [
    path('brands/', views.BrandCreateListView.as_view(), name='brand-create-list'),
    path('brands/<int:pk>/', views.BrandRetrieveUpdateDestroyView.as_view(), name='brand-detail-view'),
]
