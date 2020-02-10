from django.contrib import admin
from django.urls import path
from morae.views import main, details, writing, create, delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('details/', details),
    path('writings/', writing),
    path('writing/details/', details),
    path('create/', create),
    path('delete/', delete),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)