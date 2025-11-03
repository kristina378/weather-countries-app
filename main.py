from servises.open_weather import fetch_weather
from servises.excel_file import append_to_excel
import time



# CROM
while True: #constantly getting data
    weather = fetch_weather()
    append_to_excel(weather)
    print("Pobrano nowe dane")
    time.sleep(10)
