from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_clean_inspire_os_model_runner import run_visualization_substage_clean_inspire_os_model
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_generalise_names_runner import run_visualization_substage_generalise_names
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_generalise_runner import run_visualization_substage_generalise
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_load_gml_data_runner import run_visualization_substage_load_gml_data
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_separate_instances_and_exemplars_runner import run_visualization_substage_separate_instances_and_exemplars
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_separate_names_and_instances_runner import run_visualization_substage_separate_names_and_instances
from bclearer_boson_1_1_source.b_code.substages.visualization_substages.boson_1_visualization_substage_separate_objects_and_names_runner import run_visualization_substage_separate_objects_and_names
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def orchestrate_boson_1_evolve_stage(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        gml_data_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    os_inspire_filtered_universe = \
        run_visualization_substage_clean_inspire_os_model(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=content_universe)

    generalised_names_universe = \
        run_visualization_substage_generalise(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=os_inspire_filtered_universe)

    added_gml_data_universe = \
        run_visualization_substage_load_gml_data(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            gml_data_folder_name=gml_data_folder_name,
            content_universe=generalised_names_universe)

    separated_objects_and_names_universe = \
        run_visualization_substage_separate_objects_and_names(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=added_gml_data_universe)

    generalised_names_universe = \
        run_visualization_substage_generalise_names(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=separated_objects_and_names_universe)

    separated_names_and_instances_universe = \
        run_visualization_substage_separate_names_and_instances(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=generalised_names_universe)

    separated_instances_and_exemplars_universe = \
        run_visualization_substage_separate_instances_and_exemplars(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder_name=output_folder_name,
            content_universe=separated_names_and_instances_universe)

    return \
        separated_instances_and_exemplars_universe
