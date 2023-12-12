# Mastering Docker: From MySQL to Flask – A Simplified Journey to Installation, Containerization, and Building a To-Do List App!"

1.Create EC2 Instance (if not done)

In my previous blog, I have already covered the steps for creating an EC2 instance. Please follow the provided instructions for a smooth and successful implementation.

https://hashnode.com/post/clnumbs4u000208ifg51u1xm4

Once an EC2 instance is successfully created in AWS following the above

steps.

2.Connect to Instance Using SSH

Run

ssh -i instance.pem ubuntu@<IP_ADDRESS>

3.Update Package ,and Install Docker

$sudo apt update

$sudo apt install docker.io

4.Create a new directory ,and check docker process status

$ mkdir docker_project

$ docker ps

5.Add user into docker group

Check user group ,run below cmmand

$ sudo cat /etc/group

Add user into docker group,and check user group

$ sudo usermod -aG docker $USER

6.Restart docker or Reboot

$sudo systemctl restart docker

Still if you are facing permission denied issue ,then Reboot the instance

$sudo reboot

Now you need to check docker process status,and permission denied issue is resolved.

$docker ps

7.Pull mysql docker image from Docker Hub

$docker pull mysql:latest

8.Check Downloaded mysql image

$docker image ls

9.Run Mysql Docker image

$docker run mysql:latest

10.Set Environment Variable to Create Container

$docker run -d -e MYSQL_ROOT_PASSWORD=test@123 mysql:latest

11.Check Container Status for mysql

$docker ps

Now your mysql container up and running

12.Execute mysql container ,and Access Mysql container

$docker exec -it 228b5561becb sh

Access mysql database

sh-4.4#mysql -u root -p

Enter Password:test@123

mysql>show databases

13.Exit from mysql ,and shell

mysql>exist

sh-4.4#exit

Building a Flask To-Do List App with Docker and Deploying on AWS 🚀

Introduction

In this guide, I'll take you through the exciting journey of creating a small Flask app project — a "To-Do List" application. The best part? We'll containerize it using Docker and deploy it on AWS. Let's dive in! 📝

Setting Up the Project Structure 📁

📁 Create a folder for your project and set up the following structure:

1.Create a Project Folder:

Execute the following command to create a new folder for your project:

$mkdir flask-app

2.Main Application Script (app.py):

Create the app.py file in the flask-app folder and add the necessary content. This script will be the heart of our Flask application.

3.HTML Template (templates/index.html):

Create the templates folder and within it, create the index.html file. This HTML template will be the main page template for our app.

$mkdir templates

4.CSS Stylesheet (static/style.css):

Similarly, create the static folder and within it, create the style.css file. This CSS stylesheet will provide styles for our application.

Dockerizing the Flask App 🐳

Create Dockerfile:

Create a Dockerfile in the flask-app folder with the required configurations. This file will guide Docker in building the container for our app.

Requirements.txt:

Create a requirements.txt file with the necessary Python dependencies for your Flask app.

Building and Running the Docker Container 🏗️

1.Build the Docker Container:

Open a terminal, navigate to the project folder (flask-app), and run the following command to build the Docker image:

$docker build -t flask-app .

2.Run the Docker Container:

Start the Docker container by running:

$docker run -p 5000:5000 flask-app

Adjusting Inbound Rules on AWS 🌐

Adjust EC2 Security Group:

Don't forget to adjust the inbound rules in your EC2's security group to allow traffic on port 5000, ensuring that our app can be accessed.

Congratulations! 🎉

1.Access Your To-Do List App on AWS:

Copy your instance's public IP and access the app using that IP and port 5000.

Copy your instance public ip ,and port 5000

Congratulations! You've successfully deployed your To-Do List application using Docker on AWS. This step-by-step guide ensures a smooth journey from project setup to deployment. Happy coding! 🚀🔧

If you found value in this post, I sincerely appreciate your time and attention. Your support means the world to us! To further express your encouragement and appreciation:

Follow for More Insights:

Consider clicking the "Follow" button to stay updated on our latest posts. Join our community and be part of the ongoing conversation.

Like and Share:

Show your support by hitting the "Like" button. Sharing is caring – spread the knowledge and insights with your network.

Your engagement is a powerful motivator for us to continue sharing valuable content. Thank you for being a part of our community and investing your time in learning and growing.

Best Regards,

Sprasad 🌐
