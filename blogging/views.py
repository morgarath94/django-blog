from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
from django.http.response import HttpResponse, Http404
from django.template import loader
from blogging.models import Post


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["t%s: %s" % k for k in kwargs])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
