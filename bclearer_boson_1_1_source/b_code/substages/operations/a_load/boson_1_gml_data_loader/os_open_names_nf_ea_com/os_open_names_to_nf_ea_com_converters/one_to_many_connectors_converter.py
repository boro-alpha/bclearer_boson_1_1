from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.dataframes.nf_ea_com_table_appender import append_nf_ea_com_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def convert_one_to_many_to_connectors(
        os_open_names_dictionary: dict,
        nf_ea_com_universe: NfEaComUniverses,
        os_open_names_table_name: str,
        connector_name: str,
        connector_type: str) \
        -> NfEaComUniverses:
    os_open_names = \
        os_open_names_dictionary[os_open_names_table_name]

    log_message(
        message='adding ' + str(os_open_names.shape[0]) + ' in ' + os_open_names_table_name + ' to EA Connectors')

    new_ea_connectors = \
        __create_new_ea_connectors(
            os_open_names=os_open_names,
            connector_name=connector_name,
            connector_type=connector_type)

    nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections = \
        append_nf_ea_com_table(
            nf_ea_com_dictionary=nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections,
            new_nf_ea_com_collection=new_ea_connectors,
            nf_ea_com_collection_type=NfEaComCollectionTypes.EA_CONNECTORS)

    return \
        nf_ea_com_universe


def __create_new_ea_connectors(
        os_open_names: DataFrame,
        connector_name: str,
        connector_type: str) \
        -> DataFrame:
    filter_and_rename_dictionary = \
        {
            'owning_nf_uuids': NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name,
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

    new_ea_connectors[NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name] = \
        connector_type

    new_ea_connectors[NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name] = \
        connector_name

    return \
        new_ea_connectors
