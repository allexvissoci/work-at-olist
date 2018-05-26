from django.db import models
from django.core.validators import MinLengthValidator


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=5)
    timestamp = models.DateTimeField()
    call_id = models.CharField(max_length=200)
    source = models.CharField(
                                max_length=11, blank=True, null=True,
                                validators=[MinLengthValidator(10)])
    destination = models.CharField(
                                max_length=11, blank=True, null=True,
                                validators=[MinLengthValidator(10)])

    class Meta:
        unique_together = (("type", "call_id"))

    def __str__(self):
        return "{} {} {}".format(self.id, self.call_id, self.timestamp)
