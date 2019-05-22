This document is meant for students who keep working on this application.
DEV.md contains instructions to download all needed python dependencies and software to be able to edit the GUI and the code.

## Installing all needed dependencies.
	1. Install Python 3.7.1
	2. Intall pip by runnig EWAS_Application/Important_Documents/get-pip.py
	3. Install dependencies [ pip install -r Important_Documents/requirements.txt ]


## Downloading and Opening PyQt Designer.
	1. Install Python 3.7.1
	2. Intall pip by runnig EWAS_Application/Important_Documents/get-pip.py
	3. pip install PyQt5
	4. pip install pyqt-tools --pre
	5. Open QtDesigner. **Keep in mind that some of these files may be hidden.
		C:\Users\[YOUR USERNAME]\AppData\Local\Programs\Python\Python37\Lib\site-packages\pyqt5_tools\designer


## Generating executable File
    1. Install PyInstaller. [ pip install pyinstaller ]
    2. cd into EWAS_Application.
    3. Try [ pyinstaller -F main.py -n EWAS Application.exe ] OR
        [ pyinstaller -F main.py ] then rename executable file. 
    
Suggested to use PyCharm IDE as it is easiest to integrate with git.
