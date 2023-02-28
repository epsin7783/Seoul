from django.contrib import admin
from board.models import Board, ImageBoard, Comment

class BoardAdmin( admin.ModelAdmin ) :
    list_display = ( "num" ,"writer", "subject", "passwd", "content",
                     "readcount", "ref", "restep", "relevel", "regdate", "ip" )
admin.site.register( Board, BoardAdmin )

class ImageBoardAdmin( admin.ModelAdmin ) :
    list_display = ( "imageid", "title", "image", "name" )
admin.site.register( ImageBoard, ImageBoardAdmin )

class CommentAdmin( admin.ModelAdmin ) :
    list_display = ( "no", "nick", "comment", "date", "boardNum" )
admin.site.register( Comment, CommentAdmin )