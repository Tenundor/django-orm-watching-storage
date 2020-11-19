from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    """
    Returns the time spent by an employee in the storage in seconds (int)

    Parameters
    ----------
    visit : <class 'datacenter.models.Visit'>
    """
    entered_at_localtime = localtime(visit.entered_at)
    current_localtime = localtime()
    datetime_delta = current_localtime - entered_at_localtime

    return int(datetime_delta.total_seconds())


def format_duration(seconds):
    mm = seconds // 60
    hh, mm = divmod(mm, 60)

    return '{0:02d}ч {1:02d}мин'.format(hh, mm)


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration_of_visit_seconds = get_duration(visit)
        visit_with_duration = {
            "who_entered": visit.passcard,
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(duration_of_visit_seconds)
        }
        non_closed_visits.append(visit_with_duration)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
