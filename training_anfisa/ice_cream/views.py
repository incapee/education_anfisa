from django.shortcuts import render


ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]


# Create your views here.
def catalog(request):
    context = {
        'catalog': ice_cream_catalog,
    }
    return render(request, 'ice_cream/list.html', context)


def item(request, pk):
    context = {
        'item': ice_cream_catalog[pk],
    }
    return render(request, 'ice_cream/detail.html', context)
