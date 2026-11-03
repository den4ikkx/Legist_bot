from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.main_menu import get_main_menu_keyboard

router = Router()

# Текст приветствия главного меню
MAIN_MENU_TEXT = (
    "Я здесь, чтобы помочь разобраться в любых правовых вопросах. Напиши, что тебя интересует, или загляни в нашу базу знаний, где собраны ответы на самые частые вопросы.\n"
    "С чего начнем? 😊"
)


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Отправляет главное меню с инлайн-клавиатурой."""
    await message.answer(
        MAIN_MENU_TEXT,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "Команды:\n"
        "/start — открыть главное меню\n"
        "/help — список команд"
    )


@router.callback_query(F.data == "ask_lawyer")
async def on_ask_lawyer(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: ⚖️ Задать вопрос юристу")


@router.callback_query(F.data == "knowledge_base")
async def on_knowledge_base(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: 📚 База знаний")


@router.callback_query(F.data == "templates")
async def on_templates(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: 📄 Шаблоны документов")


@router.callback_query(F.data == "my_requests")
async def on_my_requests(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: 📂 Мои обращения")


@router.callback_query(F.data == "about_project")
async def on_about_project(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: ℹ️ О проекте")


@router.callback_query(F.data == "help_faq")
async def on_help_faq(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer("Вы выбрали: 🆘 Помощь (FAQ)")
