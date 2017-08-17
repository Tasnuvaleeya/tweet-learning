from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView,DeleteView
from .models import Tweet
from .forms import TweetModelForm
from django.forms.utils import ErrorList
from django.urls import reverse_lazy,reverse
from django import forms
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.db.models import Q


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


class TweetCreateView(FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = 'tweet_feed/create_view.html'
    # success_url = "/tweet/create/"


class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweet_feed/tweet_update.html'
    # success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    template_name = 'tweet_feed/confirm_delete.html'
    success_url = reverse_lazy("tweet:list")

    #
    # def get_success_url(self):
    #     return reverse('tweet:list')













'''
# def tweet_detail_view(request,id=1):
#     obj = Tweet.objects.get(id=id)
#
#     context ={
#         'object': obj
#     }
#     return render(request, 'tweet_feed/tweet_detail.html', context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'tweet_feed/tweet_list.html',context)
#
#
#







'''