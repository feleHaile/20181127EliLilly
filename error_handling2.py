#!/usr/bin/env python
import logging

logging.basicConfig(filename="myspeciallog.log", level=logging.WARNING)

x = 42

sample_values = [3, 4, 0, 5, '42', 9, 15]


for v in sample_values:
    try:
        result = x / v
    except ZeroDivisionError as err:
        logging.warning(err)
    except (TypeError, ValueError) as err:
        logging.error(err)
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print("*")
