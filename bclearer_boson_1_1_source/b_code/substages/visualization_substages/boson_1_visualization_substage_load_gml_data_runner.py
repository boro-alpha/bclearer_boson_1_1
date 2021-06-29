from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_f_configuration_getter_load_and_merge_gml import get_boson_1_2e_f1_configuration_load_gml_data
from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_g_configuration_getter_objects_to_classes import get_boson_1_2e_g1_configuration_objects_to_classes
from bclearer_boson_1_1_source.b_code.substages.operations.b_evolve.runners.boson_1_merge_gml_data_content_operations_substage_runner import run_boson_1_merge_gml_data_content_operations_substage
from bclearer_source.b_code.substages.operations.b_evolve.convention_shift_operations.runners.convention_shift_operations_substage_runner import run_convention_shift_operation_substage
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def run_visualization_substage_load_gml_data(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        gml_data_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    load_gml_data_configuration = \
        get_boson_1_2e_f1_configuration_load_gml_data(
            gml_data_folder_name=gml_data_folder_name)

    content_universe_merged_gml_data_universe = \
        run_boson_1_merge_gml_data_content_operations_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            load_gml_data_configuration=load_gml_data_configuration)

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=content_universe_merged_gml_data_universe)

    content_universe_objects_shifted_to_classes_universe = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe_merged_gml_data_universe,
            convention_shift_operation_configuration=get_boson_1_2e_g1_configuration_objects_to_classes())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=content_universe_objects_shifted_to_classes_universe)

    return \
        content_universe_objects_shifted_to_classes_universe
