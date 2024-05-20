from aiogram import Dispatcher, F

from handlers import bot_messages, user_commands
from middlewares.set_logs import SetLogMiddleware

dp = Dispatcher()
# dp.message.middleware(SomeMiddleware())
# dp.callback_query.outer_middleware(SomeMiddleware())


def register_all_in_dispatcher():
    include_routers()
    include_middlewares()
    register_all_callbacks()


def include_routers():
    dp.include_routers(
        user_commands.router,
        bot_messages.router,
    )


def register_all_callbacks():
    pass
    # # Help меню админа
    # register_admin_help_menu()
    #
    # # Главное меню
    # dp.callback_query.register(main_menu_callback.menu_main_handler,
    #                            F.data == 'menu_main')
    #
    # # Столовые
    # dp.callback_query.register(canteens_callback.menu_canteens_handler, F.data == "menu_canteens")
    # dp.callback_query.register(canteens_callback.canteens_handler, F.data.startswith('canteen'))
    #
    # # Ссылки
    # dp.callback_query.register(links_callback.menu_links_handler, F.data == 'menu_links')
    # dp.callback_query.register(links_callback.show_others_links_handler, F.data == 'open_others_links')
    # dp.callback_query.register(links_callback.show_main_links_handler, F.data == 'show_main_links')
    #
    # # Термины
    # dp.callback_query.register(stadburo_menu_callback.menu_stadburo_handler, F.data == 'menu_stadburo')
    #
    # #       Эмиграционное меню
    # dp.callback_query.register(stadburo_immigration_callback.menu_immigration_handler, F.data == 'menu_immigration')
    # dp.callback_query.register(stadburo_immigration_callback.aufenthaltstitel_handler, F.data == 'aufenthaltstitel')
    # dp.callback_query.register(stadburo_immigration_callback.adressanderung_handler, F.data == 'adressanderung')
    # dp.callback_query.register(stadburo_immigration_callback.eat_abholung_handler, F.data == 'eat_abholung')
    #
    # dp.callback_query.register(stadburo_menu_callback.registration_handler, F.data == 'registration')
    # dp.callback_query.register(stadburo_menu_callback.stadtburo_others_handler, F.data == 'stadtburo_others')
    #
    # # Настройки
    # dp.callback_query.register(settings_callback.menu_settings_handler, F.data == "menu_settings")
    # dp.callback_query.register(settings_callback.change_mailing_time_handler, F.data == "change_mailing_time")
    # dp.callback_query.register(settings_callback.change_status_mailing_handler, F.data == 'change_status_mailing')
    # dp.callback_query.register(settings_callback.change_status_numbers_in_menu_handler,
    #                            F.data == 'change_status_numbers_in_menu')
    # dp.callback_query.register(settings_callback.change_language_handler, F.data.startswith('settings_language'))
    #
    # # Донаты
    # dp.callback_query.register(main_menu_callback.menu_donations_handler, F.data == "menu_donations")
    #
    # # Дополнительное меню
    # dp.callback_query.register(additionally_menu_callback.menu_additionally_handler, F.data == 'menu_additionally')
    # dp.callback_query.register(additionally_menu_callback.menu_manuals_handler, F.data == 'manuals')
    #
    # #       Обратная связь
    # dp.callback_query.register(feedback_callback.menu_feedback_handler, F.data == 'menu_feedback')
    # dp.callback_query.register(feedback_callback.show_contacts_handler, F.data == 'contacts')
    # dp.callback_query.register(feedback_callback.send_response_handler, F.data == 'response')
    #
    # # Feedback
    # dp.callback_query.register(feedback_callback.send_feedback_form_check, F.data.startswith('feedback'))
    #
    # # Админ
    # # dp.callback_query.register(admin_callback.show_person_mailing_time_handler,
    # #                            F.data == 'show_person_mailing_time')
    # # dp.callback_query.register(admin_callback.change_person_mailing_time_handler,
    # #                            F.data == 'change_person_mailing_time')
    # # dp.callback_query.register(admin_callback.change_person_numbers_in_menu_handler,
    # #                            F.data == 'change_person_numbers_in_menu')
    #
    # # Выводить меню после рассылки
    # dp.callback_query.register(user_commands.send_main_menu_from_mailing_handler, F.data == 'send_menu_main')


def include_middlewares():
    """
    text

    :param type val:


    :return:
    :rtype:
    """
    dp.message.middleware(SetLogMiddleware())
    dp.callback_query.middleware(SetLogMiddleware())

