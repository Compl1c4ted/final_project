import datetime as dt
from datetime import timedelta


class Record:
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records: list[Record] = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_amount: int = 0
        for record in self.records:
            if record.date == dt.date.today():
                today_amount += record.amount
            else:
                print('НЕ СЧИТАЮ ВЧЕРА СЕГОДНЯШНИМ ДНЕМ')
        return today_amount

    def get_week_stats(self):
        week_amount: int = 0
        today = dt.date.today()
        seven_days_ago = today - timedelta(days=7)
        for record in self.records:
            if seven_days_ago <= record.date <= today:
                week_amount += record.amount
        return week_amount


class CashCalculator(Calculator):

    USD_RATE = float(93)
    EURO_RATE = float(103)
    RUB_RATE = 1

    def get_today_cash_remained(self, currency: str):
        rub_amount_remained = float(self.limit - self.get_today_stats())
        currencies = {
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'rub': ('руб', self.RUB_RATE)
        }
        cur_name, cur_rate = currencies[currency]
        money = round(rub_amount_remained / cur_rate, 2)
        if money == 0:
            return 'Денег нет, держись'
        elif money > 0:
            return f'На сегодня осталось {money} {cur_name}'
        elif rub_amount_remained <= 0:
            money1 = -money
            return f'Денег нет, держись: твой долг - {money1} {cur_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            return (
                f'Сегодня можно съесть что-нибудь ещё, '
                f'но с общей калорийностью не более '
                f'{self.limit - self.get_today_stats()} кКал')

        else:
            return 'Хватит есть!'


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))