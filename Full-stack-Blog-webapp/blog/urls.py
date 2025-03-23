from django.urls import path

from .import views


urlpatterns=[
  path ("" , views.StartingPageView.as_view() , name="starting-page"), #for main home page
  path ("posts" , views.AllPostsView.as_view() , name="posts-page"), #for '.../posts' , for all posts
  path ("posts / <slug:slug>" , views.SinglePostView.as_view() , name="post-detail-page"), #for each post in the allposts. use this <slug> method, because it will change according to differn post names. by slug:slug,it shows those post names as my-first-post   like that design.  

  path ("read-later", views.ReadLaterView.as_view() , name="read-later")

]