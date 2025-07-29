from django.urls import path

from gender.apps import GenderConfig
from gender.views import GenderView, GenderUpdateView

app_name = GenderConfig.name

urlpatterns = [
    path('', GenderView.as_view(), name='home_page'),
    path('update/<int:pk>/', GenderUpdateView.as_view(), name='update_page'),
]