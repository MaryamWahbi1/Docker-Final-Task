# Docker Final Task
![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2017/03/jenkins-docker-muscles.jpg?fit=1131%2C564&ssl=1)


## Explanation of the task

1. Create a Python Web APP (use either Flask or FastAPI libraries) that:
- Presents the Current BitCoin Price
- Stores the price in a Redis Database
- Presents the Average Price for the last 10 minutes
2. Dockerize the applications (Create Dockerfile and docker-compose.yml)

3. Create a Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub.

------------
## Prerequisites
You need to have Docker Engine and Docker Compose on your machine. You can either:

- Install Docker Engine and Docker Compose as standalone binaries.
- Install Docker Desktop which includes both Docker Engine and Docker Compose.

------------
## Run Locally

**1. Clone the project**
```shell
git clone https://github.com/MaryamWahbi1/Docker-Final-Task.git
```
**2. Go to the project directory:**
```shell
cd Docker-Final-Task
```
**3. Build**
```shell
docker compose up
```
![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_compose_up.PNG?raw=true)

**4. Enter http://localhost:8000/ in a browser to see the application running**
If this doesn’t resolve, you can also try http://127.0.0.1:8000.
![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/BitCoin_Price_HTML.PNG?raw=true)

------------
## DockerHub

**Run the image from DockerHub**

```shell
docker pull maryamwahbi/python-flask-ci
docker run -d -p 8080:8080 maryamwahbi/python-flask-ci:latest
```

![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/Dockerhub.PNG?raw=true)

------------
## Jenkins
**Create a Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub**

![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/pipline.PNG?raw=true)



