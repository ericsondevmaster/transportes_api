from django.urls import path
from . import views


urlpatterns = [
    path('colors/', views.ColorCreateListView.as_view(), name='color-create-list'),
    path('colors/<int:pk>/', views.ColorRetrieveUpdateDestroyView.as_view(), name='color-detail-view'),
]
