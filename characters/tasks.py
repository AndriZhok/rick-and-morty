from characters.models import Characters

from celery import shared_task


@shared_task
def count_widgets():
    return Characters.objects.count()
