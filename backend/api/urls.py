from django.urls import path
from . import views


urlpatterns = [
    path('risks/', views.RiskList.as_view(), name='get_post_risks'),
    path('risks/<int:pk>', views.RiskDetail.as_view(), name='get_delete_update_risk'),
]
