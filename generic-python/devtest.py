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
        # Each row in the data string is separated by `+----+---\n`
        row_sep_pattern = r'\+-*\+-*\+\n?'
        # The data with in the row pattern
        # eg: | Simple design  | Over-engineering  |
        row_data_pattern = r'[|][\s]?([A-Za-z0-9-_,".\?\'\s]+)'
        rows = re.split(row_sep_pattern, data)
        match_count = 0
        parsed_output = []
        for row in rows:
            match = re.findall(row_data_pattern, row)
            if match:
                # Ignore the header and the blank lines
                # before and after the table.
                if match_count > 0:
                    left_str, right_str = '', ''
                    line_count = 0
                    # row can have multiple lines
                    for line in match:
                        if line != '\n':
                            if (line_count % 2) == 0:
                                if not left_str:
                                    left_str += line.strip()
                                else:
                                    left_str += ' ' + line.strip()
                            else:
                                if not right_str:
                                    right_str += line.strip()
                                else:
                                    right_str += ' ' + line.strip()
                            line_count += 1
                    parsed_output.append((left_str.strip(), right_str.strip()))
                match_count += 1
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
        sanitized_word = ''.join([i.lower() for i in word if i not in self.exclude_characters])
        return sanitized_word == sanitized_word[::-1]
