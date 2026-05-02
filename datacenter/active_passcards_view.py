from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    # all_passcards = Passcard.objects.all()
    # Passcard.objects.filter(is_active=True).count()
    context = {
        'active_passcards': Passcard.objects.filter(is_active=True),  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
