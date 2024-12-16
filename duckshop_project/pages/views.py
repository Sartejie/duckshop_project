from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# Create your views here.

from . import models
from .forms import AddToCartForm, OrderConfirmForm

#View главной страницы
class ProductListView(ListView):
    model = models.Product
    template_name = 'home.html'
#View страницы описания продукта
class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'

#View страниц просмотра, создания, редактирования, удаления продуктов
class ProductAdminListView(PermissionRequiredMixin, ListView):
    permission_required = "add"
    model = models.Product
    template_name = 'product_adminlist.html'

class ProductCreateView(PermissionRequiredMixin, CreateView):
       permission_required = "add"
       model = models.Product
       template_name = 'product_new.html'
       fields = ['title', 'description', 'price', 'image']

class ProductEditView(PermissionRequiredMixin, UpdateView):
    permission_required = "add"
    model = models.Product
    fields = ['title', 'description', 'price', 'image']
    template_name = 'product_edit.html'

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "add"
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_adminlist')


#View корзины покупок
class CartListView(LoginRequiredMixin, ListView):
    template_name = 'cart.html'
    login_url = 'login'

    def get_queryset(self):
        return self.request.user.CartEntry.all()
    
    def get_context_data(self, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)
        price = 0
        for productentry in self.request.user.CartEntry.all():
            price += productentry.quantity * productentry.product.price
        context['total_sum'] = price
        return context
    
#View удаления продукта из корзины
class CartEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.CartEntry
    template_name = 'cartentry_delete.html'
    success_url = reverse_lazy('cart')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.customer == self.request.user

#View добавления продукта в корзину
class ProductAddToCart(LoginRequiredMixin, FormView):
    template_name = "add_to_cart.html"
    form_class = AddToCartForm
    success_url = reverse_lazy("cart")
    login_url = 'login'
    
    def form_valid(self, form):
        cartproduct = models.Product.objects.get(pk=self.kwargs["pk"])
        cartquery = self.request.user.CartEntry.all()
        try:
            cartentry = cartquery.get(product=cartproduct)
            cartentry.quantity += form.cleaned_data['quantity']
            cartentry.save()
        except:
            obj = models.CartEntry.objects.create(product=cartproduct, customer=self.request.user, quantity=form.cleaned_data['quantity'])
            obj.save()
        return super().form_valid(form)
    
#View страница подтверждения заказа
class OrderConfirmView(LoginRequiredMixin, FormView):
    template_name = "order_confirm.html"
    form_class = OrderConfirmForm
    success_url = reverse_lazy("cart")

    def form_valid(self, form):
        price = 0
        for productentry in self.request.user.CartEntry.all():
            price += productentry.quantity * productentry.product.price
        if price > 0:
            obj = models.Order.objects.create(customer=self.request.user, total_price=price)
            obj.save()
            cartquery = self.request.user.CartEntry.all()
            for cartentry in cartquery:
                orderobj = models.OrderEntry.objects.create(product=cartentry.product, customer=self.request.user, quantity=cartentry.quantity, order=obj)
                orderobj.save()
                cartentry.delete()
        return super().form_valid(form)
  
#View изменения количества продукта в корзине
class CartEntryEditQuant(LoginRequiredMixin, FormView):
    template_name = "edit_quantity.html"
    form_class = AddToCartForm
    success_url = reverse_lazy("cart")
    login_url = 'login'
    
    def form_valid(self, form):
        cartproduct = models.Product.objects.get(pk=self.kwargs["pk"])
        cartquery = self.request.user.CartEntry.all()
        try:
            cartentry = cartquery.get(product=cartproduct)
            cartentry.quantity = form.cleaned_data['quantity']
            cartentry.save()
        except:
            pass
        return super().form_valid(form)
    
#View страница всех заказова
class OrderListView(PermissionRequiredMixin, ListView):
    permission_required = "add"
    model = models.Order
    template_name = 'order_list.html'

#View страница подробного описания заказа
class OrderDetailView(PermissionRequiredMixin, ListView):
    permission_required = "add"
    template_name = 'order_detail.html'
    login_url = 'login'

    def get_queryset(self):
        return models.OrderEntry.objects.all().filter(order=models.Order.objects.all().get(pk=self.kwargs['pk']))