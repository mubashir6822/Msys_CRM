from django.urls import path
from .views import (lead_list, lead_detail, lead_create,lead_update, lead_delete,LeadListVeiw, LeadDetailVeiw, LeadCreateVeiw, LeadUpdateVeiw, LeadDeleteVeiw)

app_name="leads"

urlpatterns=[
    path('',LeadListVeiw.as_view()),
    path('<int:pk>/',LeadDetailVeiw.as_view()),
    path('<int:pk>/update/',LeadUpdateVeiw.as_view()),
    path('create/',LeadCreateVeiw.as_view(),),
    path('<int:pk>/delete/',LeadDeleteVeiw.as_view()),
]