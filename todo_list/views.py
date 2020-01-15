from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form:
            form.save()
            messages.success(request, 'Item added successful')
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})

    else:

        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('home')


def reschedule(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, 'Item Rescheduled successfully')
    return redirect('home')


def scheduled(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form:
            form.save()
            messages.success(request, 'Item added successful')
            return redirect('home')

    else:

        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
