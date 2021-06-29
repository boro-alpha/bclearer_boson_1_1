from enum import unique
from enum import auto
from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects


@unique
class Boson1MatchedEaObjects(
    MatchedEaObjects):
    BOSON_NAMES = \
        auto()

    GML_FILE_NAMES = \
        auto()

    INSPIRE_OBJECT_NAMES = \
        auto()

    OS_GAZETTEER_OBJECT_NAMES = \
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
        Boson1MatchedEaObjects.BOSON_NAMES: 'bOSON Names',
        Boson1MatchedEaObjects.GML_FILE_NAMES: 'GML File Names',
        Boson1MatchedEaObjects.INSPIRE_OBJECT_NAMES: 'INSPIRE Object Names',
        Boson1MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES: 'OS Gazetteer Object Names',
        Boson1MatchedEaObjects.MODEL_PACKAGE: 'bOSON_1 Package'
    }


ea_guid_mapping = \
    {
        Boson1MatchedEaObjects.BOSON_NAMES: '{79F53CC0-26DE-439f-9BBB-32E72842514F}',
        Boson1MatchedEaObjects.GML_FILE_NAMES: '{36FC597B-8B35-4a01-9476-0819D1D37657}',
        Boson1MatchedEaObjects.INSPIRE_OBJECT_NAMES: '{0D83D74E-0BE8-4fda-85B2-DC4BD3882C86}',
        Boson1MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES: '{83AF5403-09D5-4305-B050-7688D5FDBD23}',
        Boson1MatchedEaObjects.MODEL_PACKAGE: '{B4F3C8D8-AA28-4f65-9346-7C38D91A43D3}'
    }
