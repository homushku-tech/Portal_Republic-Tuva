from django.urls import path
from .views import index, OrderView
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('api/orders', OrderView)
urlpatterns = [
    path('', index, name='index')
]
urlpatterns +=router.urls