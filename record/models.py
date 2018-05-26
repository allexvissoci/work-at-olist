from django.db import models
from django.core.validators import ValidationError, MinLengthValidator


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

    def save(self, *args, **kwargs):
        if self.type == 'start':
            if self.source == self.destination:
                message = "Source and destination can't be the same"
                raise ValidationError(message)
            else:
                super().save(*args, **kwargs)
        else:
            if Record.objects.filter(call_id=self.call_id).exists():
                start_record = Record.objects.get(call_id=self.call_id)
                if(start_record.timestamp < self.timestamp):
                    super().save(*args, **kwargs)
                else:
                    message = "Initial record time greater than end time."
                    raise ValidationError(message)
            else:
                raise ValidationError("No initial record.")
