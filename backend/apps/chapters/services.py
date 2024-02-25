from .models import Chapter
from .types import ChapterDTO

from apps.novels.models import Novel
from apps.common.services import model_update


def create_chapter(dto: ChapterDTO) -> Chapter:
    novel = Novel.objects.get(pk=dto.novel)
    chapter = Chapter(title=dto.title, novel=novel, text=dto.text)
    chapter.full_clean()
    chapter.save()

    return chapter


def update_chapter(dto: ChapterDTO, pk: int) -> Chapter:
    fields = ["title", "novel", "text"]

    chapter, _ = model_update(instance=Chapter, fields=fields,
                              data=dto.dict(), auto_updated_at=True)

    return chapter
