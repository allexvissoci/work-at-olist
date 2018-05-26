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
        params = [self.call_start_record.call_id,
                  self.call_start_record.timestamp,
                  self.call_end_record.timestamp]
        return "call_id: {}, started at {} and ended at {}".format(*params)
