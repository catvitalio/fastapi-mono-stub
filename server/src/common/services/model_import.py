import importlib
import os
from types import ModuleType

from sqlalchemy.ext.declarative import declarative_base


class ModelImportService:
    @classmethod
    def import_models(cls, directory: str) -> None:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    module_path = os.path.join(root, file)
                    module = cls._import_module(module_path)
                    cls._import_models_from_module(module)

    @staticmethod
    def _import_module(module_path: str) -> ModuleType:
        module_name = module_path.replace('/', '.').replace('\\', '.')[:-3]
        return importlib.import_module(module_name)

    @staticmethod
    def _import_models_from_module(module: ModuleType) -> None:
        Base = declarative_base()
        for name in dir(module):
            obj = getattr(module, name)
            if hasattr(obj, '__class__') and issubclass(obj.__class__, Base.__class__):
                globals()[name] = obj
