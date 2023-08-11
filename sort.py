from generate import element
from needs import (
    ground,
    twelve_ground,
    six_gold,
    five_star,
    six_position,
    element,
    get_chinese_date,
)
import csv
from datetime import datetime
from borax.calendars.lunardate import LunarDate


class sort:
    def __init__(self) -> None:
        pass

    def __get_chinese_date(self):
        result = get_chinese_date()
        self.month = result[1]
        self.day = result[2]
        self.hours: str = result[3]

    def __verfigy_gong(self):
        self.six_grid: list[element] = []
        for i in six_position:
            self.six_grid.append(element(name=i))

    def __vertify_ground(self):
        day = self.day
        first_index = (day // 6) - 1
        first_focus = self.six_grid[index]
        first_focus.info = "日"
        first_focus.ground = twelve_ground[(day % 12) - 1]
        self.housr_index=0
        for i in 

    def __vertify_family(self):
        pass

    def __vertify_sixgold(self):
        pass

    def export_element(self):
        pass


def generate_result(result: sort):
    return result.export_element()
