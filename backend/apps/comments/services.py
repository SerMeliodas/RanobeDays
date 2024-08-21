from .models import Comment

from .types import CommentObject
from apps.novels.models import Novel
from apps.chapters.models import Chapter


def create_comment(data: CommentObject):
    print(data)
    comment = Comment(user=data.user,
                      comment_type=data.comment_type,
                      message=data.message)
    if data.parent:
        comment.parent = Comment.objects.get(pk=data.parent)

    if data.novel and data.comment_type == 'novel':
        comment.novel = Novel.objects.get(slug=data.novel)

        comment.clean()
        comment.save()

        return comment

    if data.chapter and data.comment_type == 'chapter':
        comment.chapter = Chapter.objects.get(pk=data.chapter)

        comment.clean()
        comment.save()

        return comment
