# Weather Dashboard

A Django-based weather application that displays real-time weather information and dynamic city backgrounds. The application fetches weather data from OpenWeatherMap API and city images from Google Custom Search API.

![Weather Dashboard Preview]

![alt text](<Screenshot 2024-10-25 125947-1.png>)

## Features

- Real-time weather information display
- Dynamic background images based on the searched city
- Responsive design for mobile and desktop
- Error handling with user-friendly messages
- Default fallback for unavailable cities
- Clean, modern UI with blur effect and transparent elements

## Technologies Used

- Django 5.1.1
- Python 3.12
- OpenWeatherMap API
- Google Custom Search API
- HTML5/CSS3
- JavaScript

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.12 or higher installed
- pip (Python package manager)
- Git (optional, for cloning the repository)
- API Keys:
  - OpenWeatherMap API key
  - Google Custom Search API key
  - Google Search Engine ID

## Installation

1. Clone the repository (or download the ZIP file):
```bash
git clone <repository-url>
cd weatherproject
```

2. Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install django requests python-decouple
```

4. Create a `.env` file in the project root with your API keys:
```plaintext
SECRET_KEY=your_django_secret_key
DEBUG=True
WEATHER_API_KEY=your_openweathermap_api_key
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id
```

5. Create the static directory:
```bash
mkdir static
```

6. Apply migrations:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000` in your browser


## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```plaintext
SECRET_KEY=your_django_secret_key
DEBUG=True
WEATHER_API_KEY=your_openweathermap_api_key
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id
```

### API Keys Setup

1. **OpenWeatherMap API Key**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Generate an API key
   - Add to `.env` file as `WEATHER_API_KEY`

2. **Google Custom Search API**:
   - Visit [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project
   - Enable Custom Search API
   - Create credentials (API key)
   - Set up a Custom Search Engine at [Google Programmable Search Engine](https://programmablesearchengine.google.com)
   - Add both keys to `.env` file

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://127.0.0.1:8000`

3. Enter a city name in the search box and click the search button

4. View the weather information and dynamic background image for the searched city

## Features Explanation

### Weather Information
- Temperature in Celsius
- Weather condition description
- Weather icon
- Current date

### Dynamic Backgrounds
- Changes based on the searched city
- Falls back to default image if:
  - City is not found
  - API request fails
  - No suitable image is found

### Error Handling
- Invalid city names
- API timeout errors
- Network connectivity issues
- Missing API keys

## Customization

### Styling
Modify `static/css/style.css` to change the appearance:
- Color scheme in `:root` variables
- Container dimensions
- Responsive breakpoints
- Background blur effects

### Default Values
Modify `views.py` to change default settings:
- Default city
- Default temperature
- Default background image
- Timeout values
- API parameters

## Troubleshooting

1. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Ensure `STATIC_URL` and `STATICFILES_DIRS` are properly configured

2. **API Errors**
   - Verify API keys in `.env` file
   - Check API quota limits
   - Ensure proper network connectivity

3. **Database Errors**
   - Run `python manage.py migrate`
   - Check database configuration in settings.py

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT licence

## Acknowledgments

- OpenWeatherMap for weather data
- Google Custom Search for city images
- Django community for the framework
