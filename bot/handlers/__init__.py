from .middleware import middleware_handler
from .start import start_handler
# from .help import help_handler


HANDLERS_LIST = [
    [middleware_handler],
    [start_handler]
]

