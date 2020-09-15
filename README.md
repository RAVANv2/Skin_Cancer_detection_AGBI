# Skin_Cancer_detection_AGBI

## Flask API 
Flask api for cancer detection model. To download resnet weight [click here](https://drive.google.com/file/d/152UqL62m27_xgEudL9fSnd1_YegT5YEG/view?usp=sharing) and for fastAI [click here](https://drive.google.com/file/d/1f0qGfKANlS6x_ICG_aMjVe3It5B9XVF6/view?usp=sharing)

Base URL:[http://host:port_number] <br>
port_number = 5000 (Malonoma_stages) and 6000 (skin_infection_types) <br>
Request Method: `Post`

Sample Request<br>
{"src":"path to image"}<br>
Response<br>
{"Class_of_infection","index","Probability"}
