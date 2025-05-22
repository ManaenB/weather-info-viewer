
import tkinter.messagebox
import requests
import datetime
import tkinter
from PIL import Image, ImageTk
import os
import json



class WeatherApp:
    def __init__(self, weather_app):
        weather_app.title("Weather Report Viewer")
        weather_app.geometry("400x370")
        weather_app.resizable(False, False)

        target_city_label = tkinter.Label(weather_app, text="City Name: ")
        target_city_label.grid(row=0, column=0,sticky="w")
        self.target_city_var = tkinter.StringVar()
        self.target_city_entry = tkinter.Entry(weather_app, textvariable=self.target_city_var)
        self.target_city_entry.grid(row=0, column=1)

        blank_1 = tkinter.Label(weather_app, text="",width=2)
        blank_1.grid(row=0,column=2)

        country_code_label = tkinter.Label(weather_app,text="Country Code: ")
        country_code_label.grid(row=0,column=3,sticky="w")
        self.country_code_var = tkinter.StringVar()
        self.country_code_entry = tkinter.Entry(weather_app,textvariable=self.country_code_var,state="readonly",width=10)
        self.country_code_entry.grid(row=0,column=4)

        blank_2 = tkinter.Label(weather_app)
        blank_2.grid(row=1)

        weather_description_label = tkinter.Label(weather_app,text="Description: ")
        weather_description_label.grid(row=2,column=0,sticky="w")
        self.weather_description_var = tkinter.StringVar()
        self.weather_description_entry = tkinter.Entry(weather_app,textvariable=self.weather_description_var,state="readonly")
        self.weather_description_entry.grid(row=2,column=1,columnspan=4,sticky="ew")

        blank_2 = tkinter.Label(weather_app)
        blank_2.grid(row=3)

        average_temperature_label = tkinter.Label(weather_app,text="Temperature: ")
        average_temperature_label.grid(row=4,column=0,sticky="w")
        self.average_temperature_var = tkinter.StringVar()
        self.average_temperature_entry = tkinter.Entry(weather_app,textvariable=self.average_temperature_var,state="readonly")
        self.average_temperature_entry.grid(row=4,column=1)

        blank_3 = tkinter.Label(weather_app,text="")
        blank_3.grid(row=4,column=2,sticky="w")
        feels_like_temperature_label = tkinter.Label(weather_app, text="Feels Like: ")
        feels_like_temperature_label.grid(row=4, column=3,sticky="w")
        self.feels_like_temperature_var = tkinter.StringVar()
        self.feels_like_temperature_entry = tkinter.Entry(weather_app,textvariable=self.feels_like_temperature_var,state="readonly",width=10)
        self.feels_like_temperature_entry.grid(row=4,column=4)

        blank_4 = tkinter.Label(weather_app)
        blank_4.grid(row=5)

        humidity_label = tkinter.Label(weather_app,text="Humidity: ")
        humidity_label.grid(row=6,column=0,sticky="w")
        self.humidity_var = tkinter.StringVar()
        self.humidity_entry = tkinter.Entry(weather_app,textvariable=self.humidity_var,state="readonly")
        self.humidity_entry.grid(row=6,column=1)

        blank_5 = tkinter.Label(weather_app)
        blank_5.grid(row=7,column=0,columnspan=2)

        wind_speed_label = tkinter.Label(weather_app,text="Wind Speed: ")
        wind_speed_label.grid(row=8,column=0,sticky="w")
        self.wind_speed_var = tkinter.StringVar()
        self.wind_speed_entry = tkinter.Entry(weather_app,textvariable=self.wind_speed_var,state="readonly")
        self.wind_speed_entry.grid(row=8, column=1)

        blank_6 = tkinter.Label(weather_app)
        blank_6.grid(row=9,column=0,columnspan=2)

        cloudiness_label = tkinter.Label(weather_app,text="Cloudiness: ")
        cloudiness_label.grid(row=10,column=0,sticky="w")
        self.cloudiness_var = tkinter.StringVar()
        self.cloudiness_entry = tkinter.Entry(weather_app,textvariable=self.cloudiness_var,state="readonly")
        self.cloudiness_entry.grid(row=10,column=1)

        blank_7 = tkinter.Label(weather_app)
        blank_7.grid(row=11,column=0,columnspan=2)

        sunrise_time_label = tkinter.Label(weather_app, text="Sunrise at: ")
        sunrise_time_label.grid(row=12,column=0,sticky="w")
        self.sunrise_time_var = tkinter.StringVar()
        self.sunrise_time_entry = tkinter.Entry(weather_app,textvariable=self.sunrise_time_var,state="readonly")
        self.sunrise_time_entry.grid(row=12,column=1)

        blank_7 = tkinter.Label(weather_app)
        blank_7.grid(row=13,column=0,columnspan=2)

        sunset_time_label = tkinter.Label(weather_app,text="Sunset at: ")
        sunset_time_label.grid( row=14,column=0,sticky="w")
        self.sunset_time_var = tkinter.StringVar()
        self.sunset_time_entry = tkinter.Entry(weather_app,textvariable=self.sunset_time_var,state="readonly")
        self.sunset_time_entry.grid( row=14,column=1)

        if os.path.exists("ran.jpg"):
            #Inserting image to the app
            image = Image.open("ran.jpg")
            image = image.resize((150,150))
            self.photo = ImageTk.PhotoImage(image)
            self.ran_photo = tkinter.Label(weather_app,image=self.photo,width=200)
            self.ran_photo.grid(row=6, column=2, rowspan=9, columnspan=4, sticky="nsew") # Set image to occupy the right portion of the window starting from row 6 through row 14 and from column 2 onwards effectively filling the extra space to the right of data fields like humidity, wind speed, etc.

        # blank_8 = tkinter.Label(weather_app)
        # blank_8.grid(row=15)

        button_frame = tkinter.Frame(weather_app)
        button_frame.grid(row=15, column=0, columnspan=6, pady=(10, 0))  # Spread across all columns, below image and inputs

        self.get_data_to_app_btn = tkinter.Button(button_frame, text="Get", width=10,command=self.update_weather_app)
        self.get_data_to_app_btn.pack(side="left", padx=5)

        self.input_API_key_btn = tkinter.Button(button_frame, text="API Key", width=10,command=self.set_API_key)
        self.input_API_key_btn.pack(side="left", padx=5)

        self.clear_data_on_app_btn = tkinter.Button(button_frame, text="Clear", width=10,command=self.clear_weather_app)
        self.clear_data_on_app_btn.pack(side="left", padx=5)

    # puts GET request to OpenWeatherMap API and return the received data as dictionary
    def request_weather_report(self,CITY_NAME):
        try:
            with open("config.json","r") as file:
                weather_info_dict = json.load(file)
                API_kEY = weather_info_dict.get("API_KEY")
                if not API_kEY:
                    raise ValueError("API missing in config.json file")
        except Exception as e:
            tkinter.messagebox.showerror("API Error",f"Could not read API key\nError Message: {e}")
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q":CITY_NAME,
            "appid":API_kEY
        }

        headers = {
            "content-type":"application/json",
            "accept":"application/json",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
        }

        if CITY_NAME:
            try:
                response = requests.get(BASE_URL, params=params,headers=headers)
                if response.status_code == 200:
                    weather_report = response.json()
                    return weather_report
                else:
                    if response.status_code >=400 or response.status_code <500:
                        tkinter.messagebox.showerror("Client Error","Enter Valid City Name or\nUse Valid API_KEY for openWeathermap API")
                    elif response.status_code >=500:
                        tkinter.messagebox.showerror("Server Error","Unable to establish Connection with Server")
                    else:
                        tkinter.messagebox.showerror("API Error",f"API status Code: {response.status_code}")
            except Exception as e:
                tkinter.messagebox.showerror("Connection Error",f"Something went wrong!\nCheck your Internet Connection.\nError Mesaage: {e}")
        else:
            tkinter.messagebox.showwarning("Field Empty Error","City Name Entry cannot be empty")
            


    # Updates the fields on the GUI when the "get" button is clicked
    def update_weather_app(self):
        CITY_NAME = self.target_city_var.get().capitalize().strip()
        self.clear_weather_app()   
        weather_report = self.request_weather_report(CITY_NAME)
        if weather_report:
            #Extracting data
            city = weather_report['name']
            country = weather_report['sys']['country']
            weather_description = weather_report['weather'][0]['description']
            temperature = self.convert_kelvin_to_celsius(weather_report['main']['temp'])
            feels_like = self.convert_kelvin_to_celsius(weather_report['main']['feels_like'])
            humidity = weather_report['main']['humidity']
            wind_speed = weather_report['wind']['speed']
            cloudiness = weather_report['clouds']['all']
            sunrise = self.convert_time(weather_report['sys']['sunrise'])
            sunset = self.convert_time(weather_report['sys']['sunset'])

            # DisplayIng each data in the appropriate Fields on the GUI
            self.target_city_var.set(city) 
            self.country_code_var.set(country)
            self.weather_description_var.set(f"{weather_description.capitalize()}")
            self.average_temperature_var.set(f"{temperature}°C")
            self.feels_like_temperature_var.set(f"{feels_like}°C")
            self.humidity_var.set(f"{humidity}%")
            self.wind_speed_var.set(f"{wind_speed}m/s")
            self.cloudiness_var.set(f"{cloudiness}%")
            self.sunrise_time_var.set(f"{sunrise}")
            self.sunset_time_var.set(f"{sunset}")
        
    # Converts temperature value from Kelvin to Degress Celisus and returns it
    def convert_kelvin_to_celsius(self,kelvin_var):
        return round(kelvin_var-273, 2)
    
    # Converts unix timestamp to human readable format and returns it
    def convert_time(self,unix_time):
        return datetime.datetime.fromtimestamp(unix_time).strftime("%d-%m-%Y, %H:%M:%S")
    
    # CLears each field on the GUI of data
    def clear_weather_app(self):
        self.target_city_var.set("")
        self.country_code_var.set("")
        self.weather_description_var.set("")
        self.average_temperature_var.set("")
        self.feels_like_temperature_var.set("")
        self.humidity_var.set("")
        self.wind_speed_var.set("")
        self.cloudiness_var.set("")
        self.sunrise_time_var.set("")
        self.sunset_time_var.set("")

    # Allows the setting of API key directly from the GUI
    def set_API_key(self):
        
        API_key_collector_app = tkinter.Tk()
        
        API_key_collector_app.title("Enter API Key - Weather Report Veiwer")
        API_key_collector_app.geometry("400x101")
        API_key_collector_app.resizable(False,False)
        
        notice_label_one = tkinter.Label(API_key_collector_app, text="Must use API key for OpenWeatherMap API",font=("Arial",10),)
        notice_label_one.grid(row=0,column=0,padx=5,pady=5)

        frame = tkinter.Frame(API_key_collector_app)
        frame.grid(row=1, column=0, columnspan=8,padx=10,pady=10)

        

        
        key_entry = tkinter.Entry(frame,width=40)
        key_entry.grid(row=0,column=0,columnspan=4,padx=10,pady=5,sticky="ew")
        key_entry_save_btn = tkinter.Button(frame,state="active",text="Save Key",width=10,command=lambda:self.save_API_key_to_file(key_entry,API_key_collector_app,))
        key_entry_save_btn.grid(row=0,column=5,columnspan=4)

        notice_label_two = tkinter.Label(API_key_collector_app, text="Note: Entering a new API KEY will override the previous one",font=("Arial",10),)
        notice_label_two.grid(row=2,column=0,padx=1,pady=1)

        
        API_key_collector_app.mainloop()

    # Saves the Entered API Key to a JSON file
    def save_API_key_to_file(self,key_entry_var,API_key_collector_app):   
            API_KEY = key_entry_var.get()
            print(API_KEY)
            if API_KEY != "":        
                with open("config.json","w") as file:
                    data={
                        "API_KEY":f"{API_KEY}"
                    }
                    json.dump(data,file)
                    tkinter.messagebox.showinfo("Saving API KEY - Weather Report Viewer","API Key saved successfully.\nNote: Entering a new API KEY will override the previous one")
                    API_key_collector_app.destroy()
            else:
                tkinter.messagebox.showwarning("Field Empty Error","The Entry must not be empty")
    
def main():

    weather_app = tkinter.Tk()
    WeatherApp(weather_app) # Creates an instance of the WeatherApp
    weather_app.mainloop()

if __name__ == "__main__":
    main()