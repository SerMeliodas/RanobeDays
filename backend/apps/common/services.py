from django.db import models
from django.utils import timezone

from pydantic import BaseModel


def get_fields_to_update(data: BaseModel):
    fields = []

    for field, value in data.dict().items():
        if value is not None:
            fields.append(field)

    return fields


def _update_foreign_key_fields(instance: models.Model,
                               fields: dict[str, int]) -> bool:
    for field, value in fields.items():
        model = instance._meta.get_field(field).remote_field.model
        setattr(instance, field, model.objects.get(pk=value))

    return True


def _update_many_to_many_fields(instance: models.Model,
                                many_to_many_fields:
                                dict[str, models.ManyToManyField]
                                ) -> bool:

    for field_name, value in many_to_many_fields.items():
        related_manager = getattr(instance, field_name)
        related_manager.set(value)

    return True


def model_update(*, instance: models.Model, fields: list[str],
                 data: dict[str, any], auto_updated_at: bool = False
                 ) -> tuple[models.Model, bool]:
    has_updated = False
    updated_fields = list()
    many_to_many_fields = dict()
    foreign_key_fields = dict()
    model_fields = {field.name: field for field in instance._meta.fields
                    + instance._meta.many_to_many}

    for field in fields:
        if field not in data:
            continue

        model_field = model_fields.get(field)

        assert model_field is not None, f"{field} is not part of \
        {instance.__class__.__name__} fields"

        if isinstance(model_fields[field], models.ManyToManyField):
            many_to_many_fields[field] = data[field]
            continue

        if getattr(instance, field) != data[field]:
            if isinstance(model_fields[field], models.ForeignKey):
                foreign_key_fields[field] = data[field]
                continue

            has_updated = True
            updated_fields.append(field)
            setattr(instance, field, data[field])

    if has_updated:
        if auto_updated_at:
            if ("updated_at" in model_fields and
                    "updated_at" not in updated_fields):
                updated_fields.append("updated_at")
                instance.updated_at = timezone.now()

        instance.full_clean()
        instance.save(update_fields=updated_fields)

    has_updated = _update_many_to_many_fields(instance, many_to_many_fields)
    has_updated = _update_foreign_key_fields(instance, foreign_key_fields)

    return instance, has_updated
