from datetime import datetime
from datetime import timedelta


def get_call_price(call_start, call_end):

    start_call = call_start.timestamp.time()
    end_call = call_end.timestamp.time()
    start_timedelta = convert_to_timedelta(start_call)
    end_timedelta = convert_to_timedelta(end_call)

    start_time_to_charge = datetime.strptime("06:00:00", "%H:%M:%S").time()
    end_time_to_charge = datetime.strptime("22:00:00", "%H:%M:%S").time()
    start_timedelta_charge = convert_to_timedelta(start_time_to_charge)
    end_timedelta_charge = convert_to_timedelta(end_time_to_charge)

    standing_charge = 0.36
    charge_per_minute = 0.09

    if(
        start_call < start_time_to_charge
        and end_call < start_time_to_charge
        or start_call > end_time_to_charge
        and end_call > end_time_to_charge
    ):
        call_price = standing_charge
    elif(
        start_call >= start_time_to_charge
        and end_call <= end_time_to_charge
    ):
        diff_time = end_timedelta - start_timedelta
        minutes_between = int(diff_time.seconds/60)
        call_price = (minutes_between * charge_per_minute) + standing_charge

    elif(
        start_call < start_time_to_charge
        and end_call >= start_time_to_charge
        and end_call <= end_time_to_charge
    ):
        diff_time = end_timedelta - start_timedelta_charge
        minutes_between = int(diff_time.seconds/60)
        call_price = (minutes_between * charge_per_minute) + standing_charge
    elif(
        start_call >= start_time_to_charge
        and start_call <= end_time_to_charge
        and end_call >= start_time_to_charge
    ):
        diff_time = end_timedelta_charge - start_timedelta
        minutes_between = int(diff_time.seconds/60)
        call_price = (minutes_between * charge_per_minute) + standing_charge
    elif(
        start_call < start_time_to_charge
        and end_call > end_time_to_charge
    ):
        diff_time = end_timedelta_charge - start_timedelta_charge
        minutes_between = int(diff_time.seconds/60)
        call_price = (minutes_between * charge_per_minute) + standing_charge

    return call_price


def convert_to_timedelta(date1):
    data = {'hours': date1.hour,
            'minutes': date1.minute,
            'seconds': date1.second}

    return timedelta(**data)
