from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
# – главной main_view;
# – направлению /departure/<str:departure>/ – departure_view;
# – тура /tour/<int:id>/ – tour_view
# Create your views here.


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    context = {"departure": departure}
    return render(request, 'departure.html', context=context)


def tour_view(request, id):
    context = {"id": id}
    return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Нет такого тура или маршрута')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
