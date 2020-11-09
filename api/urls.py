from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from product.views import GetCategoryViewSet,GetProductForHomeViewSet,GetProductImageViewSet,SearchAPIView,ProductViewSet,ProductItemViewSet
from order.views import ProductInBasketViewSet,Order,OrderViewSet,ProductInOrderViewSet
from order.views import ProductInBasket,DeleteProductInBasket,UpdateProductInBasket
from blog.views import BlogViewSet,TegViewSet
from users.views import UserViewSet,SendMailForNewEmail,PasswordResetView
from userCabinet.views import ClientViewSet
from home.views import BigSliderViewSet,AdvertisingImageViewSet
from wishlist.views import WishlistPost,WishlistViewSet,DeleteWishlist
from quethen.views import QuethenViewSet
from skafi.views import *
from kuhni.views import KuhniViewSet,KuhniPodcategViewSet,GetKuhniImageViewSet
from gostinye.views import GostinyeViewSet,GostinyePodcategViewSet,GetGostinyeImageViewSet
from prihozhie.views import PrihozhieViewSet,PrihozhiePodcategViewSet,GetPrihozhieImageViewSet
from spalni.views import SpalniViewSet,SpalniPodcategViewSet,GetSpalniImageViewSet
from detskie.views import DetskieViewSet,DetskiePodcategViewSet,GetDetskieImageViewSet
from derevyannayamebel.views import DerevyannayamebelViewSet,DerevyannayamebelPodcategViewSet
from myagkayamebel.views import MyagkayamebelViewSet,MyagkayamebelPodcategViewSet,GetMyagkayamebelImageViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'register', UserRegisterViewSet)
router.register(r'postel', ProductViewSet)
# router.register(r'product', ProductItemViewSet)
router.register(r'producthome', GetProductForHomeViewSet)
# вывод одного шкафа
router.register(r'category',GetCategoryViewSet)
router.register(r'shkafy-kupe', SkafViewSet)
router.register(r'pristavki-k-shkafam-kupe', SkafViewSet)
router.register(r'shkaf', SkafViewSet)
router.register(r'shkafy-kupepodcateg', SkafPodcategViewSet)
router.register(r'height', SkafHeightViewSet)
router.register(r'deep', SkafDeepViewSet)
router.register(r'widht', SkafWidhtViewSet)
router.register(r'brend', SkafBrendViewSet)
router.register(r'gallerySkaf',  GetSkafImageViewSet)
router.register(r'galleryKuhni',GetKuhniImageViewSet) 
router.register(r'galleryGostiny',GetGostinyeImageViewSet)
router.register(r'galleryPrihozhie',GetPrihozhieImageViewSet)
router.register(r'gallerySpalni',GetSpalniImageViewSet)
router.register(r'galleryDetskie',GetDetskieImageViewSet)
router.register(r'galleryMyagkayamebel',GetMyagkayamebelImageViewSet)
router.register(r'kuhni',KuhniViewSet)
router.register(r'kuhnipodcateg',KuhniPodcategViewSet)
router.register(r'gostinye',GostinyeViewSet)
router.register(r'gostinyepodcateg',GostinyePodcategViewSet)
router.register(r'prihozhie',PrihozhieViewSet)
router.register(r'prihozhiepodcateg',PrihozhiePodcategViewSet)
router.register(r'spalni',SpalniViewSet)
router.register(r'spalnipodcateg',SpalniPodcategViewSet)
router.register(r'detskie',DetskieViewSet)
router.register(r'detskiepodcateg',DetskiePodcategViewSet)
router.register(r'derevyannayamebel',DerevyannayamebelViewSet)
router.register(r'derevyannayamebelpodcateg',DerevyannayamebelPodcategViewSet)
router.register(r'myagkayamebel', MyagkayamebelViewSet)
router.register(r'myagkayamebelpodcateg', MyagkayamebelPodcategViewSet)
router.register(r'productinorder', ProductInBasketViewSet)
router.register(r'getuser',ClientViewSet),
router.register(r'getorder',OrderViewSet),
router.register(r'productinorderbyid',ProductInOrderViewSet),
router.register(r'gallery',GetProductImageViewSet),
router.register(r'bigslider',BigSliderViewSet)
router.register(r'advetising',AdvertisingImageViewSet)
router.register(r'blog',BlogViewSet)
router.register(r'teg',TegViewSet)
router.register(r'wishlist',WishlistViewSet)
router.register(r'quethen',QuethenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('search/', SearchAPIView.as_view()),
    path('productinbasket/', ProductInBasket.as_view()),
    path('deleteproductinbasket/', DeleteProductInBasket.as_view()),
    path('updateproductinbasket/', UpdateProductInBasket.as_view()),
    path('order/',Order.as_view()),
    path('wishlispost/',WishlistPost.as_view()),
    path('deletewishlist/',DeleteWishlist.as_view()),
    path('changepassword/',SendMailForNewEmail.as_view()),
    path('password/reset/confirm/', PasswordResetView.as_view(),),

]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
