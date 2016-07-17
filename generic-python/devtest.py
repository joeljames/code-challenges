import operator
import six
import collections
from datetime import timedelta, time, datetime
import calendar
import string
import re


__all__ = [
    'Solutions',
    'IsPalindrome',
]


class Solutions:

    def greater_than_avg(self, data_list):
        """
        Given a data_list returns a list of values whose
        value is greater than the avg.

        :param data_list: A list of integers
        """
        self._assert_list(data_list)
        avg = sum(data_list)/len(data_list)
        return [value for value in data_list if value > avg]

    def sort_fruit(self, data_list):
        """
        Given a data_list sorts the list by the count attribute on the object

        :param data_list: A list of objects where each object has
            a count attribute
        """
        self._assert_list(data_list)
        return sorted(data_list, key=operator.itemgetter('count'))

    def transpose_dict(self, data_dict):
        """
        Given a data_dict returns the transpose of the dict

        :param data_dict: A dictionary object
        """
        self._assert_dict(data_dict)
        return {value: key for key, value in six.iteritems(data_dict)}

    def week_start_end(self, dt):
        """
        Given a datetime object returns start and the end datetime of the week

        :param dt: A datetime object
        """
        self._assert_datetime(dt)
        max_time = time.max
        min_time = time.min
        start = (dt - timedelta(days=dt.weekday()))\
            .replace(
                hour=min_time.hour,
                minute=min_time.minute,
                second=min_time.second,
                microsecond=min_time.microsecond
            )
        end = (start + timedelta(days=6))\
            .replace(
                hour=max_time.hour,
                minute=max_time.minute,
                second=max_time.second,
                microsecond=max_time.microsecond
            )
        return start, end

    def month_last_day(self, dt):
        """
        Given a datetime object returns the last day of the month

        :param dt: A datetime object
        """
        self._assert_datetime(dt)
        return calendar.monthrange(dt.year, dt.month)[1]

    def palindrome_test_function(self):
        """
        Return a function object that will accept 1
        argument and can be called to check for palindromes
        """
        return IsPalindrome()

    def string_parse(self, data):
        # Each row in the data string is separated by `+-------`
        row_sep_pattern = r'\+-+'
        # The data with in the row pattern
        # eg: | Simple design  | Over-engineering  |
        row_data_pattern = r'[|][\s]?([A-Za-z0-9-_,".\?\'\s]+)'
        # Split the data string and capture each row
        rows = [value for value in re.split(row_sep_pattern, data) if value.startswith('+\n|')]
        # The first row is the header,
        # slice the rows to remove header
        rows = rows[1:]
        parsed_output = []
        for row in rows:
            # A row could have multiple lines,
            # so split the row by new line char
            row_output = []
            for line in row.split('\n'):
                match = re.findall(row_data_pattern, line)
                if match:
                    if not row_output:
                        row_output = [value.strip() for value in match]
                    else:
                        for index, value in enumerate(match):
                            value = value.strip()
                            if value:
                                row_output[index] += unicode(' ' + value)
            parsed_output.append(tuple(row_output))
        return parsed_output

    def _assert_list(self, data_list):
        if not isinstance(data_list, (list, tuple)):
            msg = 'The argument should be a `list` or `tuple`.'
            raise ValueError(msg)

    def _assert_dict(self, data_dict):
        if not isinstance(data_dict, collections.Mapping):
            msg = 'The argument should be a `dict` type.'
            raise ValueError(msg)

    def _assert_datetime(self, dt):
        if not isinstance(dt, datetime):
            msg = 'The argument should be a `datetime` object.'
            raise ValueError(msg)


class IsPalindrome:
    exclude_characters = string.punctuation + ' '

    def __call__(self, word):
        word = word.lower()
        if len(word) <= 1:
            return True
        elif word[0] != word[-1]:
            return False
        else:
            return self.__call__(word[1:-1].strip(self.exclude_characters))
