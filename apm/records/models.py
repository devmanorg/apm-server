from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta


class Play(models.Model):
    created = models.DateTimeField('создана', default=timezone.now, null=True, blank=True)
    terminated = models.DateTimeField('завершено', null=True, blank=True)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def get_absolute_url(self):
        return reverse('play', kwargs={
            'play_id': self.id
        })


class EventQuerySet(models.QuerySet):

    def count_events(self, secs, end_datetime=None):
        if end_datetime is None:
            end_datetime = timezone.now()
        return self.filter(
            registered__lte=end_datetime,
            registered__gt=end_datetime - timedelta(seconds=secs)
        ).count()


class Event(models.Model):
    play = models.ForeignKey('Play', verbose_name='запись', related_name='events', on_delete=models.CASCADE)
    registered = models.DateTimeField(
        'зарегистрировано',
        default=timezone.now,
        help_text='серверное время',
        db_index=True
    )

    objects = EventQuerySet.as_manager()

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'