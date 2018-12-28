from datetime import datetime as dt
from datetime import timedelta as td
import numpy

class Sbe_instrument:
    """A Sea Bird instrument"""

    def __init__(self):
        pass
    
# For output format 0 converted hex data...
def dec_to_t(dec):
    return (dec / 10000.0) - 10.0
def dec_to_c(dec):
    return float((dec / 100000.0) - 0.5)
def dec_to_p(dec, pres_range):
    return (dec * pres_range / (0.85 * 65536)) - (0.05 * pres_range)


# Utility functions...
def hex_reverse_byte_order(old_hex):
    new_hex = ''
    while len(new_hex) < len(old_hex):
        new_hex = old_hex[len(new_hex):len(new_hex)+2] + new_hex
    return new_hex
def pressure_range_psia_to_db(pressure_range_psia):
    return 0.6894757 * (pressure_range_psia - 14.7)
def pressure_to_depth_seawater(pressure, latitude):
    x = (numpy.sin(latitude / 57.29578))**2
    gravity_variation = 9.780318 * (1.0 + (5.2788e-3 + 2.36e-5 * x) * x) + 1.092e-6 * pressure
    return ((((-1.82e-15 * pressure + 2.279e-10) * pressure - 2.2512e-5) * pressure + 9.72659) * pressure) / gravity_variation

# Time functions...
def T_origin(origin_date_str):
    """Accepts a date as 'YYYYMMDDhhmmss'"""
    return dt.strptime(origin_date_str, "%Y%m%d%H%M%S")
def T_delt(T_seconds):
    return td(seconds=T_seconds)
def T_delt_to_date(delt, origin):
    return dt.strftime((T_origin(origin) + T_delt(delt)), "%m/%d/%Y %H:%M:%S")
