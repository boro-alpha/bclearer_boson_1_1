from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_CONVERT_FILENAME
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_REMOVE_FILENAME
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_CONVERT_FILENAME_HDF5
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_filename_constants import ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_REMOVE_FILENAME_HDF5
from bclearer_boson_1_1_source.b_code.configurations.resource_constants.resources_namespace_constants import ADJUSTMENT_OPERATIONS_RESOURCES_NAMESPACE
from bclearer_source.b_code.common_knowledge.adjustment_operation_types import AdjustmentOperationTypes
from bclearer_source.b_code.configurations.adjustment_operation_configurations import AdjustmentOperationConfigurations
from bclearer_source.b_code.configurations.adjustment_operations_substage_configurations import AdjustmentOperationsSubstageConfigurations
from bclearer_source.b_code.configurations.attribute_to_association_adjustment_operation_configurations import AttributeToAssociationAdjustmentOperationConfigurations
from bclearer_source.b_code.configurations.load_ea_model_configurations import LoadEaModelConfigurations
from bclearer_source.b_code.configurations.load_hdf5_model_configurations import LoadHdf5ModelConfigurations
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_association_direction_types import EaAssociationDirectionTypes


def get_boson_1_2e_b1_configuration_load_ea_attributes_to_convert() \
        -> LoadEaModelConfigurations:
    load_ea_model_configuration = \
        LoadEaModelConfigurations(
            resource_namespace=ADJUSTMENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_name=ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_CONVERT_FILENAME,
            short_name='2e_b1_input_adj_uni_convert')

    return \
        load_ea_model_configuration


def get_boson_1_2e_b2_configuration_load_ea_attributes_to_remove() \
        -> LoadEaModelConfigurations:
    load_ea_model_configuration = \
        LoadEaModelConfigurations(
            resource_namespace=ADJUSTMENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_name=ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_REMOVE_FILENAME,
            short_name='2e_b2_input_adj_uni_remove')

    return \
        load_ea_model_configuration


def get_boson_1_2e_b1_configuration_load_hdf5_attributes_to_convert() \
        -> LoadHdf5ModelConfigurations:
    load_hdf5_model_configuration = \
        LoadHdf5ModelConfigurations(
            resource_namespace=ADJUSTMENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_file_name=ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_CONVERT_FILENAME_HDF5,
            universe_short_name='2e_b1_input_adj_uni_convert')

    return \
        load_hdf5_model_configuration


def get_boson_1_2e_b2_configuration_load_hdf5_attributes_to_remove() \
        -> LoadHdf5ModelConfigurations:
    load_hdf5_model_configuration = \
        LoadHdf5ModelConfigurations(
            resource_namespace=ADJUSTMENT_OPERATIONS_RESOURCES_NAMESPACE,
            resource_file_name=ADJUSTMENT_UNIVERSE_OS_INSPIRE_ATTRIBUTES_TO_REMOVE_FILENAME_HDF5,
            universe_short_name='2e_b2_input_adj_uni_remove')

    return \
        load_hdf5_model_configuration


def get_boson_1_2e_b_configuration_clean_inspire() \
        -> AdjustmentOperationsSubstageConfigurations:
    convert_attributes_to_associations_adjustment_operation_configuration = \
        AttributeToAssociationAdjustmentOperationConfigurations(
            adjustment_operation_type=AdjustmentOperationTypes.CONVERT_ATTRIBUTES_TO_ASSOCIATIONS,
            adjustment_universe_load_hdf5_model_configuration=get_boson_1_2e_b1_configuration_load_hdf5_attributes_to_convert(),
            output_universe_short_name='2e_b1_output_convert',
            direction=EaAssociationDirectionTypes.BACKWARD,
            package_name='2e_b1_new_objects')

    remove_attributes_adjustment_operation_configuration = \
        AdjustmentOperationConfigurations(
            adjustment_operation_type=AdjustmentOperationTypes.REMOVE_ATTRIBUTES,
            adjustment_universe_load_hdf5_model_configuration=get_boson_1_2e_b2_configuration_load_hdf5_attributes_to_remove(),
            output_universe_short_name='2e_b2_output_remove')

    clean_inspire_adjustment_operations_substage_configuration = \
        AdjustmentOperationsSubstageConfigurations(
            operation_configurations={
                convert_attributes_to_associations_adjustment_operation_configuration,
                remove_attributes_adjustment_operation_configuration})

    return \
        clean_inspire_adjustment_operations_substage_configuration
