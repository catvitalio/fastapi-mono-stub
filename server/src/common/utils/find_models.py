import importlib
import os
from types import ModuleType

from ..models import Base


def find_models() -> None:
    """
    Recursive find and import all models in project
    """
    for root, _, files in os.walk('src'):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                module_path = os.path.join(root, file)
                module = _import_module(module_path)
                _import_models_from_module(module)


def _import_module(module_path: str) -> ModuleType:
    module_name = module_path.replace('/', '.').replace('\\', '.')[:-3]
    return importlib.import_module(module_name)


def _import_models_from_module(module: ModuleType) -> None:
    for name in dir(module):
        obj = getattr(module, name)
        if hasattr(obj, '__class__') and issubclass(obj.__class__, Base.__class__):
            globals()[name] = obj
