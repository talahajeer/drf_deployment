from django.urls import path, include
from .views import PostSnack, RetrieveSnack

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', PostSnack.as_view(), name='all_snacks'),
    path('<int:pk>', RetrieveSnack.as_view(), name='snack_details'),
]
