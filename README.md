# Skin_Cancer_detection_AGBI

`pip install gdown`


## Flask API 
Flask api for cancer detection model. To download 
- resnet weight [click here](https://drive.google.com/file/d/152UqL62m27_xgEudL9fSnd1_YegT5YEG/view?usp=sharing) 
`gdown https://drive.google.com/uc?id=152UqL62m27_xgEudL9fSnd1_YegT5YEG&export=download`

- and for fastAI [click here](https://drive.google.com/file/d/1f0qGfKANlS6x_ICG_aMjVe3It5B9XVF6/view?usp=sharing)
`gdown https://drive.google.com/u/0/uc?id=1f0qGfKANlS6x_ICG_aMjVe3It5B9XVF6&export=download`



Base URL: [http://host:port_number/

#### 1. For (Malonoma_stages)

Here : http://0.0.0.0:5005/

Request Method: `POST`

Endpoing: `/`

Parameter:

| Parameter | Data Type | Value | Required |
|-----------|-----------|-------|----------|
| user_id_to_test | string | any unique user id | True |
| image_for_test|string|base64image| True|

Sample Request:  

`Content-Type: application/json`


{
    "user_id_to_test": "<unique user id>",
    "image_for_test":"< base64image >"
}


Response:

{ "errorcode": 0, "value": "[4.9043792e-06 9.9999511e-01]", "result": "success" }

or 

{ "errorcode": -1, "result": "Eror in Resnet Model" }

or 

{ "errorcode": -2, "result": "Unable to Read base 64 image" }


#### 2. For (skin_infection_types)

Here : http://0.0.0.0:6000/

Request Method: `POST`

Endpoing: `/`

Parameter:

| Parameter | Data Type | Value | Required |
|-----------|-----------|-------|----------|
| user_id_to_test | string | any unique user id | True |
| image_for_test|string|base64image| True|

Sample Request:  

`Content-Type: application/json`


{
    "user_id_to_test": "<unique user id>",
    "image_for_test":"< base64image >"
}


Response:


{
    "value": "[4.9043792e-06 9.9999511e-01]"
}


------------------------

Sample Request<br>
{"src":"path to image"}<br>
Response<br>
{"Class_of_infection","index","Probability"}

-------------------------
