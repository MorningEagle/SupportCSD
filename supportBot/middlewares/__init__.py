from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .support_middlewares import SupportMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(SupportMiddleware())
