from django.conf.urls import url
from . import views

app_name = 'doxwiki'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tag/$', views.TagList.as_view(), name='tag_list'),
    url(r'^category/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tag, name='tag'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.category, name='category'),
    url(r'^(?P<slug>[-\w]+)/$', views.page, name='page'),
    url(r'^(?P<slug>[-\w]+)/(?P<attachment>.*)/$', views.attachment, name='attachment'),
]

