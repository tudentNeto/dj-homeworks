from django.http import Http404
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views import generic
from main.models import Car, Client, Sale

class CarDetailView(generic.DetailView):
    model = Car

def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    qry = Car.objects.all()
    context = {}
    context['cars'] = list(qry)
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    try:
        # получите авто, если же его нет, выбросьте ошибку 404
        template_name = 'main/details.html'
        car_set = Car.objects.get(id=car_id)
        car={}
        car['car'] = car_set
        return render(request, template_name, context=car)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car_set = Car.objects.get(id=car_id)
        # qry_car=Car.objects.filter(id=car_id).values_list('model', 'year')
        qry = Sale.objects.filter(car_id=car_id)
        context={}
        context['sales'] = list(qry)
        context['car'] = car_set
        # context['car'] = {'model' : list(qry_car)[0][0], 'year' : list(qry_car)[0][1]}
        template_name = 'main/sales.html'
        print(context)
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
