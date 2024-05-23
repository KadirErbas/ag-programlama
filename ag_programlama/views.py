from django.shortcuts import render

# Create your views here.
def home_view(request):    
    return render(request, 'ag_programlama/home.html')



import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST




@csrf_exempt
def get_road_risk_data(request):
    if request.method == 'POST':
        apiKey = '35f149de4dbcba4e08addae19a4cae55'
        apiUrl = f'https://api.openweathermap.org/data/2.5/roadrisk?appid={apiKey}'
        requestBody = json.loads(request.body)

        response = requests.post(apiUrl, json=requestBody)
        
        # Ensure the response is in the correct format
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch data from OpenWeatherMap'}, status=response.status_code)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def get_bus_ticket(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            city_start = body.get('cityStart')
            city_end = body.get('cityEnd')

            if not city_start or not city_end:
                return JsonResponse({'status': 'error', 'message': 'Invalid city names'}, status=400)

            api_url = f"https://api.collectapi.com/travel/busTicket?data.to={city_end}&data.from={city_start}"
            headers = {
                'content-type': 'application/json',
                'authorization': 'apikey 66oJTceaR2rJ6Sdzx56nhm:7psLaL2zOq1kAJSSWNZZfe'
            }

            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data)
            else:
                return JsonResponse({'status': 'error', 'message': f'Error from CollectAPI: {response.status_code}', 'details': response.text}, status=500)
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON in request body'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred', 'details': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)