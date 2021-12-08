from django import forms
# from django.utils.translation import gettext_lazy as _
# a form to apply coupons to items

class CouponApplyForm(forms.Form):
	code = forms.CharField(label='Coupon')
	