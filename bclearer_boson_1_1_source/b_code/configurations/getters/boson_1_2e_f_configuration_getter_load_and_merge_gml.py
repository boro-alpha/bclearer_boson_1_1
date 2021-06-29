from bclearer_boson_1_1_source.b_code.configurations.objects.load_gml_data_configurations import LoadGmlDataConfigurations
from bclearer_source.b_code.common_knowledge.content_operation_types import ContentOperationTypes
from bclearer_source.b_code.configurations.content_operation_configurations import ContentOperationConfigurations


def get_boson_1_2e_f1_configuration_load_gml_data(
        gml_data_folder_name: str) \
        -> LoadGmlDataConfigurations:
    load_gml_data_configuration = \
        LoadGmlDataConfigurations(
            gml_data_folder_path=gml_data_folder_name,
            short_name='2e_f1_input_cont_uni_gml')

    return \
        load_gml_data_configuration


def get_boson_1_2e_f1_configuration_merge_gml_data() \
        -> ContentOperationConfigurations:
    content_operation_configuration = \
        ContentOperationConfigurations(
            content_operation_type=ContentOperationTypes.MERGE_UNIVERSES,
            output_universe_short_name='2e_f1_output_merge_gml')

    return \
        content_operation_configuration
