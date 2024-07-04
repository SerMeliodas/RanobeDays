from .models import Chapter
from .types import ChapterObject

from apps.novels.models import Novel
from apps.translator_teams.models import TranslatorTeam
from apps.common.services import model_update, get_fields_to_update


def create_chapter(data: ChapterObject) -> Chapter:
    novel = Novel.objects.get(pk=data.novel)
    translator_team = TranslatorTeam.objects.get(pk=data.translator_team)
    chapter = Chapter(title=data.title, novel=novel, text=data.text,
                      translator_team=translator_team)
    chapter.full_clean()
    chapter.save()

    return chapter


def update_chapter(data: ChapterObject, pk: int) -> Chapter:
    chapter = Chapter.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    chapter, _ = model_update(instance=chapter, fields=fields,
                              data=data.dict(), auto_updated_at=True)

    return chapter
