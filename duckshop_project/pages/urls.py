from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path("adminlist/", views.ProductAdminListView.as_view(), name="product_adminlist"),
    path("new/", views.ProductCreateView.as_view(), name="product_new"),
    path("edit/<int:pk>", views.ProductEditView.as_view(), name="product_edit"),
    path("delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"),

    path("cart/", views.CartListView.as_view(), name="cart"),
    path("cart/add/<int:pk>", views.ProductAddToCart.as_view(), name="add_to_cart"),
    path("cart/edit/<int:pk>", views.CartEntryEditQuant.as_view(), name="cartentry_edit_quantity"),
    path("cart/<int:pk>/delete", views.CartEntryDeleteView.as_view(), name="cartentry_delete"),
    path("cart/order/", views.OrderConfirmView.as_view(), name="confirm_order"),

    path("order/", views.OrderListView.as_view(), name="order_list"),
    path("order/<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
]
