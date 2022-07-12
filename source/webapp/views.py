from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GoodForm
from webapp.models import Good, CATEGORY_CHOICES

def main_view(request):
    goods = Good.objects.filter().order_by("description", "category")
    return render(request, 'index.html', {'goods':goods})


def good_create_view(request):
    if request.method == 'GET':
        form = GoodForm()
        return render(request, 'good_create.html', {"category_choices":CATEGORY_CHOICES, "form":form})
    else:
        form = GoodForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            remainder = form.cleaned_data.get('remainder')
            price = form.cleaned_data.get('price')
            detailed_description = form.cleaned_data.get('detailed_description')
            new_good = Good.objects.create(description=description,
                                           category=category,
                                           remainder=remainder,
                                           detailed_description=detailed_description,
                                           price=price)
            return redirect("good_view", pk=new_good.pk)
        return render(request, "good_create.html", {"form":form})


def good_view_(request, pk):
   good = get_object_or_404(Good, pk=pk)
   context = {"good": good}
   return render(request, 'good_view.html', context)



