from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_to_nf_ea_com_converters.dependency_connectors_converter import convert_dependency_connectors
from bclearer_source.b_code.common_knowledge.matched_objects import MatchedEaObjects
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.dataframes.nf_ea_com_table_appender import append_nf_ea_com_table
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_element_types import EaElementTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from pandas import DataFrame


def convert_to_classifiers(
        os_open_names_dictionary: dict,
        nf_ea_com_universe: NfEaComUniverses,
        matched_type: MatchedEaObjects,
        os_open_names_table_name: str,
        root_package_nf_uuid: str,
        matched_association: MatchedEaObjects = None) \
        -> NfEaComUniverses:
    os_open_names = \
        os_open_names_dictionary[os_open_names_table_name]

    log_message(
        message='converting ' + str(os_open_names.shape[0]) + ' in ' + os_open_names_table_name + ' to EA Classifiers')

    new_ea_classifiers = \
        __create_new_ea_classifiers(
            os_open_names=os_open_names,
            root_package_nf_uuid=root_package_nf_uuid)

    nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections = \
        append_nf_ea_com_table(
            nf_ea_com_dictionary=nf_ea_com_universe.nf_ea_com_registry.dictionary_of_collections,
            new_nf_ea_com_collection=new_ea_classifiers,
            nf_ea_com_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS)

    nf_ea_com_universe = \
        convert_dependency_connectors(
            os_open_names=os_open_names,
            nf_ea_com_universe=nf_ea_com_universe,
            matched_type=matched_type,
            matched_association=matched_association)

    return \
        nf_ea_com_universe


def __create_new_ea_classifiers(
        os_open_names: DataFrame,
        root_package_nf_uuid: str) \
        -> DataFrame:
    filter_and_rename_dictionary = \
        {
            NfColumnTypes.NF_UUIDS.column_name: NfColumnTypes.NF_UUIDS.column_name,
            'name': NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name
        }

    new_ea_classifiers = \
        dataframe_filter_and_rename(
            dataframe=os_open_names,
            filter_and_rename_dictionary=filter_and_rename_dictionary)

    new_ea_classifiers[NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name] = \
        EaElementTypes.OBJECT.type_name

    new_ea_classifiers[NfEaComColumnTypes.PACKAGEABLE_OBJECTS_PARENT_EA_ELEMENT.column_name] = \
        root_package_nf_uuid

    return \
        new_ea_classifiers
