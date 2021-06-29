from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame


def convert_os_open_names_dictionary_dictionary_to_dataframe_dictionary(
        os_open_names_dictionary_dictionary: dict) \
        -> dict:
    log_message(
        message='converting os_open_names_dictionaries to dataframes')

    os_open_names_dataframe_dictionary = \
        {}

    for dataframe_name, os_open_names_dictionary in os_open_names_dictionary_dictionary.items():
        os_open_names_dataframe_dictionary = \
            __add_os_open_names_dataframe(
                os_open_names_dataframe_dictionary=os_open_names_dataframe_dictionary,
                dataframe_name=dataframe_name,
                os_open_names_dictionary=os_open_names_dictionary)

    return \
        os_open_names_dataframe_dictionary


def __add_os_open_names_dataframe(
        os_open_names_dataframe_dictionary: dict,
        dataframe_name: str,
        os_open_names_dictionary: dict) \
        -> dict:
    log_message(
        message='converting ' + str(dataframe_name))

    os_open_names_dataframe = \
        __convert_os_open_names_dictionary_to_dataframe(
            os_open_names_dictionary=os_open_names_dictionary)

    os_open_names_dataframe_dictionary[dataframe_name] = \
        os_open_names_dataframe

    return \
        os_open_names_dataframe_dictionary


def __convert_os_open_names_dictionary_to_dataframe(
        os_open_names_dictionary: dict) \
        -> DataFrame:
    os_open_names_dataframe = \
        DataFrame(
            os_open_names_dictionary)

    os_open_names_dataframe = \
        os_open_names_dataframe.transpose()

    os_open_names_dataframe = \
        os_open_names_dataframe.reset_index(
            drop=True)

    return \
        os_open_names_dataframe
