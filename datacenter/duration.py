from django.utils.timezone import localtime


def get_duration(visit):
    """
    :param visit: <class 'datacenter.models.Visit'>
    :return: Returns the time spent by an employee in the storage in seconds (int)
    """
    if visit.leaved_at is None:
        entered_at_localtime = localtime(visit.entered_at)
        current_localtime = localtime()
        datetime_delta = current_localtime - entered_at_localtime

        return int(datetime_delta.total_seconds())
    else:
        visit_duration_time = visit.leaved_at - visit.entered_at

        return int(visit_duration_time.total_seconds())


def format_duration(seconds):
    """
    :param seconds: int
    :return: Returns the time duration in the format 'hh ч mm мин'
    """
    mm = seconds // 60
    hh, mm = divmod(mm, 60)

    return '{0:02d}ч {1:02d}мин'.format(hh, mm)


def is_visit_long(visit, minutes=60):
    """
    :param visit: <class 'datacenter.models.Visit'>
    :param minutes: int
    :return: Boolean
    """
    visit_duration_minutes = get_duration(visit) // 60
    if visit_duration_minutes > minutes:
        return True
    else:
        return False
