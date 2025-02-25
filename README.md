# ms-flask-python
This is a simple microservice that allow to connect to other docker with a database microsof sql server 2019 and execute a query on a system table.
This is common use case for figure out how to works a database and the stack of python called Flask but the concepts here are pretty common and useful.
![image](https://github.com/user-attachments/assets/d8a6767f-4072-4f58-95e4-f2b74fb26510)

## Step 1 - Clone
To clone this repository git in your local filesystem

## Step 2 - Start up the docker microsoft database
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=SetYourPassword01-' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest

## Step 3 - Compile the microservice
### Note. Review the file called app.py and set IP address of the host where is running the docker previous with the db
docker build --no-cache -t flask-api .

## Step 4 - Start up the microservice docker
docker run -p 5000:5000 --name flask-api-test -d flask-api

## Step 5 - Check if both docker microservice and db are running OK
docker ps
### Your must see something similar to this
![image](https://github.com/user-attachments/assets/f43ecbad-2b16-45cc-93d2-9de41916ca02)

## Step 6 - Test the microservice
curl -v http://localhost:5000/data
### Your must see something similar to this
![image](https://github.com/user-attachments/assets/727efb90-4ca9-47ed-b002-a9358e9d10a1)


