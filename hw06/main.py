"""docstring просто зачем"""
class ListComparer:
    """Класс для сравнения средних арифметических списков"""

    def __init__(self, list1, list2):
        """Инициализация"""
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Аргументы должны быть списками")

        if len(list1) == 0 or not all(isinstance(num, (int, float)) for num in list1) \
                or len(list2) == 0 or not all(isinstance(num, (int, float)) for num in list2):
            raise TypeError("Списки должны содержать только числа")
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def calculate_average(lst):
        """Среднее арифметическое списка"""
        return sum(lst) / len(lst)

    def compare_lists(self):
        """Сравнение средних арифметических"""
        avg_list1 = self.calculate_average(self.list1)
        avg_list2 = self.calculate_average(self.list2)
        if avg_list1 > avg_list2:
            result = "Первый список имеет большее среднее значение"
        elif avg_list1 < avg_list2:
            result = "Второй список имеет большее среднее значение"
        else:
            result = "Средние значения равны"
        print(result)
        return result
