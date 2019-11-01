import enum


class TopEnum():
    pass


@enum.unique
class BaseEnum(TopEnum, enum.Enum):
    pass


@enum.unique
class BaseIntEnum(TopEnum, enum.IntEnum):
    pass
