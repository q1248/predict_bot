from datetime import datetime
from borax.calendars.lunardate import LunarDate


class ground:
    def __init__(self, name, attribute, color) -> None:
        self.name: str = name
        self.attribute: str = attribute
        self.color: str = color


class element:
    def __init__(self, fivestar, sixgold, ground, family, info, name) -> None:
        self.fivestar = fivestar
        self.sixgold = sixgold
        self.ground = ground
        self.family = family
        self.info = info
        self.name = name


twelve_ground = [
    ground("子", "木", "green"),
    ground("丑", "土", "yellow"),
    ground("寅", "木", "green"),
    ground("卯", "木", "green"),
    ground("辰", "土", "yellow"),
    ground("巳", "火", "red"),
    ground("午", "火", "red"),
    ground("未", "土", "yellow"),
    ground("申", "金", "white"),
    ground("酉", "金", "white"),
    ground("戌", "土", "yellow"),
    ground("亥", "水", "blue"),
]

six_position = ["大安", "留连", "速喜", "赤口", "小吉", "空亡"]

six_gold = ["青龙", "朱雀", "勾陈", "螣蛇", "白虎", "玄武"]
five_star = ["金星", "木星", "水星", "火星", "土星", "天空"]

shichen = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def get_chinese_date():
    rightnow = datetime.now()
    lunar_now = LunarDate.from_solar_date(rightnow.year, rightnow.month, rightnow.day)
    lunar_date = [lunar_now.year, lunar_now.month, lunar_now.day]
    # 将小时转换成时辰
    if rightnow.hour == 23:
        lunar_date.append("子")
    else:
        lunar_date.append(shichen[rightnow.hour // 2])
    return lunar_date
