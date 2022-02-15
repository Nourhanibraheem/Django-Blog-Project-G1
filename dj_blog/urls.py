from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('post/', views.post,name='post'),
    # path('all-posts/',views.postPage,name='all-posts'),
    path('register/', views.registerpage , name='register' ),
    path('login/', views.loginpage , name='login' ),
    path('landing/', views.landing,name='landing'),
    path('logout/', views.logoutpage,name='logout'),
    path('subscribe/<cat_id>', views.subscribe,name="subscribe"),
    path('unsubscribe/<cat_id>', views.unsubscribe,name="unsubscribe"),
    path('manageBlog/', views.manageBlog,name='manageBlog'),
    path('add-post/',views.addPost,name='add-post'),
    path('cat-posts/<CatId>',views.catPosts,name='cat-posts'),
    path('post/<post_id>',views.AddLike,name='like'),
    path('post/<post_id>',views.AddDislike,name='dislike'),
      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)