# 🌤️ Weather Info Viewer

A simple yet functional desktop application built with Python and Tkinter to fetch and display real-time weather data using the OpenWeatherMap API.

---

## 📦 Features

- 🔍 Get current weather details by city name
- 📍 Auto-fetch country code of queried city
- 🌡️ View temperature, feels-like temperature, humidity, wind speed, and cloudiness
- 🌅 Displays sunrise and sunset time (local to city)
- 🖼️ Displays a decorative image
- 🔑 Save and reuse your OpenWeatherMap API key (stored locally)
- 🔁 Clear current data on the interface
- 🧪 Gracefully handles API errors and empty inputs
- 🧭 Intuitive and responsive layout using `grid()`

---

## 🧰 Requirements

- Python 3.x
- Modules:
  - `requests`
  - `tkinter` *(built-in with Python)*
  - `Pillow` *(for image support)*

---

## 🛠️ Installation & Setup

### 1. Clone the repository or download the `.zip`:

```bash
git clone https://github.com/ManaenB/weather-info-viewer.git
cd weather-info-viewer
````

### 2. Create a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application:

```bash
python weather_info_viewer.py
```

---

## 🔑 API Key Setup

To use the app, you’ll need an API key from [OpenWeatherMap](https://openweathermap.org/api):

1. Sign up and generate a free API key.
2. Launch the app and click the **API Key** button.
3. Paste your API key and click **Save**.
4. The key is stored securely in a local `config.json` file.

---

## 🖼️ Notes

* The decorative image (`ran.jpg`) must be present in the same folder as the script. You can choose to change it.
* The saved API key can be replaced any time by re-entering a new one; either directly from the **config.json** file or from the launched Aopp 

---

## 📁 Project Structure

```
weather-info-viewer/
│
├── weather_info_viewer.py        # Main application script
├── config.json                   # Stores API key (auto-generated)
├── ran.jpg                       # Image shown in the GUI
├── requirements.txt              # List of required packages
└── README.md                     # This file
```



## 🤝 Contribution

Feel free to fork this repository, suggest improvements, or open pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by **ManaenB** — a back-street Python & C# coder in the making 💻🚀

```
