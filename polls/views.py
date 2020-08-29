import datetime
import time

from django.http import HttpResponse

from polls.models import Batch


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_data(request):
    for i in range(5):
        create_timestamp = int(time.time())
        create_datetime = datetime.datetime.now()
        print(create_datetime)
        batch = Batch.objects.create(create_timestamp=create_timestamp, create_datetime=create_datetime)
        batch.save()
    return HttpResponse("Create Success!")


def get_datas(request):
    data = Batch.objects.first()
    print(data.create_datetime)
    return HttpResponse("Get Success!")
