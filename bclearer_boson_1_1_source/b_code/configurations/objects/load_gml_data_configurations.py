class LoadGmlDataConfigurations:
    def __init__(
            self,
            gml_data_folder_path: str,
            short_name: str):
        self.gml_data_folder_path = \
            gml_data_folder_path

        self.short_name = \
            short_name

    def __enter__(
            self):
        return \
            self

    def __exit__(
            self,
            exception_type,
            exception_value,
            traceback):
        pass
