# EWAS_Android

## Running the program.
	1. Download Project.
	2. Install dependencies [ pip install -r Important_Documents/requirements.txt ]
	3. There are 2 ways to run it:
	    A) Run (Double-Click) EWAS "Application.exe"
	    ------------------------------------------------
	    B.1) Edit run.bat to your:
		Python .exe --> "C:\Users\[YOUR USERNAME]\AppData\Local\Programs\Python\Python37\python.exe"
		main.py --> "C:\Users\[YOUR USERNAME]\[YOUR PATH]\EWAS_Application\main.py"
	    B.2). Open (Double-Click) run.bat to run the program next time. 

### Count conversion to input voltage
    $$ Vin=(counts)(298^-9)(12) / gain $$
	
### Instructions to begin recording.
    1. Write a Test Name.
    2. Input Test Duration.
    3. Set Location Name.
    4. Select Location Source (GPS | Individual Module Location Description)
        [--- GPS ---]
        1.1 Synchronize GPS with button.
        2.1 Manually Set Latitud and longitud. (NMEA)
        2.2 Manually Set Time. (Hour, Minute and seconds)
        
        [--- Module Location Information ---]
        1. Write a description for the location of the sensors in each module.
    
    5. Select Cutoff Frequency
    6. Select Sampling rate or use suggested.
    7. Select Gain
    
    [---OPTIONAL---]
    8. Set sensor information:
        8.1 Sensor Name,
        8.2 Sensor Type
        8.3 Sensitivity
        8.4 Bandwidth
        8.5 Full-Scale
        8.6 Damping
        8.7 More detailed description of each sensor localization.
    9. START
