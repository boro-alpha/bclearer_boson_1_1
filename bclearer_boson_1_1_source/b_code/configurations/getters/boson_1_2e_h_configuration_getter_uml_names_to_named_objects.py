from bclearer_boson_1_1_source.b_code.common_knowledge.boson_1_matched_ea_objects import Boson1MatchedEaObjects
from bclearer_boson_1_1_source.b_code.common_knowledge.inspire_matched_ea_objects import InspireMatchedEaObjects
from bclearer_boson_1_1_source.b_code.common_knowledge.os_matched_ea_objects import OsMatchedEaObjects
from bclearer_source.b_code.common_knowledge.bclearer_matched_ea_objects import BclearerMatchedEaObjects
from bclearer_source.b_code.configurations.attribute_name_to_name_object_configuration_objects import AttributeNameToNameObjectConfigurationObjects
from bclearer_source.b_code.configurations.uml_name_to_named_object_configuration_objects import UmlNameToNamedObjectConfigurationObjects
from bclearer_source.b_code.common_knowledge.convention_shift_operation_types import ConventionShiftOperationTypes
from bclearer_source.b_code.configurations.convention_shift_operation_configurations import ConventionShiftOperationConfigurations


def get_boson_1_2e_h1_configuration_uml_names_to_named_objects() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_uml_names_to_named_objects_list_of_configuration_objects = [
        UmlNameToNamedObjectConfigurationObjects(
            matched_package=InspireMatchedEaObjects.MODEL_PACKAGE,
            matched_naming_space=Boson1MatchedEaObjects.INSPIRE_OBJECT_NAMES),
        UmlNameToNamedObjectConfigurationObjects(
            matched_package=OsMatchedEaObjects.MODEL_PACKAGE,
            matched_naming_space=Boson1MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES),
        UmlNameToNamedObjectConfigurationObjects(
            matched_package=BclearerMatchedEaObjects.MODEL_PACKAGE,
            matched_naming_space=BclearerMatchedEaObjects.BCLEARER_FOUNDATION_COMMON_RESERVED_NAMES),
        UmlNameToNamedObjectConfigurationObjects(
            matched_package=Boson1MatchedEaObjects.MODEL_PACKAGE,
            matched_naming_space=Boson1MatchedEaObjects.BOSON_NAMES)
    ]

    convention_shift_operation_configuration_uml_names_to_named_objects = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.UML_NAME_TO_NAMED_OBJECT,
            list_of_configuration_objects=convention_shift_uml_names_to_named_objects_list_of_configuration_objects,
            output_universe_short_name='2e_h1_output_uml_to_attr')

    return \
        convention_shift_operation_configuration_uml_names_to_named_objects


def get_boson_1_2e_h2_configuration_uml_name_attributes_to_name_objects() \
        -> ConventionShiftOperationConfigurations:
    convention_shift_attribute_names_to_name_objects_list_of_configuration_objects = [
        AttributeNameToNameObjectConfigurationObjects(
            matched_naming_space_instance=Boson1MatchedEaObjects.INSPIRE_OBJECT_NAMES),
        AttributeNameToNameObjectConfigurationObjects(
            matched_naming_space_instance=Boson1MatchedEaObjects.OS_GAZETTEER_OBJECT_NAMES),
        AttributeNameToNameObjectConfigurationObjects(
            matched_naming_space_instance=BclearerMatchedEaObjects.BCLEARER_FOUNDATION_COMMON_RESERVED_NAMES),
        AttributeNameToNameObjectConfigurationObjects(
            matched_naming_space_instance=Boson1MatchedEaObjects.BOSON_NAMES)
    ]

    convention_shift_operation_configuration_attribute_names_to_name_objects = \
        ConventionShiftOperationConfigurations(
            convention_shift_operation_type=ConventionShiftOperationTypes.ATTRIBUTE_NAME_TO_NAMED_OBJECT,
            list_of_configuration_objects=convention_shift_attribute_names_to_name_objects_list_of_configuration_objects,
            output_universe_short_name='2e_h2_output_uml_attr_to_ass')

    return \
        convention_shift_operation_configuration_attribute_names_to_name_objects
