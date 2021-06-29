from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import CONTENT_UNIVERSE_OS_INSPIRE_FILENAME
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import CONTENT_UNIVERSE_OS_INSPIRE_FILENAME_HDF5
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_namespace_constants import CONTENT_OPERATIONS_RESOURCES_NAMESPACE
from bclearer_source.b_code.configurations.load_ea_model_configurations import LoadEaModelConfigurations
from bclearer_source.b_code.configurations.load_hdf5_model_configurations import LoadHdf5ModelConfigurations


def get_boson_1_1l_a1_configuration_load_ea_os_inspire_filtered() \
        -> LoadEaModelConfigurations:
    load_ea_model_configuration = \
        LoadEaModelConfigurations(
            resource_namespace=CONTENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_name=CONTENT_UNIVERSE_OS_INSPIRE_FILENAME,
            short_name='1l_a1_output_os_inspire')

    return \
        load_ea_model_configuration


def get_boson_1_1l_a1_configuration_load_hdf5_os_inspire_filtered() \
        -> LoadHdf5ModelConfigurations:
    load_hdf5_model_configuration = \
        LoadHdf5ModelConfigurations(
            resource_namespace=CONTENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_file_name=CONTENT_UNIVERSE_OS_INSPIRE_FILENAME_HDF5,
            universe_short_name='1l_a1_output_os_inspire')

    return \
        load_hdf5_model_configuration
