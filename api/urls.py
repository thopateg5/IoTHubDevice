from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import DDetailsView
 


urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
    url(r'^create/$',DDetailsView.as_view(), name="garry"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)


 

