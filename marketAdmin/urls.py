
# from django.urls import path
# from . import views as p_view
# urlpatterns = [

  
#     # for the user 
#     path('health/',p_view.healthList.as_view(),name='health'),
#     path('medicines/',p_view.medicinesList.as_view(),name='medicines')
# ]

from django.urls import path
from . import views as p_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [

    # for the user 
    path('health/', p_view.healthList.as_view(), name='health'),
    path('medicines/', p_view.medicinesList.as_view(), name='medicines'),


]

# ✅ Append media/static URL handling
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

