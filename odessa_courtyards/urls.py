from rest_framework.routers import DefaultRouter

from .views import MemberRequestViewSet, FormBeforeViewSet, ProblemAreaViewSet


router = DefaultRouter()
router.register(r'member-request', MemberRequestViewSet, basename='member request')
router.register(r'from-before', FormBeforeViewSet, basename='from before')
router.register(r'problem-area', ProblemAreaViewSet, basename='problem area')

urlpatterns = router.urls
