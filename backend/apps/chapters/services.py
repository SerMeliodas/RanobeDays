from .models import Chapter
from .types import ChapterObject

from apps.novels.models import Novel
from apps.common.services import model_update


def create_chapter(data: ChapterObject) -> Chapter:
    novel = Novel.objects.get(pk=data.novel)
    chapter = Chapter(title=data.title, novel=novel, text=data.text)
    chapter.full_clean()
    chapter.save()

    return chapter


def update_chapter(data: ChapterObject, pk: int) -> Chapter:
    fields = ["title", "novel", "text"]

    chapter, _ = model_update(instance=Chapter, fields=fields,
                              data=data.dict(), auto_updated_at=True)

    return chapter
