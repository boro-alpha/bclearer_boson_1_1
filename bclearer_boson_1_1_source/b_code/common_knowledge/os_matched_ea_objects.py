from enum import unique
from enum import auto
from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects


@unique
class OsMatchedEaObjects(
    MatchedEaObjects):
    NAMED_PLACE = \
        auto()

    MODEL_PACKAGE = \
        auto()

    def __object_name(
            self) \
            -> str:
        object_name = \
            object_name_mapping[self]

        return \
            object_name

    def __ea_guid(
            self) \
            -> str:
        ea_guid = \
            ea_guid_mapping[self]

        return \
            ea_guid

    object_name = \
        property(
            fget=__object_name)

    ea_guid = \
        property(
            fget=__ea_guid)


object_name_mapping = \
    {
        OsMatchedEaObjects.NAMED_PLACE: 'NamedPlace',
        OsMatchedEaObjects.MODEL_PACKAGE: 'OS OpenData Product Models - keep'
    }


ea_guid_mapping = \
    {
        OsMatchedEaObjects.NAMED_PLACE: '{3713CCC7-0651-498f-843D-5EA94B746A93}',
        OsMatchedEaObjects.MODEL_PACKAGE: '{DF1B8D7E-4497-49bb-98E7-B187AEE4630D}'
    }
