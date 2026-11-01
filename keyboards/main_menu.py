from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Главное меню: широкая CTA-кнопка, сетка 2x2 и нижняя строка FAQ."""
    builder = InlineKeyboardBuilder()

    # Главная кнопка во всю ширину
    builder.row(
        InlineKeyboardButton(
            text="⚖️ Задать вопрос юристу",
            callback_data="ask_lawyer",
        )
    )

    # Сетка функциональных разделов 2x2
    builder.row(
        InlineKeyboardButton(text="📚 База знаний", callback_data="knowledge_base"),
        InlineKeyboardButton(text="📄 Шаблоны документов", callback_data="templates"),
    )
    builder.row(
        InlineKeyboardButton(text="📂 Мои обращения", callback_data="my_requests"),
        InlineKeyboardButton(text="ℹ️ О проекте", callback_data="about_project"),
    )

    # Вспомогательная кнопка внизу
    builder.row(
        InlineKeyboardButton(text="🆘 Помощь (FAQ)", callback_data="help_faq")
    )

    return builder.as_markup()
