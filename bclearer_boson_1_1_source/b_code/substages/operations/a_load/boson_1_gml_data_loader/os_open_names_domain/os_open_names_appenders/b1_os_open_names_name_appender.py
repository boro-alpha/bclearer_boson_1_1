import untangle
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes


def append_gn_name(
        os_open_names_dictionary: dict,
        gn_name: untangle.Element,
        named_place_uuid: str,
        presentation_prefix: str):
    gn_name_uuid = \
        create_new_uuid()

    os_open_names_dictionary['gn_GeographicalNames'][gn_name_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_name_uuid,
            'name': presentation_prefix + ' Geographical Name',
            'owning_nf_uuids': named_place_uuid
        }

    gn_spelling = \
        gn_name.gn_GeographicalName.gn_spelling

    gn_spelling_uuid = \
        create_new_uuid()

    text = \
        gn_spelling.gn_SpellingOfName.gn_text.cdata

    script = \
        gn_spelling.gn_SpellingOfName.gn_script.cdata

    os_open_names_dictionary['gn_spellingOfNames'][gn_spelling_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_spelling_uuid,
            'name': presentation_prefix + ' Spelling Of Name',
            'owning_nf_uuids': gn_name_uuid,
            'text': text,
            'script': script
        }

    return os_open_names_dictionary


def append_simple_name(
        os_open_names_dictionary: dict,
        gn_name_text: str,
        named_place_uuid: str,
        presentation_prefix: str):
    gn_name_uuid = \
        create_new_uuid()

    os_open_names_dictionary['gn_GeographicalNames'][gn_name_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_name_uuid,
            'name': presentation_prefix + ' Geographical Name',
            'owning_nf_uuids': named_place_uuid
        }

    gn_spelling_uuid = \
        create_new_uuid()

    os_open_names_dictionary['gn_spellingOfNames'][gn_spelling_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_spelling_uuid,
            'name': presentation_prefix + ' Spelling Of Name',
            'owning_nf_uuids': gn_name_uuid,
            'text': gn_name_text
        }

    return os_open_names_dictionary
