
# Solaris Backend
[![244326655-332221555363473-4636031536199997176-n.jpg](https://i.postimg.cc/pLmcczpd/244326655-332221555363473-4636031536199997176-n.jpg)](https://postimg.cc/Mn8Yvc0k)
The core of the "Solaris" web app and the mobile app is its backend REST API. This is where the fetching of data occurs. And our calculation for optimal tilt angle is also done here

You can view are web app [here](https://solaris-bd.web.app/)


### Challenges
---
While building the web app for "Solaris", we encountered two huge problems : 
  - #### CORS error while fetching data
	  Fetching data directly from POWER API causes CORS(Cross Origin Resource Sharing) error. This is error is resolved in our backend using the CORS module for flask
  - #### Calculation of the optimal tilt angle
	  One of the key features of "Solaris" is to provide the optimal tilt angle for solar panels. All the calculations for that are done in our backend.

### Dependencies
---
We have used a few modules to build up our backend REST API. They are listed below:
1. Python Flask
2. flask_cors from CORS
3. json module
4. requests module
5. math module
6. requests module
### Endpoints
---
There are basically 3 basic endpoints of this REST API 

1. ```/api/temporal/daily/optimum```
	This endpoint returns the estimated power output, optimal tilt angle, optimal power output etc. This is a part of our unique API which makes use of our exquisite algorithm to calculate the optimal tilt angle and returns it to the client
2.  ```/api/temporal/monthly/point/params``` 
	This endpoint return the monthly data of a certain location at a certain time. This actually fetches data from NASA POWER API and routes it back to the client
3. ```/api/temporal/daily/point```
	This endpoint deals with the daily data of a particular location at a particular day. The param list contains all the information about latitude, longitude, starting date, ending date, return type. This endpoint also fetches data from NASA POWER API and feeds it to the client
### Resources
---
* Solaris web app : [Solaris web homepage](https://solaris-bd.web.app/)
* Solaris web app repo : [Github repo for Solaris web app](https://github.com/SalmanSayeed79/Solaris-BD)
* Solaris Mobile app : [Apk drive link](https://drive.google.com/file/d/170HMrigXFpZwzHW3F4FIAJt-gC9HfU5Z/view?usp=sharing)
* Solaris Mobile app repo: [Github repo for solaris mobile app](https://github.com/zarifikram/SOLARIS)
* Solaris IOT module : [Github repo for Solaris IOT code](https://github.com/pptx704/solaris-servo-control)

### Reference
---
NASA POWER API Homepage : [NASA POWER API](https://power.larc.nasa.gov/)
Python Flask : [Flask Website](https://flask.palletsprojects.com/en/2.0.x/)
