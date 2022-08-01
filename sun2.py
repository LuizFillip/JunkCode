import datetime
import numpy as np

# Using 32 arc minutes as sun's apparent diameter
SUN_APPARENT_RADIUS = 32.0 / (60.0 * 2.0)



def julianday(date: datetime.date) -> float:
    """Calculate the Julian Day for the specified date"""
    y = date.year
    m = date.month
    d = date.day

    if m <= 2:
        y -= 1
        m += 12

    a = np.floor(y / 100)
    b = 2 - a + np.floor(a / 4)
    jd = np.floor(365.25 * (y + 4716)) + np.floor(30.6001 * (m + 1)) + d + b - 1524.5

    return jd

def jday_to_jcentury(julianday: float) -> float:
    """Convert a Julian Day number to a Julian Century"""
    return (julianday - 2451545.0) / 36525.0

def geom_mean_long_sun(juliancentury: float) -> float:
    """Calculate the geometric mean longitude of the sun"""
    l0 = 280.46646 + juliancentury * (36000.76983 + 0.0003032 * juliancentury)
    return l0 % 360.0


def geom_mean_anomaly_sun(juliancentury: float) -> float:
    """Calculate the geometric mean anomaly of the sun"""
    return 357.52911 + juliancentury * (35999.05029 - 0.0001537 * juliancentury)

def eccentric_location_earth_orbit(juliancentury: float) -> float:
    """Calculate the eccentricity of Earth's orbit"""
    return 0.016708634 - juliancentury * (0.000042037 + 0.0000001267 * juliancentury)


def sun_eq_of_center(juliancentury: float) -> float:
    """Calculate the equation of the center of the sun"""
    m = geom_mean_anomaly_sun(juliancentury)

    mrad = np.radians(m)
    sinm = np.sin(mrad)
    sin2m = np.sin(mrad + mrad)
    sin3m = np.sin(mrad + mrad + mrad)

    c = (
        sinm * (1.914602 - juliancentury * (0.004817 + 0.000014 * juliancentury))
        + sin2m * (0.019993 - 0.000101 * juliancentury)
        + sin3m * 0.000289
    )

    return c

def sun_true_long(juliancentury: float) -> float:
    """Calculate the sun's true longitude"""
    l0 = geom_mean_long_sun(juliancentury)
    c = sun_eq_of_center(juliancentury)

    return l0 + c


def sun_true_anomaly(juliancentury: float) -> float:
    """Calculate the sun's true anomaly"""
    m = geom_mean_anomaly_sun(juliancentury)
    c = sun_eq_of_center(juliancentury)

    return m + c


def sun_rad_vector(juliancentury: float) -> float:
    v = sun_true_anomaly(juliancentury)
    e = eccentric_location_earth_orbit(juliancentury)

    return (1.000001018 * (1 - e * e)) / (1 + e * np.cos(np.radians(v)))

def sun_apparent_long(juliancentury: float) -> float:
    true_long = sun_true_long(juliancentury)

    omega = 125.04 - 1934.136 * juliancentury
    return true_long - 0.00569 - 0.00478 * np.sin(np.radians(omega))


def mean_obliquity_of_ecliptic(juliancentury: float) -> float:
    seconds = 21.448 - juliancentury * (
        46.815 + juliancentury * (0.00059 - juliancentury * (0.001813))
    )
    return 23.0 + (26.0 + (seconds / 60.0)) / 60.0


def obliquity_correction(juliancentury: float) -> float:
    e0 = mean_obliquity_of_ecliptic(juliancentury)

    omega = 125.04 - 1934.136 * juliancentury
    return e0 + 0.00256 * np.cos(np.radians(omega))


def sun_rt_ascension(juliancentury: float) -> float:
    """Calculate the sun's right ascension"""
    oc = obliquity_correction(juliancentury)
    al = sun_apparent_long(juliancentury)

    tananum = np.cos(np.radians(oc)) * np.sin(np.radians(al))
    tanadenom = np.cos(np.radians(al))

    return np.degrees(np.arctan2(tananum, tanadenom))


