from sensor import sensors_values
import sys


async def check_for_alerts():
    try:
        for x in sensors_values:
            value_sens = sensors_values[x]['value']
            minval_sens = sensors_values[x]['min_val']
            maxval_sens = sensors_values[x]['max_val']
            if value_sens >= maxval_sens:
                print("Alert occured, too high")
            elif value_sens <= minval_sens:
                print("Alert occured, too low")
    except Exception as e:
        sys.print_exception(e)
