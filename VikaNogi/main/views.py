from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def gift_voucher(request):
    return render(request, 'main/gift-vouchers.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contacts.html')
