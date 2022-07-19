import logging
import os.path
import yaml


class ConfigFile(object):
    """
    Used to parse a yaml file for the configuration.
    """
    def __init__(self, file_name="test-config.yaml"):
        self.__file_name = file_name
        self.__file_path = self._find_file_path(self.__file_name)
        self.__config = self.load_yaml_file(self.__file_path)

    def _find_file_path(self, file_name: str, file_path: str = "") -> str:
        full_path = f"{file_path}{file_name}"
        try:
            if os.path.exists(full_path):
                return full_path
            else:
                return self._find_file_path(file_name=file_name, file_path=f"../{file_path}")
        except Exception as e:
            logging.error(f"Could not find the specified configuration file: {file_name} ({e})")

        return ""

    @property
    def config(self) -> dict:
        return self.__config

    def load_yaml_file(self, file_path: str) -> dict:
        config = {}
        try:
            with open(file_path, 'r') as fs:
                try:
                    config = yaml.safe_load(fs)
                except yaml.YAMLError as e:
                    logging.error(f"YAML format if wrong: {file_path} ({e})")
        except FileNotFoundError as e:
            logging.error(f"File name doesn't exist: {file_path} ({e})")
            raise FileNotFoundError("Could not parse the configuration file.")

        return config
