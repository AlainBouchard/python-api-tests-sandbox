import pytest
from src.ConfigFile import ConfigFile


class TestConfigFile(object):
    """
    Testing the ConfigFile() class that load the YAML configuration for tests.
    """
    def test_load_yaml_config_file_with_default_file_name_expect_success(self):
        # As a developer, I want my tests to load the default test suite configuration file

        config = ConfigFile()

        assert len(config.config) > 0

    def test_load_yaml_config_file_with_good_name_expect_success(self):
        # As a developer, I want my tests to load the given test suite configuration file
        config = ConfigFile(file_name="test-config.yaml")

        assert len(config.config) > 0

    def test_load_yaml_config_file_with_bad_name_expect_fail(self):
        # As a developer, I want my tests to raise an exception if test suite configuration file isn't found
        with pytest.raises(Exception) as e:
            ConfigFile("bad-filename.yaml")

        assert str(e.value) == "Could not parse the configuration file."
