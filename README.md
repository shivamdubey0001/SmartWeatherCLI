
# 🌦️ Smart Weather CLI

> A Python command-line interface tool to get real-time weather updates for any city using the OpenWeatherMap API.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- ✅ Real-time weather data for any city worldwide
- 🌡️ Temperature in both Celsius and Fahrenheit
- 💨 Wind speed, humidity, and atmospheric conditions
- 🔍 Smart error handling for invalid cities
- 🛡️ Internet connection validation
- 🎨 User-friendly interface with emojis
- 🔄 Session management with multiple city lookups
- ⚡ Fast API response with timeout handling

## 📋 Prerequisites

- Python 3.11+
- Internet connection
- OpenWeatherMap API key (free)

## 🛠️ Installation & Setup

1. **Clone this repository:**
```bash
git clone https://github.com/shivamdubey0001/SmartWeatherCLI.git
cd SmartWeatherCLI
```

2. **Install required packages:**
```bash
pip install requests
```

3. **Get your FREE API key:**
   - Visit [OpenWeatherMap API](https://openweathermap.org/api)
   - Create a free account
   - Copy your API key

4. **Configure API key in main.py:**
```python
API_KEY = "your_actual_api_key_here"  # Replace with your key
```

## 🎯 Usage

**Run the application:**
```bash
python main.py
```

**Follow the interactive prompts:**
- Enter any city name when prompted
- View detailed weather information
- Type 'quit' to exit
- Choose 'y' or 'n' to check another city

## 📱 Example Output

```
🌦️  Welcome to Smart Weather CLI!
Get real-time weather updates for any city
---------------------------------------------

🏙️  Enter city name (or 'quit' to exit): London
🔍 Getting weather data for London...
🔄 Fetching weather data...

=======================================================
🌦️  WEATHER REPORT FOR LONDON
=======================================================
📅 Date & Time: 07-07-2025 15:29:10
🌡️  Temperature: 20.82°C (69.5°F)
🔥 Feels Like: 20.18°C
☁️  Weather: Scattered Clouds
💨 Wind Speed: 5.88 m/s
💧 Humidity: 47%
🔽 Min Temp: 20.82°C
🔺 Max Temp: 20.82°C
=======================================================
```

## 🔧 Technical Features

- **Smart Input Validation**: Prevents invalid city names
- **Error Handling**: Graceful handling of network issues
- **API Security**: Secure API key management
- **Session Control**: Auto-exit after 5 cities
- **Cross-Platform**: Works on Windows, macOS, Linux
- **No Dependencies**: Only uses standard Python libraries + requests

## 🌟 Key Highlights

- **Real-time Data**: Direct integration with OpenWeatherMap API
- **User Experience**: Intuitive command-line interface
- **Robust**: Handles network timeouts and API errors
- **Educational**: Clean, well-commented code for learning

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/) for weather data
- Python `requests` library for HTTP requests

---

**Made with ❤️ by [Shivam Dubey](https://github.com/shivamdubey0001)**

⭐ Star this repo if you found it helpful!
