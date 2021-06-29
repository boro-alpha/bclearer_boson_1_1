from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations


def get_boson_1_2e_g1_configuration_objects_to_classes() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.OBJECTS_TO_CLASSES,
            list_of_configuration_objects=[],
            output_universe_short_name='2e_g1_output_shift_obj_to_class')

    return \
        convention_shift_operation_configuration
