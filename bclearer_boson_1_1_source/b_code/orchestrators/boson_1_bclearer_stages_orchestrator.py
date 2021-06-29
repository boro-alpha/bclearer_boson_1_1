from bclearer_boson_1_1_source.b_code.orchestrators.boson_1_evolve_stage_orchestrator import orchestrate_boson_1_evolve_stage
from bclearer_boson_1_1_source.b_code.orchestrators.boson_1_load_stage_orchestrator import orchestrate_boson_1_load_stage
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses


@run_and_log_function
def orchestrate_boson_1_bclearer_stages(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        gml_data_folder_name: str)\
        -> NfEaComUniverses:
    content_universe = \
        orchestrate_boson_1_load_stage(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name)

    evolved_universe = \
        orchestrate_boson_1_evolve_stage(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            gml_data_folder_name=gml_data_folder_name,
            content_universe=content_universe)

    return \
        evolved_universe
