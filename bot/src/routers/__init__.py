"""This package is used for a bot logic implementation."""
from .close import close_driver_router
from .help import help_router
from .parse import parse_router
from .send_captcha import captcha_router
from .start import start_router

routers = (
    start_router, 
    help_router, 
    parse_router, 
    captcha_router, 
    close_driver_router
)
