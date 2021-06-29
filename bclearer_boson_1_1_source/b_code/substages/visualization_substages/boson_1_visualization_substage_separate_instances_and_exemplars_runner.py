from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_l_configuration_getter_separate_instances_and_exemplars import get_boson_1_2e_l1_configuration_separate_standard_instances_and_names
from bclearer_boson_1_1_source.b_code.configurations.getters.boson_1_2e_l_configuration_getter_separate_instances_and_exemplars import get_boson_1_2e_l2_configuration_separate_bespoke_instances_and_names
from bclearer_source.b_code.substages.operations.b_evolve.convention_shift_operations.runners.convention_shift_operations_substage_runner import run_convention_shift_operation_substage
from bclearer_source.b_code.substages.visualizations.instrumentation_and_visualization_runner import instrument_and_visualize
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def run_visualization_substage_separate_instances_and_exemplars(
        ea_tools_session_manager: EaToolsSessionManagers,
        output_folder_name: str,
        content_universe: NfEaComUniverses) \
        -> NfEaComUniverses:
    separated_standard_instances_and_exemplars_universe = \
        __separate_standard_instances_and_exemplars(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            output_folder_name=output_folder_name)

    separated_bespoke_instances_and_exemplars_universe = \
        __separate_bespoke_instances_and_exemplars(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=separated_standard_instances_and_exemplars_universe,
            output_folder_name=output_folder_name)

    return \
        separated_bespoke_instances_and_exemplars_universe


def __separate_standard_instances_and_exemplars(
        ea_tools_session_manager: EaToolsSessionManagers,
        content_universe: NfEaComUniverses,
        output_folder_name: str) \
        -> NfEaComUniverses:
    separated_standard_instances_and_exemplars_universe = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            convention_shift_operation_configuration=get_boson_1_2e_l1_configuration_separate_standard_instances_and_names())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=separated_standard_instances_and_exemplars_universe)

    return \
        separated_standard_instances_and_exemplars_universe


def __separate_bespoke_instances_and_exemplars(
        ea_tools_session_manager: EaToolsSessionManagers,
        content_universe: NfEaComUniverses,
        output_folder_name: str) \
        -> NfEaComUniverses:
    separated_bespoke_instances_and_exemplars = \
        run_convention_shift_operation_substage(
            ea_tools_session_manager=ea_tools_session_manager,
            content_universe=content_universe,
            convention_shift_operation_configuration=get_boson_1_2e_l2_configuration_separate_bespoke_instances_and_names())

    instrument_and_visualize(
        output_folder_name=output_folder_name,
        visualization_substage_output_universe=separated_bespoke_instances_and_exemplars)

    return \
        separated_bespoke_instances_and_exemplars
