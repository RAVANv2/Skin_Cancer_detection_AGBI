# iVision: Skin Cancer Detection

### Whole demo and working to run the website can be found here 

https://www.loom.com/share/ebc43e6724804237895b497915320344  

or you can follow the below steps


### Step 1 : Clone the directory
 

`git clone https://github.com/RAVANv2/Skin_Cancer_detection_AGBI.git`


`cd Skin_Cancer_detection_AGBI`
              
### Step 2 : Creating virtual environment
`pip install virtualenv`

`virtualenv venv -p python3`

### Step 3: Activating Virtual environment


`source venv/bin/activate`

### Step 4: Installing Requirements


`pip install -r requirements.txt`

### Step 5: Running Individual Services


### STep 5.1: For Website Service


Change directory to `cd website`


Type in code `python3 skin_app.py`


### STep 5.2: For Skin Cancer Prediction Model Service

open new terminal using `ctrl+shift+T`


Change directory to root `cd ..` 


Change directory to `cd flask_api/skin_infection_types`


Type in code `python3 app.py`


### STep 5.3: For Near-by hospital Service

open new terminal using `ctrl+shift+T`


Change directory to root `cd ../`


Change directory to `cd MAP/nearby`


Type in code `python3 main.py`

### STep 5.4: For Directions to hospital Service

open new terminal using `ctrl+shift+T`


Change directory to root `cd ../`


Change directory to `cd MAP/map_route`


Type in code `python3 app.py`




### 6. Hitting the Website service on localhost

Here : http://0.0.0.0:7007/


`And you will see our website made with love`

# Our Android Application

### Whole demo and working to run the Android APP can be found here 

https://www.loom.com/share/da1ad40ba03e40b0b59533e5e28e2257  

or you can follow the below steps


### Step 1. Install Android Studio on Ubuntu 18.04

#### Java Installation
`sudo apt update`

`sudo apt install openjdk-8-jdk`

`java -version`

#### Installing Android Studio
`sudo snap install android-studio --classic`

Output

android-studio 3.3.1.0 from Snapcrafters installed

### Step 2. Open Android Studio and click on the open new project.
![](https://github.com/RAVANv2/Skin_Cancer_detection_AGBI/blob/master/Android_app/screenshots/studio.PNG)


### Step 3. Slect the unzipped folder and build the sdk

### Step 4. Now plugin in your device and enable debugging from developer settings

### Step 5. Click on the build and install apk on your mobile device.

![](https://github.com/RAVANv2/Skin_Cancer_detection_AGBI/blob/master/Android_app/screenshots/congo.PNG)

