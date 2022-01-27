from dataclasses import field, fields
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.forms import FeedingForm

# import out model
from .models import Ferret, Toy


class FerretCreate(CreateView):
	model = Ferret
	fields = ['name', 'breed', 'description', 'age']
	success_url = '/ferrets/'


class FerretUpdate(UpdateView):
	model = Ferret
	fields = ['breed', 'description', 'age']


class FerretDelete(DeleteView):
	model = Ferret
	success_url = '/ferrets/'


def home(request):
	return HttpResponse('<h1>Hello  ۜ\(סּںסּَ` )/ۜ</h1>')


def about(request):
	return render(request, 'about.html')


def ferrets_index(request):
	ferrets = Ferret.objects.all()
	return render(request, 'ferrets/index.html', {'ferrets': ferrets})


def ferrets_detail(request, ferret_id):
	ferret = Ferret.objects.get(id=ferret_id)
	toys_ferret_doesnt_have = Toy.objects.exclude(
		id__in=ferret.toys.all().values_list('id'))
	feeding_form = FeedingForm()
	print(f"{ferret} <-- ferret")
	return render(request, 'ferrets/detail.html', {
		'ferret': ferret, 
		'feeding_form': feeding_form,
		'toys': toys_ferret_doesnt_have
	})


def add_feeding(request, ferret_id):
	form = FeedingForm(request.POST)

	if form.is_valid():
		new_feeding = form.save(commit=False)
		new_feeding.ferret_id = ferret_id
		new_feeding.save()
	return redirect('detail', ferret_id=ferret_id)


def assoc_toy(request, ferret_id, toy_id):
	Ferret.objects.get(id=ferret_id).toys.add(toy_id)
	return redirect('detail', ferret_id=ferret_id)


class ToyList(ListView):
	model = Toy


class ToyDetail(DetailView):
	model = Toy


class ToyCreate(CreateView):
	model = Toy
	fields = '__all__'


class ToyUpdate(UpdateView):
	model = Toy
	fields = ['name', 'color']


class ToyDelete(DeleteView):
	model = Toy
	success_url = '/toys/'
