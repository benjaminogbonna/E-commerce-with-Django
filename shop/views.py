from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm, CartAddProductForm2
# from .recommender import Recommender

# Create your views here.

# A function for Product list (all products) 
# A view to display all products
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	# cart_product_form2 = CartAddProductForm2()

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	return render(request, 'shop/product/list.html',
		{'category': category, 'categories': categories, 'products': products})


# A view to retrive single products
def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)

	# r = Recommender()
	# recommended_products = r.suggest_products_for([product], 4)
	return render(request, 
		'shop/product/detail.html', 
		{'product': product, 
		'cart_product_form': cart_product_form,
		# 'recommended_products': recommended_products
		})
