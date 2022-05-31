from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def board_list(request): #글목록 
    Post_list=Post.objects.order_by('-create_date')
    context={'Post_list': Post_list}
    return render(request, 'board/board_list.html', context)

def detail(request, Post_id): #글 내용 조회
    in_post=Post.objects.get(id=Post_id)
    context={'Post': in_post} 
    return render(request, 'board/Post_detail.html', context)


def write(request): #글 작성 화면 출력
    return render(request, 'board/write.html')

def save_post(request): #post로 받는 내용 저장
    write_post=Post(subject=request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    write_post.save()
    return redirect('http://127.0.0.1:8000/board') #저장되면 글 목록화면을 띄우기

