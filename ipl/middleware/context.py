from django.urls import reverse


def extra_context(request):
    context = {
        "driver_url":reverse('application:driver'),
        "truck_url": reverse('application:truck'),
        "consignee_url": reverse('application:consignee'),
        "consignor_url": reverse('application:consignor'),
        "landingpage_url": reverse('application:landingpage'),
        "logout_url": reverse('account:logout')
    }

    return context