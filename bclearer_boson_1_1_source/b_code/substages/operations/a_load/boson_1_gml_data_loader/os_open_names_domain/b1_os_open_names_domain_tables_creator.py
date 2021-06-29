import os
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.common.b1_dataframes_dictionary_summeriser import summarise_dataframes_dictionary
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.b1_os_open_names_dictionary_dictionary_to_dataframe_dictionary_converter import convert_os_open_names_dictionary_dictionary_to_dataframe_dictionary
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.b1_os_open_names_initialiser import initialise_os_open_names_dictionary
from bclearer_boson_1_1_source.b_code.substages.operations.a_load.boson_1_gml_data_loader.os_open_names_domain.os_open_names_appenders.b1_os_open_names_dictionary_appender import append_os_open_names_dictionary
from pathlib import Path
from nf_common_source.code.services.file_system_service.objects.files import Files


def create_os_open_names_domain_tables(
        folder_path: str) \
        -> dict:
    os_open_names_dictionary_dictionary = \
        initialise_os_open_names_dictionary()

    for root, dirs, file_names in os.walk(folder_path):
        os_open_names_dictionary_dictionary = \
            __process_files(
                os_open_names_dictionary_dictionary=os_open_names_dictionary_dictionary,
                root=root,
                file_names=file_names)

    os_open_names_dataframe_dictionary = \
        convert_os_open_names_dictionary_dictionary_to_dataframe_dictionary(
            os_open_names_dictionary_dictionary=os_open_names_dictionary_dictionary)

    summarise_dataframes_dictionary(
        dataframes_dictionary=os_open_names_dataframe_dictionary)

    return \
        os_open_names_dataframe_dictionary


def __process_files(
        os_open_names_dictionary_dictionary: dict,
        root: str,
        file_names: list) \
        -> dict:
    for file_name in file_names:
        os_open_names_dictionary_dictionary = \
            __process_file(
                os_open_names_dictionary_dictionary=os_open_names_dictionary_dictionary,
                root=root,
                file_name=file_name)

    return \
        os_open_names_dictionary_dictionary


def __process_file(
        os_open_names_dictionary_dictionary: dict,
        root: str,
        file_name: str) \
        -> dict:
    root_path = \
        Path(
            root)

    file_path = \
        root_path.joinpath(
            file_name)

    os_open_names_dictionary_dictionary = \
        append_os_open_names_dictionary(
            os_open_names_dictionary=os_open_names_dictionary_dictionary,
            file=Files(absolute_path_string=str(file_path)))

    return \
        os_open_names_dictionary_dictionary

