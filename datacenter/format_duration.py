def format_duration(seconds):
    mm = seconds // 60
    hh, mm = divmod(mm, 60)
    return '{0:02d}ч {1:02d}мин'.format(hh, mm)
