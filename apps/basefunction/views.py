from django.shortcuts import render
from apps.poster.models import Post
from apps.base.common_view import get_exchange_link, get_read_most_post, get_navbar_item_homepage, get_feature_post_post
from apps.base.tracking_view import peekpa_tracking
# Create your views here.
from apps.cms import models

@peekpa_tracking
def index(request):
    top_post = Post.objects.filter(is_main_page=True).order_by('-priority')
    list_post = Post.objects.filter(is_main_page=False)
    row_obj = models.PageSetting.objects.all().first()
    page_title = row_obj.page_title
    ad_title = row_obj.ad_title
    ad_image = row_obj.ad_image
    print(ad_image)

    context = {
        'top_post': top_post,
        'list_post': list_post,
        'page_title': page_title,
        'ad_title': ad_title,
        'ad_image': ad_image
    }
    context.update(get_read_most_post())
    context.update(get_exchange_link())
    context.update(get_navbar_item_homepage())
    context.update(get_feature_post_post())
    return render(request, 'post/index.html', context=context)