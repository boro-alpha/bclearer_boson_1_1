from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_i_configuration_getter_attribute_names_to_name_objects import get_boson_1_2e_i1_configuration_name_attributes_to_name_objects
from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_h_configuration_getter_uml_names_to_named_objects import get_boson_1_2e_h1_configuration_uml_names_to_named_objects
from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_h_configuration_getter_uml_names_to_named_objects import get_boson_1_2e_h2_configuration_uml_name_attributes_to_name_objects
from bclearer_source.b_code.substages.operations.b_evolve.convention_shift_operations.runners.convention_shift_operations_substage_runner import run_convention_shift_operation_substage
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def run_visualization_substage_separate_objects_and_names(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    separated_uml_objects_and_names_universe = \
        __separate_uml_objects_and_names(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            output_folder_name=output_folder_name)

    separated_gml_file_objects_and_names_universe = \
        __separate_gml_file_objects_and_names(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=separated_uml_objects_and_names_universe,
            output_folder_name=output_folder_name)

    return \
        separated_gml_file_objects_and_names_universe


def __separate_uml_objects_and_names(
        ea_tools_session_manager: EaToolsSessionManagers,
        content_universe: NfEaComUniverses,
        output_folder_name: str) \
        -> NfEaComUniverses:
    extracted_uml_names_universe = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            convention_shift_operation_configuration=get_boson_1_2e_h1_configuration_uml_names_to_named_objects())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=extracted_uml_names_universe)

    extracted_attribute_names_universe = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=extracted_uml_names_universe,
            convention_shift_operation_configuration=get_boson_1_2e_h2_configuration_uml_name_attributes_to_name_objects())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=extracted_attribute_names_universe)

    return \
        extracted_attribute_names_universe


def __separate_gml_file_objects_and_names(
        ea_tools_session_manager: EaToolsSessionManagers,
        content_universe: NfEaComUniverses,
        output_folder_name: str) \
        -> NfEaComUniverses:
    extracted_attribute_names_universe = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            convention_shift_operation_configuration=get_boson_1_2e_i1_configuration_name_attributes_to_name_objects())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=extracted_attribute_names_universe)

    return \
        extracted_attribute_names_universe
