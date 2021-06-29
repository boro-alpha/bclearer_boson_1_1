from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_1l_a_configuration_getter_load_os_inspire_filtered import get_boson_1_1l_a1_configuration_load_hdf5_os_inspire_filtered
from bclearer_source.b_code.substages.operations.a_load.content_operations.runners.hdf5_to_content_universe_loader import load_hdf5_model_to_content_universe
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def orchestrate_boson_1_load_stage(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str) \
        -> NfEaComUniverses:
    os_inspire_filtered_universe = \
        load_hdf5_model_to_content_universe(
            ea_tools_session_manager=ea_tools_session_manager,
            load_hdf5_model_configuration=get_boson_1_1l_a1_configuration_load_hdf5_os_inspire_filtered())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=os_inspire_filtered_universe)

    return \
        os_inspire_filtered_universe
