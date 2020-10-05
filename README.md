# iVision: Skin Cancer Detection

#### Step 1 : Clone the directory
 

`git clone https://github.com/RAVANv2/Skin_Cancer_detection_AGBI.git`


`cd Skin_Cancer_detection_AGBI`
              
#### Step 2 : Creating virtual environment
`pip install virtualenv`

`virtualenv venv -p python3`

#### Step 3: Activating Virtual environment


`source venv/bin/activate`

#### Step 4: Installing Requirements


`pip install -r requirements`

#### Step 5: Running Individual Services


#### STep 5.1: For Website Service


Change directory to `cd website`


Type in code `python3 skin_app.py`


#### STep 5.2: For Skin Cancer Prediction Model Service

Change directory to root `cd ..` 


Change directory to `cd skin_infection_types`


Type in code `python3 app.py`


#### STep 5.3: For Near-by hospital Service

Change directory to root `cd ..` 


Change directory to `cd MAP/nearby`


Type in code `python3 main.py`

#### STep 5.3: For Directions to hospital Service

Change directory to root `cd ..` 


Change directory to `cd MAP/map_route`


Type in code `python3 app.py`




#### 6. Hitting the Website service on localhost

Here : http://0.0.0.0:7007/


`And you will see our website made with love`
