from django.urls import path
from .views import StoreCreationEndpoint,StoreDetailEndpoint,CategoryCreationEndpoint,CategoryDetailEndpoint,ProductCreateEndpoint,ProductDetailEndpoint,ProductByCategoryEndpoint, ProductSearchEndpoint

urlpatterns = [
    path('store/create/', StoreCreationEndpoint.as_view(), name= 'store-create'),
    path('store/update/<int:pk>/',StoreDetailEndpoint.as_view(), name= 'update-post'),
    path('store/delete-store/<int:pk>/',StoreDetailEndpoint.as_view(), name= 'delete-post'),
    path('categories/create/',CategoryCreationEndpoint.as_view(), name= 'create-category'),
    path('categories/update/<int:pk>/',CategoryDetailEndpoint.as_view(), name= 'update-post'),
    path('categories/delete/<int:pk>/',CategoryDetailEndpoint.as_view(), name= 'delete-post'),
    path('products/create/',ProductCreateEndpoint.as_view(), name= 'create-product' ),
    path('products/update/<int:pk>/',ProductDetailEndpoint.as_view(), name= 'update-products'),
    path('product/list/', ProductCreateEndpoint.as_view(), name= 'list-product'),
    path('category/list/',CategoryCreationEndpoint.as_view(), name= 'list-category'),
    path('products/category/<int:category_id>/', ProductByCategoryEndpoint.as_view(), name = 'products-by-category'),
    path('products/list/', ProductSearchEndpoint.as_view(), name= 'new-product-list')

]