from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.duration import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration_of_visit_seconds = get_duration(visit)
        visit_with_duration = {
            "who_entered": visit.passcard,
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(duration_of_visit_seconds),
            "is_strange": is_visit_long(visit)
        }
        non_closed_visits.append(visit_with_duration)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
