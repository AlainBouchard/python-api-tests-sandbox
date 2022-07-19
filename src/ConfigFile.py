import logging
import os.path
import yaml


class ConfigFile(object):
    """
    Used to parse a yaml file for the configuration.
    """
    def __init__(self, file_name="test-config.yaml"):
        """
        :param file_name: filename of the YAML configuration file.
        """
        self.__file_name = file_name
        self.__file_path = self._find_file_path(self.__file_name)
        self.__config = self.load_yaml_file(self.__file_path)

    def _find_file_path(self, file_name: str, file_path: str = "") -> str:
        """
        Returns the relative path of the configuration file.
        :param file_name: the YAML filename with no path.
        :param file_path: the relative path to search the file in.
        :return: the relative path of the specified filename.
        """
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
        """
        Loading a given YAML file.
        :param file_path: full relative path of the YAML file to source.
        :return: YAML file content in a dictionary format.
        """
        config = {}
        try:
            with open(file_path, 'r') as fs:
                try:
                    config = yaml.safe_load(fs)
                except yaml.YAMLError as e:
                    message = f"YAML format if wrong: {file_path}"
                    logging.error(f"{message} ({e})")
                    raise ConfigFileError(message)

        except FileNotFoundError as e:
            logging.error(f"File name doesn't exist: {file_path} ({e})")
            raise FileNotFoundError("Could not parse the configuration file.")

        return config


class ConfigFileError(Exception):
    """ Exception to deal with bad configuration file. """
    pass
