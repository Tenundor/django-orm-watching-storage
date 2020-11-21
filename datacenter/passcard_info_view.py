from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.format_duration import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    this_passcard_visits = []

    for visit in Visit.objects.filter(passcard=passcard):
        visit_with_duration_no_name = {
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long()
        }
        this_passcard_visits.append(visit_with_duration_no_name)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
