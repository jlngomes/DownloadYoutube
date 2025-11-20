from datetime import datetime

dict_mouth = {
        1: 'Jan',
        2: 'Fev',
        3: 'Mar',
        4: 'Abr',
        5: 'Mai',
        6: 'Jun',
        7: 'Jul',
        8: 'Ago',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }

class DateHandler:
    """
    en: Class responsible for handling dates.
    br: Class responsável pela manipulação de datas.
    """

    def __init__(self):
        self._date_actual = datetime.today().date()

    @property
    def get_date_actual(self):
        """
        en: Return the date of the current date (format: YYYY-MM-DD).
        br: Retorna a data atual (formato: YYYY-MM-DD).
        """
        return self._date_actual

    @property
    def get_day(self):
        """"
        en: Return the day of the current date.
        br: Retorna a dia atual.
        """
        return self._date_actual.day

    @property
    def get_month(self):
        """"
        en: Return the mouth of the current date.
        br: Retorna a mês atual.
        """
        return dict_mouth.get(self._date_actual.month, None)

    @property
    def get_year(self):
        """"
        en: Return the year of the current date.
        br: Retorna a ano atual.
        """
        return self._date_actual.year

    def check_its_saturday(self):
        """"
        en: Return true if current date is saturday.
        br: Retorna True se a data de hoje é sábado.
        """
        if not self._date_actual:
            return False

        return True if self._date_actual.weekday() in 5 else False

    def format_br_date(self):
        """"
        en: Return the date of the current date (format: DD-MM-YYYY).
        br: Retorna a data atual (formato: DD-MM-YYYY).
        """
        return self._date_actual.strftime('%d-%m-%Y')
