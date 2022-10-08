from datetime import datetime


def get_time(request):
    time_now = datetime.now()
    return {"time": time_now}


