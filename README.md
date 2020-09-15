# Skin_Cancer_detection_AGBI

## Flask API 
Flask api for cancer detection model. To download resnet weight [click here](https://drive.google.com/file/d/152UqL62m27_xgEudL9fSnd1_YegT5YEG/view?usp=sharing) and for fastAI [click here](https://drive.google.com/file/d/1f0qGfKANlS6x_ICG_aMjVe3It5B9XVF6/view?usp=sharing)


`pip install gdown`
`gdown https://drive.google.com/uc?id=152UqL62m27_xgEudL9fSnd1_YegT5YEG&export=download`


Base URL: [http://host:port_number/

#### 1. For (Malonoma_stages)

Here : http://0.0.0.0:5005/

Request Method: `POST`

Endpoing: `/`

Parameter:

| Parameter | Data Type | Value | Required |
|-----------|-----------|-------|----------|
| user_id_to_test | string | any unique user id | True |
| enrollmentimages|string|base64image| True|

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


#### 1. For (skin_infection_types)

Here : http://0.0.0.0:6000/

Request Method: `POST`

Endpoing: `/`

Parameter:

| Parameter | Data Type | Value | Required |
|-----------|-----------|-------|----------|
| user_id_to_test | string | any unique user id | True |
| enrollmentimages|string|base64image| True|

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
