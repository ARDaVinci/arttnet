from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,)
from .models import Messageprive
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404 , render, redirect
from django.utils.text import slugify
from django.http import Http404

class MessageList(LoginRequiredMixin , ListView):
    login_url = '/intranet_artt/login/'
    template_name = 'mp/messages.html'
    context_object_name = 'all_messages'

    def get_queryset(self):
        return Messageprive.objects.all().order_by('-creation_date')

class MessageDetail(LoginRequiredMixin , DetailView):
    login_url = '/intranet_artt/login/'
    template_name = 'mp/message.html'
    model = Messageprive

class MessageCreate(LoginRequiredMixin, CreateView):
    login_url = '/intranet_artt/login/'
    model = Messageprive
    fields = [ 'title' , 'text' , 'receiver']

    def form_valid(self, form):
        self.object = form.save(commit= False)
        self.object.sender.username = self.request.user.username
        self.object.creation_date =  datetime.datetime.now()
        self.object.save()
        return super().form_valid(form)


