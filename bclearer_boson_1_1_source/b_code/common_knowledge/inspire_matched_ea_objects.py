from enum import unique
from enum import auto
from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects


@unique
class InspireMatchedEaObjects(
    MatchedEaObjects):
    GML_FILES = \
        auto()

    GML_FILE_NAMES = \
        auto()

    NAMED_PLACE = \
        auto()

    CHARACTER_STRING = \
        auto()

    IDENTIFIER = \
        auto()

    GEOGRAPHICAL_NAME = \
        auto()

    SPELLING_OF_NAME = \
        auto()

    MODEL_PACKAGE = \
        auto()

    LOCAL_ID_ATTRIBUTE = \
        auto()

    TEXT_ATTRIBUTE = \
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
        InspireMatchedEaObjects.GML_FILES: 'GML Files',
        InspireMatchedEaObjects.GML_FILE_NAMES: 'GML File Names',
        InspireMatchedEaObjects.NAMED_PLACE: 'NamedPlace',
        InspireMatchedEaObjects.CHARACTER_STRING: 'CharacterString',
        InspireMatchedEaObjects.IDENTIFIER: 'Identifier',
        InspireMatchedEaObjects.GEOGRAPHICAL_NAME: 'GeographicalName',
        InspireMatchedEaObjects.SPELLING_OF_NAME: 'SpellingOfName',
        InspireMatchedEaObjects.MODEL_PACKAGE: 'INSPIRE Consolidated UML Model - keep',
        InspireMatchedEaObjects.LOCAL_ID_ATTRIBUTE: 'localId',
        InspireMatchedEaObjects.TEXT_ATTRIBUTE: 'text'
    }


ea_guid_mapping = \
    {
        InspireMatchedEaObjects.GML_FILES: '{3F93572A-E12C-47d1-BDEF-579CD5E67C40}',
        InspireMatchedEaObjects.GML_FILE_NAMES: '{36FC597B-8B35-4a01-9476-0819D1D37657}',
        InspireMatchedEaObjects.NAMED_PLACE: '{8C3D164C-2A8F-4df9-A35F-C5CFBDE23ABC}',
        InspireMatchedEaObjects.CHARACTER_STRING: '{AF7C81A6-B1C1-4469-A09F-B97989024A14}',
        InspireMatchedEaObjects.IDENTIFIER: '{CB20C133-5AA4-4671-80C7-8ED2879AB0D9}',
        InspireMatchedEaObjects.GEOGRAPHICAL_NAME: '{E548F6CD-653D-4dc7-AAF3-2E510C1453E0}',
        InspireMatchedEaObjects.SPELLING_OF_NAME: '{67BC30C2-B4B5-4a94-9645-FF31C4F25E89}',
        InspireMatchedEaObjects.MODEL_PACKAGE: '{85FDCAF5-BB31-493a-ADE6-CEA426E6F42C}',
        InspireMatchedEaObjects.LOCAL_ID_ATTRIBUTE: '{A63416FC-693C-47d3-9E52-BCF2165F806B}',
        InspireMatchedEaObjects.TEXT_ATTRIBUTE: '{803EBE76-48DF-4391-9523-5BA48A3CA5E0}'
    }
