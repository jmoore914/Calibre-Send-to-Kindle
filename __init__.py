# The class that all Interface Action plugin wrappers must inherit from
from calibre.customize import InterfaceActionBase


class InterfacePlugin(InterfaceActionBase):

    name = 'Send to Kindle'
    description = 'Updates metadata then sends file to kindle'
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'jmoore914'
    version = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)

    #: This field defines the GUI plugin class that contains all the code
    #: that actually does something. Its format is module_path:class_name
    #: The specified class must be defined in the specified module.
    actual_plugin = 'calibre_plugins.send_to_kindle.ui:Main'
