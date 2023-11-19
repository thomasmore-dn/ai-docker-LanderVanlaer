[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ntg-lIM7)

# Cloud for AI

## Assignment 1 - Docker

In this exercise, you will create 2 Docker containers. The first one will train your AI model. The second one will host
an application using your model. You can use an existing training model from the internet (document the source of your
example) or you can use a model that you created yourself in another course.

Use a Git repository in which you commit your code and add a Readme file that gives some information on how to use your
code.
Deadline for this assignment is 6 December 2021

---

**Note** that you can detach the terminal from the container by adding the `-d` flag to the `docker-compose up` command.

You can train and run the model using the following command:

```shell
docker-compose up
```

When you want to retrain the model, you can use the following command:

```shell
docker-compose up --build train
```

When you want to run the application, you can use the following command:

```shell
docker-compose up --build server
```

You can test the server using the following command: _make sure the server is running_

```shell
python test.py
```