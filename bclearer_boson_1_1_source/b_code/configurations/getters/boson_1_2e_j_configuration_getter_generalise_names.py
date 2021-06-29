from bclearer_boson_1_1_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_source.b_code.common_knowledge.bclearer_matched_ea_objects import BclearerMatchedEaObjects
from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations
from bclearer_source.b_code.configurations.generalise_names_configuration_objects import GeneraliseNamesConfigurationObjects


def get_boson_1_2e_j1_configuration_generalise_names() \
        -> ConventionShiftOperationConfigurations:
    list_of_configuration_objects = \
        [
            GeneraliseNamesConfigurationObjects(
                matched_named_object=InspireMatchedEaObjects.NAMED_PLACE,
                matched_naming_space=InspireMatchedEaObjects.IDENTIFIER,
                matched_name=BclearerMatchedEaObjects.NAMES,
                matched_named_by_stereotype=BclearerMatchedEaObjects.NAMED_BY_STEREOTYPE),
            GeneraliseNamesConfigurationObjects(
                matched_named_object=InspireMatchedEaObjects.NAMED_PLACE,
                matched_naming_space=InspireMatchedEaObjects.GEOGRAPHICAL_NAME,
                matched_name=BclearerMatchedEaObjects.NAMES,
                matched_named_by_stereotype=BclearerMatchedEaObjects.NAMED_BY_STEREOTYPE),
        ]

    convention_shift_operation_configuration = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.GENERALISE_NAMES,
            list_of_configuration_objects=list_of_configuration_objects,
            output_universe_short_name='2e_j1_output_gen_names')

    return \
        convention_shift_operation_configuration
