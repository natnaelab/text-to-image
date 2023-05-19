from .middleware import middleware_handler
from .start import start_handler
from .help import help_handler


HANDLERS_LIST = [
    [middleware_handler],
    [start_handler, help_handler]
]


#   DATABASE_URL=postgres://text_to_image:FabYuX9ylioDudN@text-to-image-db.flycast:5432/text_to_image?sslmode=disable
