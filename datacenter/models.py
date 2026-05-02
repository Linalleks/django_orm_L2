from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    # рассчитывает длительность визита, возвращает количество секунд
    def get_duration(self):
        from django.utils.timezone import localtime, now
        if self.leaved_at:
            delta = localtime(self.leaved_at) - localtime(self.entered_at)
        else:
            delta = localtime(now().replace(microsecond=0)) - localtime(self.entered_at)
        return delta.total_seconds()

    # определяет, подозрителен визит или нет. Возвращает True или False
    def is_visit_long(self, minutes=60):
        minutes_duration = self.get_duration() // 60
        if minutes_duration > minutes:
            return True
        else:
            return False

    # Превращает длительность визита в строку, готовит к выводу на страницу
    def format_duration(self):
        seconds = int(self.get_duration())
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        str_duration = f'{minutes} мин'
        if hours:
            str_duration = f'{hours} ч {str_duration}'

        return str_duration
