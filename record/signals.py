from django.db.models.signals import post_save
from django.dispatch import receiver
from record.models import Record
from bill.models import Bill
import bill.helper as helper


@receiver(post_save, sender=Record)
def create_bill(sender, instance=None, created=False, **kwargs):
    if created and instance.type == "end":

        if(Record.objects.filter(call_id=instance.call_id).count() == 2):
            call_start = Record.objects.get(
                                            call_id=instance.call_id,
                                            type="start"
                                          )
            call_end = Record.objects.get(
                                            call_id=instance.call_id,
                                            type="end"
                                        )
            call_duration = call_end.timestamp - call_start.timestamp
            call_price = helper.get_call_price(call_start, call_end)

            Bill.objects.create(
                                call_start_record=call_start,
                                call_end_record=call_end,
                                call_duration=call_duration,
                                call_price=call_price
                                )
