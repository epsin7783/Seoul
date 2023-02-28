# urls.py
from django.urls.conf import path
from django.views.generic.base import TemplateView
from member import views

urlpatterns = [
    path( "main", views.MainView.as_view(),name='main' ),
    path( "join", views.JoinView.as_view(), name="join" ), 
    path( "login", views.LoginView.as_view(), name="login" ),
    path( "confirm", views.ConfirmView.as_view(), name="confirm" ),     
    path( "logout", views.LogoutView.as_view(), name="logout" ),
    path( "findid", views.FindIdView.as_view(), name="findid" ),
    path( "findpw", views.FindPwView.as_view(), name="findpw" ),
    path( "changepw", views.ChangePwView.as_view(), name="changepw" ),
    path( "mypage", views.MypageView.as_view(), name="mypage" ),
    path( "mypagedelete", views.MypageDeleteView.as_view(), name="mypagedelete" ),
    path( "mypagemodify", views.MypageModifyView.as_view(), name="mypagemodify" ),
    path( "mypagemodifypro", views.MypageModifyProView.as_view(), name="mypagemodifypro" ),
    path("idchk", views.IdChkView.as_view(), name="idchk"),
    path("mypagedetail", views.MypageDetailView.as_view(), name="mypagedetail"),
    path("nicknamechk", views.NicknameChkView.as_view(), name="nicknamechk"),

    path("plandel", views.PlanDelView.as_view(), name="plandel"),
    path( "wishlist", views.WishlistView.as_view(), name="wishlist" ),
    path("wishlistdetail", views.WishlistDetailView.as_view(), name="wishlistdetail"),
    path("wishdel", views.WishDelView.as_view(), name="wishdel"),  
     
    path("KakaoLogin", views.KakaoLoginView.as_view(), name="KakaoLogin"),  
    path("callback", views.KakaoLoginCallbackView.as_view(), name="callback"),  
    path("NaverLogin", views.NaverLoginView.as_view(), name="NaverLogin"),  
    path("callback2", views.NaverLoginCallback2View.as_view(), name="callback2"),  
    ]