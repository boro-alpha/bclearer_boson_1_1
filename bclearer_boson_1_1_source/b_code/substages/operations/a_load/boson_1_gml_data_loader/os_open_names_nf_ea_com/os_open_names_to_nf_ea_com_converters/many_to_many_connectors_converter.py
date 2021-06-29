from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.dataframes.nf_ea_com_table_appender import append_nf_ea_com_table
from pandas import DataFrame


def convert_many_to_many_to_connectors(
        os_open_names_dictionary: dict,
        nf_ea_com_dictionary: dict,
        os_open_names_table_name: str,
        client_nf_uuid_column_name: str,
        supplier_nf_uuid_column_name: str,
        connector_name_column_name: str,
        connector_type: str) \
        -> dict:
    os_open_names = \
        os_open_names_dictionary[os_open_names_table_name]

    log_message(
        message='adding ' + str(os_open_names.shape[0]) + ' in ' + os_open_names_table_name + ' to EA Connectors')

    new_ea_connectors = \
        __create_new_ea_connectors(
            os_open_names=os_open_names,
            client_nf_uuid_column_name=client_nf_uuid_column_name,
            supplier_nf_uuid_column_name=supplier_nf_uuid_column_name,
            connector_name_column_name=connector_name_column_name,
            connector_type=connector_type)

    nf_ea_com_dictionary = \
        append_nf_ea_com_table(
            nf_ea_com_dictionary=nf_ea_com_dictionary,
            new_nf_ea_com_collection=new_ea_connectors,
            nf_ea_com_collection_type=NfEaComCollectionTypes.EA_CONNECTORS)

    return \
        nf_ea_com_dictionary


def __create_new_ea_connectors(
        os_open_names: DataFrame,
        client_nf_uuid_column_name: str,
        supplier_nf_uuid_column_name: str,
        connector_name_column_name: str,
        connector_type: str) \
        -> DataFrame:
    filter_and_rename_dictionary = \
        {
            supplier_nf_uuid_column_name: NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name,
            client_nf_uuid_column_name: NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name,
            connector_name_column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name
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

    return \
        new_ea_connectors
