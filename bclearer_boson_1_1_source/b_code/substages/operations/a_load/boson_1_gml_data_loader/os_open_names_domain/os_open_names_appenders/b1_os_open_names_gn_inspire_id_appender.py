import untangle
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes


def append_gn_inspire_id(
        os_open_names_dictionary: dict,
        gn_inspire_id: untangle.Element,
        named_place_uuid: str,
        presentation_prefix: str) \
        -> dict:
    gn_inspire_id_uuid = \
        create_new_uuid()

    gn_inspire_id_local_id = \
        gn_inspire_id.base_localId.cdata

    gn_inspire_id_namespace = \
        gn_inspire_id.base_namespace.cdata

    os_open_names_dictionary['inspire_ids'][gn_inspire_id_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_inspire_id_uuid,
            'name': presentation_prefix + ' Identifier',
            'owning_nf_uuids': named_place_uuid,
            'localId': gn_inspire_id_local_id,
            'namespace': gn_inspire_id_namespace
        }

    return \
        os_open_names_dictionary


def append_gn_inspire_id_from_href(
        os_open_names_dictionary: dict,
        xlink_href: str,
        owning_nf_uuid: str,
        presentation_prefix: str) \
        -> dict:
    gn_inspire_id_uuid = \
        create_new_uuid()

    gn_inspire_id_local_id = \
        xlink_href.split('/')[-1]

    gn_inspire_id_namespace = \
        '/'.join(xlink_href.split('/')[0:-1])

    os_open_names_dictionary['inspire_ids'][gn_inspire_id_uuid] = \
        {
            NfColumnTypes.NF_UUIDS.column_name: gn_inspire_id_uuid,
            'name': presentation_prefix + ' Identifier',
            'owning_nf_uuids': owning_nf_uuid,
            'localId': gn_inspire_id_local_id,
            'namespace': gn_inspire_id_namespace
        }

    return \
        os_open_names_dictionary
