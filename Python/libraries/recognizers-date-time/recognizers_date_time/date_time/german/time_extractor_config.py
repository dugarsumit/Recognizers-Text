from typing import List, Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.german_date_time import GermanDateTime
from ..base_time import TimeExtractorConfiguration
from ..base_timezone import BaseTimeZoneExtractor
from .timezone_extractor_config import GermanTimeZoneExtractorConfiguration


class GermanTimeExtractorConfiguration(TimeExtractorConfiguration):
    @property
    def time_zone_extractor(self):
        return self._time_zone_extractor

    @property
    def options(self):
        return self._options

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def time_regex_list(self) -> List[Pattern]:
        return self._time_regex_list

    @property
    def at_regex(self) -> Pattern:
        return self._at_regex

    @property
    def ish_regex(self) -> Pattern:
        return self._ish_regex

    @property
    def time_before_after_regex(self) -> Pattern:
        return self._time_before_after_regex

    def __init__(self):
        super().__init__()
        self._time_regex_list: List[Pattern] = GermanTimeExtractorConfiguration.get_time_regex_list(
        )
        self._at_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.AtRegex)
        self._time_before_after_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            GermanDateTime.TimeBeforeAfterRegex)
        self._time_zone_extractor = self._timezone_extractor = BaseTimeZoneExtractor(
            GermanTimeZoneExtractorConfiguration())
        # TODO When the implementation for these properties is added, change the None values to the respective Regexps
        self._ish_regex: Pattern = None

    @staticmethod
    def get_time_regex_list() -> List[Pattern]:
        return [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex1),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex2),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex3),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex4),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex5),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex6),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex7),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex8),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex9),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeRegex10),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.ConnectNumRegex)
        ]
