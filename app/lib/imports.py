import importlib
from pathlib import Path


def init(app):
    modules_dir = Path(__file__).parent.parent.joinpath('modules')

    for m_dir in modules_dir.iterdir():
        if m_dir.is_dir() and m_dir.name != '__pycache__':
            module_name = 'modules.' + m_dir.name
            try:
                module = importlib.import_module(module_name)
                if(module.init):
                    module.init(app)
            except:
                pass
