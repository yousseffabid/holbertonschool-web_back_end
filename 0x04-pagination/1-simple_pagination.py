#!/usr/bin/env python3
""" 1. Simple pagination """
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
        assert type(page) == int and type(page_size) == int
        mydataset = self.dataset()
        indexes = index_range(page, page_size)
        dataset_length = len(mydataset)
        if indexes[1] >= dataset_length:
            return []
        if indexes[0] < dataset_length and indexes[1] <= dataset_length:
            return mydataset[indexes[0]:indexes[1]]

        return []
