from django.urls import path, include
from rest_framework.routers import DefaultRouter
# 追加
from .views import ProductViewSet, ProductDummyApiView, Product_list

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path("dummy/", ProductDummyApiView.as_view()),
    path('list/', Product_list),
]