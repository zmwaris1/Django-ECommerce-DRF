from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreationListView.as_view(), name='orders'),
    path('<int:order_id>', views.OrderDetailView.as_view(), name='order-details'),
    path('update-status/<int:order_id>', views.UpdateOrderStatus.as_view(), name='update-order'),
    path('user/<int:user_id>/orders', views.UserOrdersView.as_view(), name='user-orders'),
    path('user/<int:user_id>/orders/<int:order_id>', views.UserOrderDetailView.as_view(), name='user-order-detail'),

]