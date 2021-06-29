from pathlib import Path
from nf_common_source.code.services.log_environment_utility_service.loggers.environ_logger import log_filtered_environ_items
from nf_common_source.code.services.reporting_service.reporters.log_file import LogFiles
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import log_timing_header


def set_up_logger_and_output_folder(
        output_folder_name: str):
    output_folder = \
        Path(
            output_folder_name)

    output_folder.mkdir(
        parents=True,
        exist_ok=True)

    LogFiles.open_log_file(
        folder_path=output_folder_name)

    log_timing_header()

    log_filtered_environ_items()

    return \
        output_folder


def close_log_file():
    log_message(
        'DONE')

    LogFiles.close_log_file()
