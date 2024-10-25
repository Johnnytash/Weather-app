from django.shortcuts import render
import requests
import datetime
from django.contrib import messages
from django.conf import settings

def home(request):
    city = request.POST.get('city', 'Nairobi')
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}'
    PARAMS = {'units': 'metric'}

    # Default values including the default image URL
    DEFAULT_IMAGE = 'https://unsplash.com/photos/silhouette-of-trees-during-daytime-QRBe3Ithczs'
    
    context = {
        'description': 'clear sky',
        'icon': '01d',
        'temp': 25,
        'day': datetime.date.today(),
        'city': 'Nairobi',  # Reset to Nairobi if city not found
        'exception_occurred': False,
        'image_url': DEFAULT_IMAGE
    }

    try:
        # Weather API request
        weather_response = requests.get(weather_url, params=PARAMS, timeout=5)
        weather_response.raise_for_status()  # Raises an HTTPError for bad responses
        data = weather_response.json()

        # Check if the API returned an error message
        if 'cod' in data and str(data['cod']) != '200':
            if str(data['cod']) == '404':
                messages.error(request, f"City '{city}' not found. Showing default city information.")
                return render(request, 'weatherapp/index.html', context)
            else:
                messages.error(request, f"Weather API Error: {data.get('message', 'Unknown error')}")
                context['exception_occurred'] = True
                return render(request, 'weatherapp/index.html', context)

        # Update context with weather data
        context.update({
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'temp': data['main']['temp'],
            'city': city  # Update city only if it's valid
        })

        # Only try to get a new image if the city was found successfully
        try:
            query = f"{city} 1920x1080"
            city_url = f"https://www.googleapis.com/customsearch/v1"
            search_params = {
                'key': settings.GOOGLE_API_KEY,
                'cx': settings.SEARCH_ENGINE_ID,
                'q': query,
                'searchType': 'image',
                'imgSize': 'xlarge',
                'num': 2
            }
            
            image_response = requests.get(city_url, params=search_params, timeout=5)
            image_response.raise_for_status()
            image_data = image_response.json()
            
            search_items = image_data.get("items", [])
            if search_items and len(search_items) > 1:
                context['image_url'] = search_items[1]['link']
            else:
                context['image_url'] = DEFAULT_IMAGE
        
        except requests.exceptions.RequestException as e:
            # Log the error but keep the default image
            print(f"Image API error: {str(e)}")
            messages.warning(request, "Could not load city image, using default instead.")
            context['image_url'] = DEFAULT_IMAGE

    except requests.exceptions.RequestException as e:
        context['exception_occurred'] = True
        error_message = str(e)
        if 'ConnectTimeout' in error_message:
            messages.error(request, 'Connection timed out. Please try again.')
        else:
            messages.error(request, f'Could not retrieve weather data: {error_message}')

    return render(request, 'weatherapp/index.html', context)