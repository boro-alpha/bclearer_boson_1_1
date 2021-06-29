from bclearer_boson_1_1_source.b_code.configurations.objects.load_gml_data_configurations import LoadGmlDataConfigurations
from bclearer_boson_1_1_source.b_code.substages.operations.b_evolve.runners.gml_data_to_content_universe_loader import load_gml_data_into_content_universe
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


def run_boson_1_merge_gml_data_content_operations_substage(
        ea_tools_session_manager: EaToolsSessionManagers,
        content_universe: NfEaComUniverses,
        load_gml_data_configuration: LoadGmlDataConfigurations)\
        -> NfEaComUniverses:
    output_universe = \
        load_gml_data_into_content_universe(
            content_universe=content_universe,
            ea_tools_session_manager=ea_tools_session_manager,
            load_gml_data_configuration=load_gml_data_configuration)

    return \
        output_universe
