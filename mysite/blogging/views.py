from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, Http404
from django.template import loader
from blogging.models import Post


def stub_view(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += ('Args: \n')
        body += '\n'.join(['\t%s' % a for a in args])
    if kwargs:
        body += ('Kwargs: \n')
        body += '\n'.join(['t%s: %s' % k for k in kwargs])
    return HttpResponse(body, content_type='text/plain')

def list_view(request):
    published_posts = Post.objects.exclude(published_date__exact=None)
    posts = published_posts.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
