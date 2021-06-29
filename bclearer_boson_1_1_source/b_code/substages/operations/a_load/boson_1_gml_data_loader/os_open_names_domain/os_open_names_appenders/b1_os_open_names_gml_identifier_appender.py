import untangle
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes


def append_gml_identifier(
        os_open_names_dictionary: dict,
        gml_identifier: untangle.Element,
        named_place_uuid: str) \
        -> dict:
    gml_identifier_uuid = \
        create_new_uuid()

    value = \
        gml_identifier.cdata

    code_space = \
        gml_identifier['codeSpace']

    os_open_names_dictionary['gml_identifiers'][gml_identifier_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gml_identifier_uuid,
            'owning_nf_uuids': named_place_uuid,
            'codeSpace': code_space,
            'value': value
        }

    return \
        os_open_names_dictionary
