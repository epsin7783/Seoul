# urls.py
from django.urls.conf import path
from board import views
app_name = "board"
urlpatterns = [
    path( "list", views.ListView.as_view(), name="list" ),
    path( "bwrite", views.BWriteView.as_view(), name="bwrite" ),
    path( "detail", views.DetailView.as_view(), name="detail" ),
    path( "bdelete", views.BDeleteView.as_view(), name="bdelete" ),
    path( "bmodify", views.BModifyView.as_view(), name="bmodify" ),
    path( "bmodifypro", views.BModifyPro.as_view(), name="bmodifypro" ),
    path( "image", views.ImageView.as_view(), name="image" ),
    path( "guide", views.GuideView.as_view(), name="guide" ),
    # path('board/guide', name="guide"),
    
    
    path( "imagedown", views.ImageDownView.as_view(), name="imagedown" ),
    path( "storage", views.StorageView.as_view(), name="storage" ),
    path( "sql", views.SQLView.as_view(), name="sql" ),
    
    path( "ajax", views.AjaxView.as_view(), name="ajax" ),
    path( "ajaxtext", views.AjaxTextView.as_view(), name="ajaxtext" ),
    path( "ajaxjson", views.AjaxJsonView.as_view(), name="ajaxjson" ),    
    path( "ajaxxml", views.AjaxXMLView.as_view(), name="ajaxxml" ),    
    path( "ajaxxmljson", views.AjaxXMLJsonView.as_view(), name="ajaxxmljson" ),    
    
    path( "commentWrite", views.CommentWriteView.as_view(), name="commentWrite" ), 
    path( "replyDel", views.ReplyDelView.as_view(), name="replyDel" ), 
    path( "replyMod", views.ReplyModView.as_view(), name="replyMod"), 
    ]


























