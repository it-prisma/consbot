from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def user_start(message: Message) -> None:
    await message.answer("Hello, user")