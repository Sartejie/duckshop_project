from django import forms

class AddToCartForm(forms.Form):
      quantity = forms.IntegerField(label="Quantity", min_value=0)

class OrderConfirmForm(forms.Form):
      fields = None