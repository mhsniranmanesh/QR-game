from django.shortcuts import render

# Create your views here.
from game.models import Barcode, Submit, Slogan


def index(request, barcode_id):
    barcode = Barcode.objects.get(barcode_id=barcode_id)
    context = {'barcode': barcode}
    return render(request, 'game/index.html', context=context)


def submit(request, barcode_id, phone_number):
    print("AHAHAH")
    try:
        Submit.objects.get(phone_number=phone_number, barcode_id=barcode_id)
        return render(request, 'game/resubmit.html')
    except:
        Submit.objects.create(phone_number=phone_number, barcode_id=barcode_id)
        slogan = Slogan.objects.order_by('?').first()
        context = {'slogan': slogan.text}
        return render(request, 'game/submit.html', context=context)