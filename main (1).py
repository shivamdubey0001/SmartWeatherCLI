import requests
import json
from datetime import datetime
import sys

# My OpenWeatherMap API key - get it free from their website
API_KEY = "1db18a58fc1235766e0a3c8088e4e0f0"  # Put your actual API key here
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def check_internet():
    """
    Checks if internet connection is working
    Returns True if connected, False if not
    """
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

def get_weather_data(city_name):
    """
    Fetches weather data from the API
    Takes city name and returns weather information
    """
    # First we check if internet is working
    if not check_internet():
        print("❌ No internet connection!")
        print("💡 Please check your WiFi or mobile data")
        return None

    try:
        # Build the complete URL with city name and API key
        complete_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

        # Make the API call - this might take a moment
        print("🔄 Fetching weather data...")
        response = requests.get(complete_url, timeout=10)

        # Check what kind of response we got
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"❌ City '{city_name}' not found")
            print("💡 Check spelling or try a popular city name")
            return None
        elif response.status_code == 401:
            print("❌ API key is wrong or expired")
            print("💡 Get a new API key from OpenWeatherMap")
            return None
        else:
            print(f"❌ Server error: {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("❌ Request timed out - server is slow")
        print("💡 Try again in a few moments")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - check your internet")
        return None
    except Exception as e:
        print(f"❌ Something went wrong: {str(e)}")
        return None

def show_weather(weather_data, city_name):
    """
    Displays weather information in a nice format
    Takes weather data and city name as input
    """
    if not weather_data:
        print(f"❌ Sorry, couldn't get weather data for '{city_name}'")
        print("💡 Please check the city name spelling")
        return

    try:
        # Extract useful information from the API response
        main_info = weather_data.get('main', {})
        weather_desc = weather_data.get('weather', [{}])[0]
        wind_info = weather_data.get('wind', {})

        # Get current time for display
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Display weather information in a clean format
        print("\n" + "="*55)
        print(f"🌦️  WEATHER REPORT FOR {city_name.upper()}")
        print("="*55)
        print(f"📅 Date & Time: {current_time}")

        # Get temperature safely
        temp = main_info.get('temp', 'N/A')
        if temp != 'N/A':
            temp_f = temp * 9/5 + 32
            print(f"🌡️  Temperature: {temp}°C ({temp_f:.1f}°F)")

        feels_like = main_info.get('feels_like', 'N/A')
        if feels_like != 'N/A':
            print(f"🔥 Feels Like: {feels_like}°C")

        # Get weather description safely
        description = weather_desc.get('description', 'N/A')
        if description != 'N/A':
            print(f"☁️  Weather: {description.title()}")

        # Get wind speed safely
        wind_speed = wind_info.get('speed', 'N/A')
        print(f"💨 Wind Speed: {wind_speed} m/s")

        # Get humidity safely
        humidity = main_info.get('humidity', 'N/A')
        print(f"💧 Humidity: {humidity}%")

        # Get min/max temperature safely
        temp_min = main_info.get('temp_min', 'N/A')
        temp_max = main_info.get('temp_max', 'N/A')
        print(f"🔽 Min Temp: {temp_min}°C")
        print(f"🔺 Max Temp: {temp_max}°C")
        print("="*55)

    except Exception as e:
        print(f"❌ Error displaying weather data: {str(e)}")
        print("💡 Data format might be incorrect")

def get_city_name():
    """
    Gets city name from user with proper validation
    Returns clean city name or None if user wants to quit
    """
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            city = input("\n🏙️  Enter city name (or 'quit' to exit): ").strip()

            # Check if user wants to exit
            if city.lower() in ['quit', 'exit', 'q']:
                return None

            # Check if input is too short
            if not city or len(city) < 2:
                print("❌ Please enter a valid city name")
                attempts += 1
                continue

            # Check if city name contains numbers
            if any(char.isdigit() for char in city):
                print("❌ City names shouldn't contain numbers")
                attempts += 1
                continue

            # Check for special characters
            if any(char in city for char in ['@', '#', '$', '%', '&', '*']):
                print("❌ City names shouldn't contain special characters")
                attempts += 1
                continue

            return city

        except KeyboardInterrupt:
            print("\n👋 Stopping the program...")
            return None
        except Exception as e:
            print(f"❌ Input error: {str(e)}")
            attempts += 1

    print("❌ Too many incorrect attempts. Exiting program.")
    return None

def main():
    """
    Main function that runs the entire weather CLI application
    """
    try:
        print("🌦️  Welcome to Smart Weather CLI!")
        print("Get real-time weather updates for any city")
        print("-" * 45)

        # Check if API key is set up
        if API_KEY == "your_api_key_here":
            print("⚠️  IMPORTANT: Set up your API key first!")
            print("1. Go to https://openweathermap.org/api")
            print("2. Create a free account")
            print("3. Copy your API key")
            print("4. Replace 'your_api_key_here' in the code")
            input("\nPress Enter to continue anyway...")

        # Main program loop
        session_count = 0
        while True:
            try:
                city_name = get_city_name()

                # User wants to quit
                if city_name is None:
                    print("👋 Thanks for using Smart Weather CLI!")
                    break

                print(f"🔍 Getting weather data for {city_name}...")

                # Get weather data from API
                weather_info = get_weather_data(city_name)

                # Display the weather information
                show_weather(weather_info, city_name)

                session_count += 1

                # Continue option
                if session_count < 5:  # Auto-exit after 5 cities
                    continue_choice = input("\n🔄 Want to check another city? (y/n): ").strip().lower()
                    if continue_choice not in ['y', 'yes']:
                        print("👋 Thanks for using Smart Weather CLI!")
                        break
                else:
                    print("👋 You've checked 5 cities. Exiting program.")
                    break

            except KeyboardInterrupt:
                print("\n👋 Stopping the program...")
                break
            except Exception as e:
                print(f"❌ Error in main loop: {str(e)}")
                print("💡 Try restarting the program")
                break

    except Exception as e:
        print(f"❌ Program couldn't start: {str(e)}")
        print("💡 Check your code or internet connection")

def safe_exit():
    """
    Safely exits the program
    """
    try:
        print("\n👋 Program exiting safely...")
        sys.exit(0)
    except:
        print("Program has exited")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 User stopped the program")
        safe_exit()
    except Exception as e:
        print(f"❌ Final error: {str(e)}")
        print("💡 Please check your code")
        safe_exit()