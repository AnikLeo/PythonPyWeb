from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag

# from .models import ...


class TrainView(View):
    def get(self, request):



        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

