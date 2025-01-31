from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from datetime import datetime,timezone

@csrf_exempt
@require_GET
def hng_public_api(request):
    response_data = {
        "email": "victoroduorr@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/OviLab-sys/hng-stage0"
    }
    return JsonResponse(response_data)

