from django.db import models


class Bill(models.Model):
    call_start_record = models.ForeignKey('record.Record',
                                          on_delete=models.CASCADE,
                                          related_name='call_start_record')
    call_end_record = models.ForeignKey('record.Record',
                                        on_delete=models.CASCADE,
                                        related_name='call_end_record')
    call_duration = models.DurationField()
    call_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.call_start_record.source
