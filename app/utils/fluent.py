from fluent.runtime import FluentLocalization, FluentResourceLoader

loader = FluentResourceLoader("locales/{locale}")

l10n_en = FluentLocalization(["en"], ["base_en.ftl"], loader)
l10n_ru = FluentLocalization(["ru"], ["base_ru.ftl"], loader)
l10n_de = FluentLocalization(["de"], ["base_de.ftl"], loader)
list_of_available_languages = ['en', 'ru', 'de']

list_of_l10n = {
    'ru': l10n_ru,
    'en': l10n_en,
    'de': l10n_de
}

"""

auxiliary.get_l10n(language).format_value('')
reply_markup=inline

, language: str

inline.get_main_menu(l10n)

l10n = auxiliary.get_l10n(language)

l10n.format_value('')

l10n.format_value('to-menu-main')
"""