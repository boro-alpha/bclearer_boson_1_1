from bclearer_boson_1_1_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.bespoke_name_to_instance_configuration_objects import BespokeNameToInstanceConfigurationObjects
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations


def get_boson_1_2e_k1_configuration_separate_standard_names_and_instances() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_STANDARD_NAMES_AND_INSTANCES,
            output_universe_short_name='2e_k1_output_sep_standard_instances',
            package_name='2e_k1_new_objects_sep_standard_instances')

    return \
        convention_shift_operation_configuration


def get_boson_1_2e_k2_configuration_bespoke_standard_names_and_instances() \
        -> ConventionShiftOperationConfigurations:
    list_of_configuration_objects = \
        [
            BespokeNameToInstanceConfigurationObjects(
                matched_naming_space_type=InspireMatchedEaObjects.IDENTIFIER,
                name_instance_attribute_name=InspireMatchedEaObjects.LOCAL_ID_ATTRIBUTE.object_name,
                package_name='2e_k2_new_objects_sep_bespoke_instances'),
            BespokeNameToInstanceConfigurationObjects(
                matched_naming_space_type=InspireMatchedEaObjects.GEOGRAPHICAL_NAME,
                matched_name_instance_type=InspireMatchedEaObjects.SPELLING_OF_NAME)
        ]

    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_BESPOKE_NAMES_AND_INSTANCES,
            output_universe_short_name='2e_k2_output_sep_bespoke_instances',
            list_of_configuration_objects=list_of_configuration_objects,
            package_name='2e_k2_new_objects_sep_bespoke_instances')

    return \
        convention_shift_operation_configuration
