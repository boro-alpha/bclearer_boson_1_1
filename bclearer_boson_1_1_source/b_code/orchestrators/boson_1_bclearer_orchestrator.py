import os
from bclearer_boson_1_1_source.b_code.orchestrators.boson_1_bclearer_stages_orchestrator import orchestrate_boson_1_bclearer_stages
from bnop_source.b_code.bnop_facades import BnopFacades
from nf_common_source.code.services.datetime_service.time_helpers.time_getter import now_time_as_string_for_files
from nf_common_source.code.services.file_system_service.folder_selector import select_folder
from nf_ea_com_bnop_source.b_code.nf_ea_com_bnop_facades import NfEaComBnopFacades
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers
from bclearer_boson_1_1_source.b_code.services.logging.set_up_and_close_out_logging import set_up_logger_and_output_folder, close_log_file


def orchestrate_boson1_bclearer():
    output_root_folder_path = \
        __get_output_root_folder_path()

    gml_data_folder = \
        select_folder(
            title='Select GML folder')

    set_up_logger_and_output_folder(
        output_folder_name=output_root_folder_path)

    __process_gml_folder(
        output_folder_name=output_root_folder_path,
        gml_data_folder_name=gml_data_folder.absolute_path_string)

    close_log_file()


def __get_output_root_folder_path() \
        -> str:
    output_folder = \
        select_folder(
            title='Select output folder')

    output_folder_path = \
        output_folder.absolute_path_string

    output_root_folder_path = \
        os.path.join(
            output_folder_path,
            'bOSON_1_' + now_time_as_string_for_files().replace('_', ''))

    os.mkdir(
        output_root_folder_path)

    return \
        output_root_folder_path


def __process_gml_folder(
        output_folder_name: str,
        gml_data_folder_name: str) \
        -> None:
    with EaToolsSessionManagers() \
            as ea_tools_session_manager:

        evolved_universe = \
            orchestrate_boson_1_bclearer_stages(
                ea_tools_session_manager=ea_tools_session_manager,
                output_folder_name=output_folder_name,
                gml_data_folder_name=gml_data_folder_name)

        __export_to_xml(
            evolved_universe=evolved_universe,
            output_folder_name=output_folder_name)


def __export_to_xml(
        evolved_universe,
        output_folder_name) \
        -> None:
    nf_ea_com_bnop_facade = \
        NfEaComBnopFacades()

    nf_ea_com_bnop_facade.migrate_nf_ea_com_universe_to_bnop(
        nf_ea_com_universe=evolved_universe)

    bnop_facade = \
        BnopFacades()

    xml_file_path = \
        os.path.join(
            output_folder_name,
            'bOSON_1.xml')

    bnop_facade.write_bnop_object_to_xml(
        xml_file_path=xml_file_path)
