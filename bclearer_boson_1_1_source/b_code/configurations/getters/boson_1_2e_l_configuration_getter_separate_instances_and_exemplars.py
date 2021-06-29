from bclearer_boson_1_1_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.bespoke_instance_to_exemplar_configuration_objects import BespokeInstanceToExemplarConfigurationObjects
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations


def get_boson_1_2e_l1_configuration_separate_standard_instances_and_names() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_STANDARD_INSTANCES_AND_EXEMPLARS,
            output_universe_short_name='2e_l1_output_sep_standard_exemplars',
            package_name='2e_l1_new_objects_sep_standard_exemplars')

    return \
        convention_shift_operation_configuration


def get_boson_1_2e_l2_configuration_separate_bespoke_instances_and_names() \
        -> ConventionShiftOperationConfigurations:
    list_of_configuration_objects = \
        [
            BespokeInstanceToExemplarConfigurationObjects(
                matched_name_instance_instance=InspireMatchedEaObjects.SPELLING_OF_NAME,
                name_exemplar_attribute_name=InspireMatchedEaObjects.TEXT_ATTRIBUTE.object_name)
        ]

    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.SEPARATE_BESPOKE_INSTANCES_AND_EXEMPLARS,
            output_universe_short_name='2e_l2_output_sep_bespoke_exemplars',
            list_of_configuration_objects=list_of_configuration_objects,
            package_name='2e_l2_new_objects_sep_bespoke_exemplars')

    return \
        convention_shift_operation_configuration