def sun_declination(juliancentury: float) -> float:
    """Calculate the sun's declination"""
    e = obliquity_correction(juliancentury)
    lambd = sun_apparent_long(juliancentury)

    sint = np.sin(np.radians(e)) * np.sin(np.radians(lambd))
    return np.degrees(np.arcsin(sint))


def var_y(juliancentury: float) -> float:
    epsilon = obliquity_correction(juliancentury)
    y = np.tan(np.radians(epsilon) / 2.0)
    return y * y


def eq_of_time(juliancentury: float) -> float:
    l0 = geom_mean_long_sun(juliancentury)
    e = eccentric_location_earth_orbit(juliancentury)
    m = geom_mean_anomaly_sun(juliancentury)

    y = var_y(juliancentury)

    sin2l0 = np.sin(2.0 * np.radians(l0))
    sinm = np.sin(np.radians(m))
    cos2l0 = np.cos(2.0 * np.radians(l0))
    sin4l0 = np.sin(4.0 * np.radians(l0))
    sin2m = np.sin(2.0 * np.radians(m))

    Etime = (
        y * sin2l0
        - 2.0 * e * sinm
        + 4.0 * e * y * sinm * cos2l0
        - 0.5 * y * y * sin4l0
        - 1.25 * e * e * sin2m
    )

    return np.degrees(Etime) * 4.0

def hour_angle(
    latitude: float, declination: float, zenith: float) -> float:
    """Calculate the hour angle of the sun
    See https://en.wikipedia.org/wiki/Hour_angle#Solar_hour_angle
    Args:
        latitude: The latitude of the obersver
        declination: The declination of the sun
        zenith: The zenith angle of the sun
        direction: The direction of traversal of the sun
    Raises:
        ValueError
    """

    latitude_rad = np.radians(latitude)
    declination_rad = np.radians(declination)
    zenith_rad = np.radians(zenith)

    # n = cos(zenith_rad)
    # d = cos(latitude_rad) * cos(declination_rad)
    # t = tan(latitude_rad) * tan(declination_rad)
    # h = (n / d) - t

    h = (np.cos(zenith_rad) - np.sin(latitude_rad) * np.sin(declination_rad)) / (
        np.cos(latitude_rad) * np.cos(declination_rad)
    )

    HA = np.degrees(np.arccos(h))
    #if direction == -1:
      #  HA = -HA
    return HA

import pytz

def noon(
    longitude: float,
    date: datetime.date = None,
    tzinfo: datetime.tzinfo = pytz.utc,
    ) -> datetime.datetime:
    """Calculate solar noon time when the sun is at its highest point.
    Args:
        observer: An observer viewing the sun at a specific, latitude, longitude and elevation
        date:     Date to calculate for. Default is today for the specified tzinfo.
        tzinfo:   Timezone to return times in. Default is UTC.
    Returns:
        Date and time at which noon occurs.
    """
    if isinstance(tzinfo, str):
        tzinfo = pytz.timezone(tzinfo)

    if date is None:
        date = datetime.today(tzinfo)

    jc = jday_to_jcentury(julianday(date))
    eqtime = eq_of_time(jc)
    timeUTC = (720.0 - (4 * longitude) - eqtime) / 60.0

    hour = int(timeUTC)
    minute = int((timeUTC - hour) * 60)
    second = int((((timeUTC - hour) * 60) - minute) * 60)

    if second > 59:
        second -= 60
        minute += 1
    elif second < 0:
        second += 60
        minute -= 1

    if minute > 59:
        minute -= 60
        hour += 1
    elif minute < 0:
        minute += 60
        hour -= 1

    if hour > 23:
        hour -= 24
        date += datetime.timedelta(days=1)
    elif hour < 0:
        hour += 24
        date -= datetime.timedelta(days=1)

    noon = datetime.datetime(date.year, date.month, date.day, hour, minute, second)
    return pytz.utc.localize(noon).astimezone(tzinfo) 

class Depression(Enum):
    """The depression angle in degrees for the dawn/dusk calculations"""

    CIVIL: float = 6.0
    NAUTICAL: float = 12.0
    ASTRONOMICAL: float = 18.0
    
    
