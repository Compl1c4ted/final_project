import datetime as dt


class Record:
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.date = dt.date.today()
        self.comment = comment


class Calculator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records: list[Record] = []

    def add_record(self, record):
        self.records.append(record)

    def show_records(self):
        for record in self.records:
            print(record.amount, record.date)

    def get_today_stats(self):
        pass

    def get_calories_remained():
        pass

    def get_week_stats():
        pass


class MoneyCalculator(Calculator):

    USD_RATE = 93
    EURO_RATE = 103


class CalorieCalculator(Calculator):
    pass


calc = Calculator(1231)
add_record = calc.add_record(Record(123.1231, 'asjdfna'))
calc.get_today_stats()
calc.show_records()
