from bclearer_boson_1_1_source.b_code.common_knowledge.boson_1_matched_ea_objects import Boson1MatchedEaObjects
from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.attribute_name_to_name_object_configuration_objects import AttributeNameToNameObjectConfigurationObjects
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations


def get_boson_1_2e_i1_configuration_name_attributes_to_name_objects() \
        -> ConventionShiftOperationConfigurations:
    list_of_configuration_objects = \
        [
            AttributeNameToNameObjectConfigurationObjects(
                matched_naming_space_instance=Boson1MatchedEaObjects.GML_FILE_NAMES),
        ]

    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.ATTRIBUTE_NAME_TO_NAMED_OBJECT,
            list_of_configuration_objects=list_of_configuration_objects,
            output_universe_short_name='2e_i1_output_attr_to_obj')

    return \
        convention_shift_operation_configuration