date = datetime.date(1979, 9, 7)
latitude = 52 #-3.9
longitude = 0 #-38.58
dg2rad = np.pi / 180.
rad2dg = 1. / dg2rad
time_zone = 0 #-3
zenith = 90.83

print(date.strftime('We are the %d, %b %Y'))

jday = julianday(date)
jcentury = (jday_to_jcentury(jday))
long_sun = (geom_mean_long_sun(jcentury))
anomaly_sun = (geom_mean_anomaly_sun(jcentury))
eccentric = eccentric_location_earth_orbit(jcentury)
suncenter = sun_eq_of_center(jcentury)
sunlong = sun_true_long(jcentury)
sunanomaly = sun_true_anomaly(jcentury)
sunapparent = sun_apparent_long(jcentury)
meanobliquity = mean_obliquity_of_ecliptic(jcentury)
corrected = obliquity_correction(jcentury)
sunascention = sun_rt_ascension(jcentury)
declination = sun_declination(jcentury)
vary = var_y(jcentury)
eqtime = eq_of_time(jcentury)


ha = hour_angle(latitude, declination, zenith)

snoon = noon(longitude, date)

print(snoon)
#print(sunrise_time, sunset_time)

#print(float_to_datetime(date, noon), float_to_datetime(date, sunset_time))

import math
import datetime as dt

def jd_to_date(jd):
    
    
    """
    Convert Julian Day to date.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    jd : float
        Julian Day
        
    Returns
    -------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
        
    Examples
    --------
    Convert Julian Day 2446113.75 to year, month, and day.
    
    >>> jd_to_date(2446113.75)
    (1985, 2, 17.25)
    
    """
    jd = jd + 0.5
    
    F, I = math.modf(jd)
    I = int(I)
    
    A = math.trunc((I - 1867216.25)/36524.25)
    
    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I
        
    C = B + 1524
    
    D = math.trunc((C - 122.1) / 365.25)
    
    E = math.trunc(365.25 * D)
    
    G = math.trunc((C - E) / 30.6001)
    
    day = C - E + F - math.trunc(30.6001 * G)
    
    if G < 13.5:
        month = G - 1
    else:
        month = G - 13
        
    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715
        
    return year, month, day

def days_to_hmsm(days):
    """
    Convert fractional days to hours, minutes, seconds, and microseconds.
    Precision beyond microseconds is rounded to the nearest microsecond.
    
    Parameters
    ----------
    days : float
        A fractional number of days. Must be less than 1.
        
    Returns
    -------
    hour : int
        Hour number.
    
    min : int
        Minute number.
    
    sec : int
        Second number.
    
    micro : int
        Microsecond number.
        
    Raises
    ------
    ValueError
        If `days` is >= 1.
        
    Examples
    --------
    >>> days_to_hmsm(0.1)
    (2, 24, 0, 0)
    
    """
    hours = days * 24.
    hours, hour = math.modf(hours)
    
    mins = hours * 60.
    mins, min = math.modf(mins)
    
    secs = mins * 60.
    secs, sec = math.modf(secs)
    
    micro = round(secs * 1.e6)
    
    return int(hour), int(min), int(sec), int(micro)

def jd_to_datetime(jd):
    """
    Convert a Julian Day to an `jdutil.datetime` object.
    
    Parameters
    ----------
    jd : float
        Julian day.
        
    Returns
    -------
    dt : `jdutil.datetime` object
        `jdutil.datetime` equivalent of Julian day.
    
    Examples
    --------
    >>> jd_to_datetime(2446113.75)
    datetime(1985, 2, 17, 6, 0)
    
    """
    year, month, day = jd_to_date(jd)
    
    frac_days,day = math.modf(day)
    day = int(day)
    
    hour,min,sec,micro = days_to_hmsm(frac_days)
    
    return datetime.datetime(year,month,day,hour,min)

#julian_set = jday + sunset_time
#julian_rise = jday + sunrise_time


#print("sunrise", jd_to_datetime(julian_rise), jd_to_datetime(julian_set))