from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.utils.safestring import SafeString
from .models import BlogEntry, BlogImage, BlogCodeSnippet

def index(request):
    latest_blog_list = BlogEntry.objects.filter(posted__lte=timezone.now()).order_by('posted')
    for story in latest_blog_list:
        image_list = BlogImage.objects.filter(post=story)
        codesnippet_list = BlogCodeSnippet.objects.filter(post=story)
        if len(image_list) > 1:
            story.body = story.body.split(image_list[1].anchor)[0]
        elif len(image_list) > 0:
            image = image_list[0]
            story.body = story.body.replace(image.anchor, "<img src=\"" + image.image.url + "\" alt=\"" + image.caption + "\">" + "\n" + image.caption + "\n")
        else:
            story.body = story.body
        if len(codesnippet_list) > 1:
            story.body = story.body.split(codesnippet_list[1].anchor)[0]
        elif len(codesnippet_list) > 0:
            codesnippet = codesnippet_list[0]
            story.body = story.body.replace(codesnippet.anchor, "<div class=\"callout\"><code>" + codesnippet.caption + "</code><pre id=\"" + codesnippet.anchor + "\">" + codesnippet.CodeSnippet + "</pre></div>")
        else:
            story.body = story.body
        story.body = SafeString(story.body)
    return render(request, "blog.html", {"latest_blogs": latest_blog_list})

def detail(request, the_slug):
    try:
        blog_item = BlogEntry.objects.get(slug=the_slug)
        image_list = BlogImage.objects.filter(post=blog_item)
        codesnippet_list = BlogCodeSnippet.objects.filter(post=blog_item)
    except BlogEntry.DoesNotExist:
        raise Http404('That blog article doesn\'t exist')
    for image in image_list:
        blog_item.body = SafeString(blog_item.body.replace(image.anchor, "<img src=\"" + image.image.url + "\" alt=\"" + image.caption + "\">" + "\n" + image.caption + "\n"))
    for codesnippet in codesnippet_list:
        if codesnippet.caption:
            print("CAPTION: ", codesnippet.caption, len(codesnippet.caption))
        if bool(codesnippet.caption):
            blog_item.body = SafeString(blog_item.body.replace(codesnippet.anchor, "<div class=\"callout\"><code>" + codesnippet.caption + "</code><pre id=\"" + codesnippet.anchor + "\">" + codesnippet.CodeSnippet + "</pre></div>"))
        else:
            blog_item.body = SafeString(blog_item.body.replace(codesnippet.anchor, "<div class=\"callout\"><pre id=\"" + codesnippet.anchor + "\">" + codesnippet.CodeSnippet + "</pre></div>"))
    return render(request, "blogitem.html", {"story": blog_item, "images": image_list})
