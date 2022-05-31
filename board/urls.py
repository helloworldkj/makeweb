from django.urls import path
from . import views

#board앱의 urls.py파일
app_name="board"
urlpatterns=[
    path('', views.board_list, name='board_list'),
    path('<int:Post_id>/', views.detail), #수정한 내용 -> board/Post_id의 형식으로 매핑
    #int는 숫자가 매핑됨을 의미

    path('write/', views.write, name='write'),
    path('write/save_post/', views.save_post, name='save_post'),
]