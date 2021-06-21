from django.conf.urls import url
from . import views
app_name='blogapp'
urlpatterns = [
        url(r'^$', views.BlogIndex.as_view(), name='index'),
        url(r'^(?P<slug>[-\w]+)/comment/$', views.AddComment, name='comment'),
        url(r'^post/$', views.Postsubmit, name='post'),
        url(r'^user/$', views.BlogUser.as_view(), name='user'),
        url(r'^add/$', views.postadd, name='add'),
        url(r'^register/$', views.register, name='register'),
        url(r'^(?P<slug>[-\w]+)/compo/$', views.compo, name='compo'),
        url(r'^hello', views.swallow, name= 'login'),
        url(r'^(?P<ID>[-\w]+)/editComment/$' , views.edit,  name='edit'),
        url(r'^(?P<ID>[-\w]+)/Delcomment/$', views.delete, name='delete'),

]
