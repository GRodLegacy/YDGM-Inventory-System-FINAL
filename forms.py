from django import forms
from .models import Electronics, Apparel, Equipment, Toys, Footwear


class ElectronicsForm(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = ('price', 'stock', 'item', 'brand', 'site', 'purchased_price', 'posted_date', 'bought_at', 'model' )

class ApparelForm(forms.ModelForm):
    class Meta:
        model = Apparel
        fields = ('price', 'stock', 'item', 'brand', 'site', 'purchased_price', 'posted_date', 'bought_at' )

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('price', 'stock', 'item', 'brand', 'site', 'purchased_price', 'posted_date', 'bought_at', 'model' )

class ToysForm(forms.ModelForm):
    class Meta:
        model = Toys
        fields = ('price', 'stock', 'item', 'brand', 'site', 'purchased_price', 'posted_date', 'bought_at' )

class FootwearForm(forms.ModelForm):
    class Meta:
        model = Footwear
        fields = ('price', 'stock', 'item', 'brand', 'site', 'purchased_price', 'posted_date', 'bought_at', 'model', 'shoe_size' )