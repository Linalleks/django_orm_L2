import datetime
import os
from decouple import config
from environs import env


import django
from django.utils.timezone import localtime, now

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit  # noqa: E402


def format_duration(duration):
    seconds = int(duration.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    str_duration = f'{minutes}мин'

    if hours:
        str_duration = f'{hours}ч {str_duration}'

    return str_duration

env.read_env()
if __name__ == '__main__':
    # print('Количество пропусков:', Passcard.objects.count())
    # print('Количество активных пропусков:', Passcard.objects.filter(is_active=True).count())

    # active_visits = Visit.objects.filter(leaved_at=None)
    # print('Количество визитов:', active_visits.count())
    # print('Визиты:', active_visits)

    # print(Passcard.objects.values('owner_name'))
    # passcard = Passcard.objects.values().get(id=1)
    print(type(env.bool("DEBUG")))
    print(env.bool("DEBUG"))
    # print('Визиты:', Visit.objects.filter(passcard=passcard))

    # long_visits = []
    # for visit in Visit.objects.all():
    #     # visit = Visit.objects.filter(id=100)[0]
    #     # print(visit.get_duration())
    #     # print(visit.is_visit_long())
    #     # print(visit.is_visit_long(minutes=1000))
    #     if visit.is_visit_long(minutes=1000):
    #         long_visits.append(visit)

    # print('Визиты дольше 60 мин:', long_visits)
