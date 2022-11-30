from django.forms import ModelForm
from .models import Person

# Criando uma classe com os campos do formulário
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']






