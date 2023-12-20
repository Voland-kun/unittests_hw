"""docstring просто зачем"""
import pytest
from main import ListComparer


class TestListComparer:
    """Тесты ListComparer"""
    def test_init_valid_lists(self):
        """init valid"""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        comparer = ListComparer(list1, list2)
        assert comparer.list1 == list1
        assert comparer.list2 == list2

    def test_init_empty_list_1(self):
        """init empty list1"""
        list1 = []
        list2 = [4, 5, 6]
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_init_empty_list_2(self):
        """init empty list2"""
        list1 = [1, 2, 3]
        list2 = []
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_init_non_int_list_1(self):
        """init list1 non num"""
        list1 = [1, "a", 3]
        list2 = [4, 5, 6]
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_init_non_int_list_2(self):
        """init list2 non num"""
        list1 = [1, 2, 3]
        list2 = [4, "a", 6]
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_init_not_list_1(self):
        """init list1 errortype"""
        list1 = 1
        list2 = [4, 5, 6]
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_init_not_list_2(self):
        """init list2 errortype"""
        list1 = [1, 2, 3]
        list2 = 4
        with pytest.raises(TypeError):
            ListComparer(list1, list2)

    def test_avg(self):
        """test avg"""
        list1 = [1, 2, 3]
        assert ListComparer.calculate_average(list1) == 2


    def test_avg_comparison_lesser(self):
        """list1<list2"""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        comparer = ListComparer(list1, list2)
        assert comparer.calculate_average(list1) < comparer.calculate_average(list2)
        assert comparer.compare_lists() == "Второй список имеет большее среднее значение"

    def test_avg_comparison_greater(self):
        """list1>list2"""
        list1 = [4, 5, 6]
        list2 = [1, 2, 3]
        comparer = ListComparer(list1, list2)
        assert comparer.calculate_average(list1) > comparer.calculate_average(list2)
        assert comparer.compare_lists() == "Первый список имеет большее среднее значение"

    def test_avg_comparison_equal(self):
        """list1==list2"""
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        comparer = ListComparer(list1, list2)
        assert comparer.calculate_average(list1) == comparer.calculate_average(list2)
        assert comparer.compare_lists() == "Средние значения равны"
