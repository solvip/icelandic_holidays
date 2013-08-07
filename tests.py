#!/usr/bin/env python

import unittest

from datetime import datetime, timedelta
from icelandic_holidays import * 

class HolidayTests(unittest.TestCase):
    def setUp(self):
        # Holidays stolen from http://www.almanak.hi.is/
        self.holidays = [
            datetime(2013, 1, 1),
            datetime(2013, 3, 28),
            datetime(2013, 3, 29),
            datetime(2013, 3, 31),
            datetime(2013, 4, 1),
            datetime(2013, 4, 25),
            datetime(2013, 5, 1),
            datetime(2013, 5, 9),
            datetime(2013, 5, 20),
            datetime(2013, 6, 17),
            datetime(2013, 8, 5),
            datetime(2013, 12, 25),
            datetime(2013, 12, 26) ]

        self.businessdays = [
            datetime(2013, 1, 8),
            datetime(2013, 2, 14),
            datetime(2013, 2, 28),
            datetime(2013, 4, 18) ]

        self.weekend_days = [
            datetime(2013, 1, 2),
            datetime(2013, 2, 7),
            datetime(2013, 2, 14),
            datetime(2013, 2, 21) ]

        self.easter_sundays = [
            datetime(1736, 4, 1),
            datetime(1709, 3, 31),
            datetime(1734, 4, 25),
            datetime(1784, 4, 11),
            datetime(1710, 4, 20),
            datetime(2008, 3, 23),
            datetime(2215, 4, 16),
            datetime(2240, 4, 12),
            datetime(2292, 4, 10) ]

    def test_holidays(self):
        for day in self.holidays:
            self.assertTrue(is_holiday(day), msg="%s wasn't holiday" % day)

        for day in self.businessdays:
            self.assertFalse(is_holiday(day),
                             msg="%s was a holiday, shouldn't have been" % day)

    def test_businessdays(self):
        for day in self.businessdays:
            self.assertTrue(is_businessday(day), msg="%s wasn't a business day" % day)

        for day in self.holidays:
            self.assertFalse(is_businessday(day),
                             msg="%s was a business day, shouldn't have been" % day)

    def test_easter_sunday(self):
        for sunday in self.easter_sundays:
            self.assertTrue(easter_sunday(sunday),
                            msg="%s wasn't an easter sunday" % sunday)
        # Ensure that there's only a single easter sunday pr. year
        for year in range(1800, 2200):
            start_of_year = datetime(year, 1, 1)
            num_easter = 0
            for i in range(1, 365):
                if easter_sunday(start_of_year + timedelta(days=i)):
                    num_easter += 1

            self.assertEqual(num_easter, 1)


if __name__ == "__main__":
    unittest.main()
