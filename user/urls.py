from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('addnote/', views.addnote, name='addnote'),
    path('notes/', views.notes, name='notes'),
    path('noteedit/<int:id>', views.noteedit, name='noteedit'),
    path('notedelete/<int:id>', views.notedelete, name='notedelete'),
    path('noteaddimage/<int:id>', views.noteaddimage, name='noteaddimage'),
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),

]
