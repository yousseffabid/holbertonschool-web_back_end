#!/usr/bin/env python3
""" Deletion-resilient hypermedia pagination """
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return start index and end index"""
    end_index = page * page_size
    return (end_index-page_size, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page"""
        assert type(page) == int or type(page_size) == int
        assert page > 0 or page_size > 0
        mydataset = self.dataset()
        indexes = index_range(page, page_size)
        dataset_length = len(mydataset)

        if indexes[0] < dataset_length and indexes[1] <= dataset_length:
            return mydataset[indexes[0]:indexes[1]]

        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ 2. Hypermedia pagination """
        mydataset = self.dataset()
        data = self.get_page(page, page_size)
        page_size = len(data)
        total_pages = len(mydataset)
        result = self.get_page(page + 1, page_size)
        if result == []:
            next_page = None
        else:
            next_page = page + 1

        result = self.get_page(page - 1, page_size)
        if result == []:
            previous_page = None
        else:
            previous_page = page - 1

        return {"page_size": page_size,
                "page": page, "data": data,
                "next_page": next_page,
                "previous_page": previous_page,
                "total_pages": total_pages}

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get hyper functions"""
        assert type(index) == int and type(page_size) == int
        assert len(self.indexed_dataset()) > index >= 0
        pages = []
        next_index = index + page_size
        for i in range(index, index + page_size):
            if not self.indexed_dataset().get(i):
                i += 1
                next_index += 1
            pages.append(self.indexed_dataset()[i])
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': pages
        }
