#!/usr/bin/env python
import logging

logging.basicConfig(filename="myspeciallog.log", level=logging.WARNING)


def get_results(dividend, values):
    result_list = []

    for v in values:
        try:
            result = dividend / v
            result_list.append(result)
        except ZeroDivisionError as err:
            logging.warning(err)
        except (TypeError, ValueError) as err:
            logging.error(err)
        except Exception as err:
            print(err)

    return result_list

x = 42

sample_values = [3, 4, 0, 5, '42', 9, 15]

results = get_results(x, sample_values)

print(results)
