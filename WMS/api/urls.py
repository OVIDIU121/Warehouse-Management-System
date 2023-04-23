from django.urls import path
from .views import LocationList, LocationDetail, InventoryList, InventoryDetail, SupplierList, SupplierDetail, CustomerList, CustomerDetail, MoveTaskList, MoveTaskDetail, OrderList, OrderDetail, OrderItemList, OrderItemDetail, ItemList, ItemDetail, PreAdviceList, PreAdviceDetail, PreAdviceItemList, PreAdviceItemDetail, TransactionList, TransactionDetail

# Access enpoints for the API.
urlpatterns = [
    path('api/locations/', LocationList.as_view()),
    path('api/locations/<int:pk>/', LocationDetail.as_view()),
    path('api/orders/', OrderList.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('api/orders-items/', OrderItemList.as_view(), name='order-item-list'),
    path('api/orders-items/<int:pk>/',
         OrderItemDetail.as_view(), name='order-item-detail'),
    path('api/items/', ItemList.as_view()),
    path('api/items/<int:pk>/', ItemDetail.as_view()),
    path('api/items/', ItemList.as_view()),
    path('api/items/<int:pk>/', ItemDetail.as_view()),
    path('api/preadvice/', PreAdviceList.as_view(), name='order-list'),
    path('api/preadvice/<int:pk>/',
         PreAdviceDetail.as_view(), name='preadvice-detail'),
    path('api/preadvice-items/', PreAdviceItemList.as_view(),
         name='preadvice-item-list'),
    path('api/preadvice-items/<int:pk>/',
         PreAdviceItemDetail.as_view(), name='order-item-detail'),
    path('api/transaction/', TransactionList.as_view()),
    path('api/transaction/<int:pk>/', TransactionDetail.as_view()),
    path('api/supplier/', SupplierList.as_view()),
    path('api/supplier/<int:pk>/', SupplierDetail.as_view()),
    path('api/customer/', CustomerList.as_view()),
    path('api/customer/<int:pk>/', CustomerDetail.as_view()),
    path('api/movetask/', MoveTaskList.as_view()),
    path('api/movetask/<int:pk>/', MoveTaskDetail.as_view()),
    path('api/inventory/', InventoryList.as_view()),
    path('api/inventory/<int:pk>/', InventoryDetail.as_view()),
]
