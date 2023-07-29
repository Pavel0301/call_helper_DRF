from django.urls import path, include
from rest_framework.routers import DefaultRouter
from organisations.views import dicts
from users.views import users

router = DefaultRouter()
router.register(r'dicts/positions', dicts.PositionView, 'positions')

urlpatterns = [

]


urlpatterns += path('organisations/', include(router.urls)),






