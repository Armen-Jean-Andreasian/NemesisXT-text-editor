import os


class FilePaths:
    """
    Consists of getters of project files
    """
    __SETTINGS_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "settings.json"))

    __THEMES_FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "themes.json"))
    __LOGO_FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "window_logo.ico"))

    @property
    def settings_filepath(self):
        return self.__SETTINGS_FILE_PATH

    @property
    def themes_filepath(self):
        return self.__THEMES_FILEPATH

    @property
    def logo_filepath(self):
        return self.__LOGO_FILEPATH
