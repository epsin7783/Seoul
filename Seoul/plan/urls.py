from django.urls.conf import path
from plan import views

app_name = "plan"
urlpatterns = [
        path( "planwrite", views.PlanView.as_view(), name="planwrite" ),
        path( "planWriteView", views.PlanWriteView.as_view(), name="planWriteView" ),
        
        path( "wishlist", views.WishlistView.as_view(), name="wishlist" ),
        
        path( "plansharepage", views.PlanShareView.as_view(), name="plansharepage" ),
        path( "plansharedetail", views.PlanShareDetailView.as_view(), name="plansharedetail" ),
        path( "planlike", views.PlanLikeView.as_view(), name="planlike" ),
        path( "plansharewrite", views.PlanShareWriteView.as_view(), name="plansharewrite" ),
        path( "planselect", views.PlanSelectView.as_view(), name="planselect" ),
        
        path( "commentWrite", views.CommentWriteView.as_view(), name="commentWrite" ), 
        path( "replyDel", views.ReplyDelView.as_view(), name="replyDel" ), 
        path( "replyMod", views.ReplyModView.as_view(), name="replyMod"), 
        
        path( "planguide", views.PlanGuideView.as_view(), name="planguide"), 
        
    ]