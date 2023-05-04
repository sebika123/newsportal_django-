from django.shortcuts import render, redirect
from django.contrib import messages
# from shopping.models import Wishlist, Cart, Order, Comment, Review
from sports.models import content
from health.models import content
from politics.models import content
from home.models import content
from user.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from user.models import like
from django.shortcuts import get_object_or_404, redirect

@login_required
def comment(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        cmt = request.POST['comment']

        comment = comment(user=request.user, content_id=pid, comment=cmt)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
@login_required
def like(request, content_id):
    content = get_object_or_404(content, pk=content_id)
    like.objects.create(user=request.user, acontent=content)
    return redirect('content_detail', pk=content_id)
    
