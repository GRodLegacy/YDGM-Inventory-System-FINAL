from django.shortcuts import render, redirect, get_object_or_404
from .models import Electronics, Apparel, Equipment, Toys, Footwear
from .forms import ElectronicsForm, ApparelForm, EquipmentForm, ToysForm, FootwearForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_Electronics(request):
    items = Electronics.objects.all()
    context = {
        'items' : items,
        'header': 'Electronics'

    }
    return render(request, 'index.html', context)

def display_Apparel(request):
    items = Apparel.objects.all()
    context = {
        'items' : items,
        'header' : 'Apparel'

    }
    return render(request, 'index.html', context)

def display_Equipment(request):
    items = Equipment.objects.all()
    context = {
        'items' : items,
        'header' : 'Equipment'

    }
    return render(request, 'index.html', context)

def display_Toys(request):
    items = Toys.objects.all()
    context = {
        'items' : items,
        'header' : 'Toys'

    }
    return render(request, 'index.html', context)

def display_Footwear(request):
    items = Footwear.objects.all()
    context = {
        'items' : items,
        'header' : 'Footwear'

    }
    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_Electronics(request):
    return add_item(request, ElectronicsForm)


def add_Apparel(request):
    return add_item(request, ApparelForm)
    

def add_Equipment(request):
    return add_item(request, EquipmentForm)
       
def add_Toys(request):
    return add_item(request, ToysForm)

def add_Footwear(request):
    return add_item(request, FootwearForm)


def edit_Electronics(request, pk):
    item = get_object_or_404(Electronics, pk=pk)

    if request.method == "POST":
        form = ElectronicsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ElectronicsForm(instance=item)

        return render(request, 'edit_item.html', {'form' : form})


def edit_Apparel(request, pk):
    item = get_object_or_404(Apparel, pk=pk)

    if request.method == "POST":
        form = ApparelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ApparelForm(instance=item)

        return render(request, 'edit_item.html', {'form' : form})


def edit_Equipment(request, pk):
    item = get_object_or_404(Equipment, pk=pk)

    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EquipmentForm(instance=item)

        return render(request, 'edit_item.html', {'form' : form})


def edit_Toys(request, pk):
    item = get_object_or_404(Toys, pk=pk)

    if request.method == "POST":
        form = ToysForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ToysForm(instance=item)

        return render(request, 'edit_item.html', {'form' : form})


def edit_Footwear(request, pk):
    item = get_object_or_404(Footwear, pk=pk)

    if request.method == "POST":
        form = FootwearForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = FootwearForm(instance=item)

        return render(request, 'edit_item.html', {'form' : form})


def delete_Electronics(request, pk):

    Electronics.objects.filter(id=pk).delete()

    items = Electronics.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)


def delete_Apparel(request, pk):

    Apparel.objects.filter(id=pk).delete()

    items = Apparel.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)


def delete_Equipment(request, pk):

    Equipment.objects.filter(id=pk).delete()

    items = Equipment.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)


def delete_Toys(request, pk):

    Toys.objects.filter(id=pk).delete()

    items = Toys.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)


def delete_Footwear(request, pk):

    Footwear.objects.filter(id=pk).delete()

    items = Footwear.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)