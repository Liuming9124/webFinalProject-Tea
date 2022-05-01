from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'oid': '電話號碼',
            'name': '名字',
            'drink': '飲料',
            'size': '大小'
        }

