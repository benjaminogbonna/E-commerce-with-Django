from django import forms
# from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# A form to add or update items in the cart
class CartAddProductForm(forms.Form):
	quantity = forms.IntegerField(label='Quantity',
		widget=forms.NumberInput(attrs={'class': '',
			'value': '1', 'type': 'number', 'min':'1', 'max': '20'}))
	override = forms.BooleanField(required=False,
		initial=False, widget=forms.HiddenInput)


class CartAddProductForm2(forms.Form):
	quantity = forms.IntegerField(widget=forms.HiddenInput())


# widget=forms.EmailInput(attrs={'class': 'form-control',
		# 'placeholder': 'Senders email'}) {{ item.quantity }}
		# # quantity = forms.TypedChoiceField(label='QTY ',
		# choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
		# widget=forms.EmailInput(attrs={'class': 'input-number',
		# 'placeholder': ''}))