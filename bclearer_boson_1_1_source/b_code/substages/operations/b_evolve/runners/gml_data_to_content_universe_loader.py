from bclearer_boson_1_1_source.b_code.configurations.objects.load_gml_data_configurations import LoadGmlDataConfigurations
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.b1_os_open_names_domain_tables_creator import create_os_open_names_domain_tables
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_nf_ea_com.os_open_names_domain_to_nf_ea_com_orchestrator import orchestrate_os_open_names_domain_to_nf_ea_com
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


def load_gml_data_into_content_universe(
        content_universe: NfEaComUniverses,
        ea_tools_session_manager: EaToolsSessionManagers,
        load_gml_data_configuration: LoadGmlDataConfigurations) \
        -> NfEaComUniverses:
    log_message(
        message='CONTENT OPERATION: Load GML data to universe - ' +
                load_gml_data_configuration.short_name + ' - started')

    os_open_names_dataframe_dictionary = \
        create_os_open_names_domain_tables(
            folder_path=load_gml_data_configuration.gml_data_folder_path)

    gml_data_content_universe = \
        orchestrate_os_open_names_domain_to_nf_ea_com(
            content_universe=content_universe,
            ea_tools_session_manager=ea_tools_session_manager,
            os_open_names_dictionary=os_open_names_dataframe_dictionary,
            short_name=load_gml_data_configuration.short_name)

    log_message(
        message='CONTENT OPERATION: Load GML data to universe - ' +
                load_gml_data_configuration.short_name + ' - finished')

    return \
        gml_data_content_universe
