from typing import List, Dict, Callable
from datetime import datetime

from recognizers_text.utilities import RegExpUtility
from ..utilities import DateUtils
from ..base_holiday import BaseHolidayParserConfiguration
from ...resources.german_date_time import GermanDateTime


class GermanHolidayParserConfiguration(BaseHolidayParserConfiguration):
    @property
    def holiday_names(self) -> Dict[str, List[str]]:
        return self._holiday_names

    @property
    def holiday_regex_list(self) -> List[str]:
        return self._holiday_regexes

    @property
    def holiday_func_dictionary(self) -> Dict[str, Callable[[int], datetime]]:
        return self._holiday_func_dictionary

    def __init__(self, config):
        super().__init__()
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.HolidayRegex1),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.HolidayRegex2),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.HolidayRegex3)
        ]
        self._holiday_names = GermanDateTime.HolidayNames

        self.next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.NextPrefixRegex)
        self.previous_prefix_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.PreviousPrefixRegex)
        self.this_prefix_regex = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.ThisPrefixRegex)

    def _init_holiday_funcs(self) -> Dict[str, Callable[[int], datetime]]:
        local = dict([
            ('padres', GermanHolidayParserConfiguration.fathers_day),
            ('madres', GermanHolidayParserConfiguration.mothers_day),
            ('acciondegracias', GermanHolidayParserConfiguration.thanksgiving_day),
            ('trabajador', GermanHolidayParserConfiguration.labour_day),
            ('delaraza', GermanHolidayParserConfiguration.columbus_day),
            ('memoria', GermanHolidayParserConfiguration.memorial_day),
            ('pascuas', GermanHolidayParserConfiguration.easter_day),
            ('navidad', GermanHolidayParserConfiguration.christmas_day),
            ('nochebuena', GermanHolidayParserConfiguration.christmas_eve),
            ('añonuevo', GermanHolidayParserConfiguration.new_year),
            ('nochevieja', GermanHolidayParserConfiguration.new_year_eve),
            ('yuandan', GermanHolidayParserConfiguration.new_year),
            ('maestro', GermanHolidayParserConfiguration.teacher_day),
            ('todoslossantos', GermanHolidayParserConfiguration.halloween_day),
            ('niño', GermanHolidayParserConfiguration.children_day),
            ('mujer', GermanHolidayParserConfiguration.female_day)
        ])

        return {**super()._init_holiday_funcs(), **local}

    @staticmethod
    def new_year(year: int) -> datetime:
        return datetime(year, 1, 1)

    @staticmethod
    def new_year_eve(year: int) -> datetime:
        return datetime(year, 12, 31)

    @staticmethod
    def christmas_day(year: int) -> datetime:
        return datetime(year, 12, 25)

    @staticmethod
    def christmas_eve(year: int) -> datetime:
        return datetime(year, 12, 24)

    @staticmethod
    def female_day(year: int) -> datetime:
        return datetime(year, 3, 8)

    @staticmethod
    def children_day(year: int) -> datetime:
        return datetime(year, 6, 1)

    @staticmethod
    def halloween_day(year: int) -> datetime:
        return datetime(year, 10, 31)

    @staticmethod
    def teacher_day(year: int) -> datetime:
        return datetime(year, 9, 11)

    @staticmethod
    def easter_day(year: int) -> datetime:
        return DateUtils.min_value

    def get_swift_year(self, text: str) -> int:
        trimmed_text = text.strip().lower()
        swift = -10

        if self.next_prefix_regex.search(trimmed_text):
            swift = 1

        if self.previous_prefix_regex.search(trimmed_text):
            swift = -1

        if self.this_prefix_regex.search(trimmed_text):
            swift = 0

        return swift

    def sanitize_holiday_token(self, holiday: str) -> str:
        return holiday.replace(' ', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
