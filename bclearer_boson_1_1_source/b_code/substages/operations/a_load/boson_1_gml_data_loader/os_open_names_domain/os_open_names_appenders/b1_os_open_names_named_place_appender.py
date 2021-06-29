import untangle
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_os_open_names_gml_identifier_appender import append_gml_identifier
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_os_open_names_gn_inspire_id_appender import append_gn_inspire_id
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_os_open_names_name_appender import append_gn_name
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid


def append_named_place(
        os_open_names_dictionary: dict,
        named_place: untangle.Element,
        file_uuid: str) \
        -> dict:
    named_place_uuid = \
        create_new_uuid()

    if isinstance(named_place.gn_name, list):
        presentation_prefix = named_place.gn_name[0].gn_GeographicalName.gn_spelling.gn_SpellingOfName.gn_text.cdata

    else:
        presentation_prefix = named_place.gn_name.gn_GeographicalName.gn_spelling.gn_SpellingOfName.gn_text.cdata

    os_open_names_dictionary['named_places'][named_place_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: named_place_uuid,
            'file_uuids': file_uuid,
            'name': presentation_prefix + ' Named Place'
        }

    os_open_names_dictionary = \
        append_gml_identifier(
            os_open_names_dictionary=os_open_names_dictionary,
            gml_identifier=named_place.gml_identifier,
            named_place_uuid=named_place_uuid)

    os_open_names_dictionary = \
        append_gn_inspire_id(
            os_open_names_dictionary=os_open_names_dictionary,
            gn_inspire_id=named_place.gn_inspireId.base_Identifier,
            named_place_uuid=named_place_uuid,
            presentation_prefix=presentation_prefix)

    if isinstance(named_place.gn_name, list):
        for gn_name in named_place.gn_name:
            os_open_names_dictionary = \
                append_gn_name(
                    gn_name=gn_name,
                    named_place_uuid=named_place_uuid,
                    os_open_names_dictionary=os_open_names_dictionary,
                    presentation_prefix=presentation_prefix)
    else:
        os_open_names_dictionary = \
            append_gn_name(
                gn_name=named_place.gn_name,
                named_place_uuid=named_place_uuid,
                os_open_names_dictionary=os_open_names_dictionary,
                presentation_prefix=presentation_prefix)

    return \
        os_open_names_dictionary
