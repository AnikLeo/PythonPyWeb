from itertools import count

from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Count
from django.db.models import Avg, Q
from django.db.models import Max, Min



class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        self.answer2 = Author.objects.annotate(num_entries=Count('entries')).order_by('num_entries').first() # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer3 = Entry.objects.filter(Q (tags__name = 'Кино')| Q (tags__name = 'Музыка' ))  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer4 = Author.objects.filter(gender = 'ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?
        total_author = Author.objects.count()
        author_agree = Author.objects.filter(status_rule=True).count()
        self.answer5 =f"{(author_agree/total_author) * 100:.2f}"   # TODO Какой процент авторов согласился с правилами при регистрации?


        self.answer6 = Author.objects.filter(stage = )   # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer7 = None  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = None  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = None  # TODO Сколько статей написано каждым автором?



        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

