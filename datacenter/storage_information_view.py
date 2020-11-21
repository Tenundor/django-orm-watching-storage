from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.format_duration import format_duration


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        visit_with_duration = {
            "who_entered": visit.passcard,
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long()
        }
        non_closed_visits.append(visit_with_duration)

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
