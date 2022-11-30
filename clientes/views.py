from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


# Create your views here.
@login_required
def person_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)
    checkbox = request.GET.get('meu-checkbox', None)

    if checkbox == 'on':
        people = Person.objects.filter(ativo=True)

    if nome or sobrenome:
        people = Person.objects.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
        # '''
        # &&
        # first_name__icontains  => case insensitive
        # '''
        # #people = (people.filter(first_name__icontains=termo_busca, last_name__icontains=termo_busca))
        #
        # '''
        # OR ou |
        # '''
        # #people = (people.filter(first_name__icontains=termo_busca) | people.filter(last_name__icontains=termo_busca))
    else:
        people = Person.objects.all()
        print('nenhum resultado encontrado')

    return render(request, 'person.html', {'people': people})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)  # request.FILES (arquivos de mídia que são enviados pelo formulário), junto com o enctype no template 'person_form.html

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def people_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def people_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

