__author__ = "Marc Boucsein"

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from .Data_Replace_script import napari_experimental_provide_dock_widget

def get_module_version() -> str:
    return __version__


