from django.conf.urls import url

from .views import LeafTemplateView

urlpatterns = [
    url(r'(?P<url>.*)(/)?$', LeafTemplateView.as_view(), name='page'),
]
