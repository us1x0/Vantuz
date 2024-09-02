from django.shortcuts import render
from .models import Product, Category

# Create your views here.
# главная страница
def home_page(request):
    #Достаем данные из БД
    all_products=Product.objects.all()
    all_categories = Category.objects.all()
    #передаем данные на фронт из бэка
    context = {'products': all_products, 'categories': all_categories}
    # погружаем html файл
    return render(request, 'home.html', context)


#страница с товарами по категориям
def category_page(request, pk):
    #достаем выбранную категорию
    category= Category.objects.get(id=pk)
    #фильтруем продукты по выбранной категории
    exact_products =Product.objects.filter(pr_category=category)
    #передаем данные на фронт
    context= {'products': exact_products}
    #прогружаем html файлы
    return render(request, 'category.html', context)

#страница с выбранным товаром
def product_page(requests,pk):
    #Достаем выбранный товар
    product= Product.objects.filter(id=pk)
    #Передаем данные на фронт
    context = {'product':product}
    #Прогружаем html файлы
    return render (requests, 'product.html', context)