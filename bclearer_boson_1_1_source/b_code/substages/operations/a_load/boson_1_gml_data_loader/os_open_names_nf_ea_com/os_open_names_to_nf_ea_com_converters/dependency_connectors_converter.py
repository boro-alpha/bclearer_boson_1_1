from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects
from bclearer_source.b_code.substages.operations.common.intersection_getter import get_intersection_of_dependency_and_association_linked
from bclearer_source.b_code.substages.operations.common.nf_uuid_from_ea_guid_from_collection_getter import get_nf_uuid_from_ea_guid_from_collection
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.dataframes.nf_ea_com_table_appender import append_nf_ea_com_table
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_connector_types import EaConnectorTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def convert_dependency_connectors(
        os_open_names: DataFrame,
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        matched_association: MatchedEaObjects = None) \
        -> NfEaComUniverses:
    log_message(
        message='adding dependencies to EA Connectors')

    new_ea_connectors = \
        __create_new_ea_connectors(
            os_open_names=os_open_names,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=matched_type,
            matched_association=matched_association)

    nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections = \
        append_nf_ea_com_table(
            nf_ea_com_dictionary=nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections,
            new_nf_ea_com_collection=new_ea_connectors,
            nf_ea_com_collection_type=NfEaComCollectionTypes.EA_CONNECTORS)

    return \
        nf_ea_com_universe


def __create_new_ea_connectors(
        os_open_names: DataFrame,
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        matched_association: MatchedEaObjects) \
        -> DataFrame:
    classifier_type_nf_uuid = \
        __get_classifier_type_nf_uuid(
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=matched_type,
            matched_association=matched_association)

    filter_and_rename_dictionary = \
        {
            NfColumnTypes.NF_UUIDS.column_name: NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name
        }

    new_ea_connectors = \
        dataframe_filter_and_rename(
            dataframe=os_open_names,
            filter_and_rename_dictionary=filter_and_rename_dictionary)

    new_ea_connectors[NfColumnTypes.NF_UUIDS.column_name] = \
        new_ea_connectors.apply(
            lambda row:
            create_new_uuid(),
            axis=1)

    new_ea_connectors[NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name] = \
        classifier_type_nf_uuid

    new_ea_connectors[NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name] = \
        EaConnectorTypes.DEPENDENCY.type_name

    return \
        new_ea_connectors


def __get_classifier_type_nf_uuid(
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        matched_association: MatchedEaObjects) -> str:
    matched_type_nf_uuid = \
        get_nf_uuid_from_ea_guid_from_collection(
            nf_ea_com_universe=nf_ea_com_universe,
            collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            ea_guid=matched_type.ea_guid)

    if matched_association is None:
        return \
            matched_type_nf_uuid

    else:
        linked_by_association_nf_uuid = \
            get_nf_uuid_from_ea_guid_from_collection(
                nf_ea_com_universe=nf_ea_com_universe,
                collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
                ea_guid=matched_association.ea_guid)

        return \
            get_intersection_of_dependency_and_association_linked(
                nf_ea_com_universe=nf_ea_com_universe,
                linked_by_dependency_nf_uuid=matched_type_nf_uuid,
                linked_by_association_nf_uuid=linked_by_association_nf_uuid)
