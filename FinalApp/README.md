# How to run FinalApp:

 - Install [Python 3.8](https://www.python.org/downloads/)
- Install [Docker](https://www.docker.com/)
- Open terminal
- Clone the [repository](https://github.com/kuzaster/python_training_2020/tree/main/FinalApp)
- Go to main directory of the project `/FinalApp`
- Create virtual environment and activate it
- Install packages from requirements `pip install -r requirements.txt`
- Before run an example container _"nginx-server"_ 
  build  a base image for it `sudo docker build -t="dockerfile/ubuntu" github.com/dockerfile/ubuntu`
 - Run `flask run` 
- Open up your web browser and enter (http://localhost:5000/) in the address field to see the working app
- You could _add, change or remove_ containers from a browser or _config-file.yaml_ in a directory of the project `/FinalApp/app`  