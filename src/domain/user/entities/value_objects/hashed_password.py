from dataclasses import dataclass

from src.domain.common.entities.value_objects.value_object import ValueObject


@dataclass
class HashedPassword(ValueObject, str):
    value: str
