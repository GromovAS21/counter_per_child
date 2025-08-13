from django.urls import path

from gender.apps import GenderConfig
from gender.views import GenderView, GenderUpdateView, GenderFullUpdateView

app_name = GenderConfig.name

urlpatterns = [
    path('gender-cards/', GenderView.as_view(), name='home_page'),
    path('update/<uuid:pk>/', GenderUpdateView.as_view(), name='update_page'),
    path('update/full/<uuid:pk>/', GenderFullUpdateView.as_view(), name='update_full_page'),
]