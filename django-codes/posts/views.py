from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post

reques_counter_signal = Signal(providing_args=['timestamp'])

# Create your views here.
def home(request):
    reques_counter_signal.send(sender=Post,timestamp="2019-01-01")
    return HttpResponse("here is the response")


# @receiver(request_finished)
@receiver(reques_counter_signal)
def post_request_receiver(sender, **kwargs):
    print("Request finished daaaa")

@receiver(reques_counter_signal)
def post_counter_receiver(sender, **kwargs):
    print("sss",    kwargs)


request_finished.connect(post_request_receiver)
