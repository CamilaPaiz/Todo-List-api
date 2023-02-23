from app.views import TodoViewSet

from rest_framework.routers import DefaultRouter

#criando através da ViewSet urls para get,post,dele,put

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls
