from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET


@csrf_exempt
@require_GET
def hng_public_api(request):
    response_data = {
        "email": "victoroduorr@gmail.com",  # Update with your email
        "current_datetime": now().isoformat(timespec='milliseconds') + "Z",  # Including milliseconds
        "github_url": "https://github.com/OviLab-sys/hng-stage0"  # Update with your GitHub URL
    }
    return JsonResponse(response_data)
