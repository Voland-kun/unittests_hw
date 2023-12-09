import unittest
from unittest.mock import Mock
from book import Book, BookRepository, BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book1 = Mock(spec=Book, id=1, title='Book 1')
        self.book2 = Mock(spec=Book, id=2, title='Book 2')
        self.books = [self.book1, self.book2]

    def test_find_by_id(self):
        mock_repository = Mock(spec=BookRepository)
        service = BookService(mock_repository)
        mock_repository.find_by_id.return_value = self.book1
        self.assertEqual(service.find_by_id(1), self.book1)
        mock_repository.find_by_id.assert_called_once_with(1)

    def test_find_all(self):
        mock_repository = Mock(spec=BookRepository)
        service = BookService(mock_repository)
        mock_repository.find_all.return_value = self.books
        self.assertEqual(service.find_all(), self.books)
        mock_repository.find_all.assert_called_once()


if __name__ == '__main__':
    unittest.main()
