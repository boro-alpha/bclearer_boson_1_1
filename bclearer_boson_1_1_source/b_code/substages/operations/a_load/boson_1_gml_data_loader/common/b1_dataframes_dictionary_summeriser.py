from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message


def summarise_dataframes_dictionary(
        dataframes_dictionary: dict):
    for key, value in dataframes_dictionary.items():
        log_message(
            message='dataframe ' + str(key) + ' has shape ' + str(value.shape))
