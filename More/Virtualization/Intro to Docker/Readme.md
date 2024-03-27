# Docker
Docker is an open-source platform that allows you to automate the deployment of applications inside software containers. These containers are lightweight and contain everything needed to run the application, including the code, runtime, libraries, and dependencies. Docker containers are isolated from each other and from the host system, providing a secure and consistent environment for running applications.

# Basic Docker Syntax
The syntax for Docker can be categorised into four main groups:
* Running a container
* Managing & Inspecting containers
* Managing Docker images
* Docker daemon stats and information

## Managing Docker Images
### Pulling an Image
To pull an image from the Docker Hub, use the following command:
```bash
$ docker pull <image_name>
```
For example, to pull the Ubuntu image, use the following command:
```bash
$ docker pull ubuntu # For latest version
$ docker pull ubuntu:20.04 # For a specific version
```

### Docker Image
The docker image command, with the appropriate option, allows us to manage the images on our local system. To list the available options, we can simply do docker image to see what we can do.

```bash
$ docker image 
Manage images

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.
```

#### Docker Image ls
The docker image `ls` command lists all the images on the local system.

```bash
$ docker image ls

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              20.04               9140108b62dc        2 weeks ago         73.9MB
ubuntu              latest              9140108b62dc        2 weeks ago         73.9MB
```

#### Docker Image rm
The docker image `rm` command removes one or more images from the local system.

```bash
$ docker image rm ubuntu:22.04
Untagged: ubuntu:22.04
Untagged: ubuntu@sha256:20fa2d7bb4de7723f542be5923b06c4d704370f0390e4ae9e1c833c8785644c1
Deleted: sha256:2dc39ba059dcd42ade30aae30147b5692777ba9ff0779a62ad93a74de02e3e1f
Deleted: sha256:7f5cbd8cc787c8d628630756bcc7240e6c96b876c2882e6fc980a8b60cdfa274
```

#### Docker Image prune
The docker image `prune` command removes all the dangling images from the local system.

```bash
$ docker image prune

WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:2dc39ba059dcd42ade30aae30147b5692777ba9ff0779a62ad93a74de02e3e1f
deleted: sha256:7f5cbd8cc787c8d628630756bcc7240e6c96b876c2882e6fc980a8b60cdfa274
Total reclaimed space: 73.9MB
```

#### Docker Image pull
The docker image `pull` command pulls an image from the Docker Hub.

```bash
$ docker image pull ubuntu:22.04
22.04: Pulling from library/ubuntu
Digest: sha256:20fa2d7bb4de7723f542be5923b06c4d704370f0390e4ae9e1c833c8785644c1
Status: Image is up to date for ubuntu:22.04
docker.io/library/ubuntu:22.04
```

#### Docker Image build
The docker image `build` command builds an image from a Dockerfile.

```bash
$ docker image build -t myimage:1.0 . # Build an image from the current directory

Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu:20.04
 ---> 9140108b62dc
Step 2/2 : RUN apt-get update   
    ---> Using cache
    ---> 9140108b62dc
Successfully built 9140108b62dc
Successfully tagged myimage:1.0
```

# Running a Container
The Docker run command creates running containers from images. This is where commands from the Dockerfile (as well as our own input at runtime) are run.

The command works in the following way: `docker run [OPTIONS] IMAGE_NAME [COMMAND] [ARGUMENTS...]` the options enclosed in brackets are not required for a container to run.

**Example: Lets create an image named `myimage`, and make it interactive and spawn a shell within the container.**
```bash
$ docker run -it myimage /bin/bash
```

You can list all the running containers using the `docker ps` command.

```bash
$ docker ps
```
Adding a `-a` flag to the `docker ps` command will list all the containers, including the ones that are not running.


## Table of usefull options
| Option | Description | Dockerfile Instruction | Example |
|---|---|---|---|
| -d | Run the container in the background | N/A | `docker run -d myimage` |
| -it | Run the container in interactive mode | N/A | `docker run -it myimage /bin/bash` |
| -v | Bind a volume to the container | VOLUME | `docker run -v /host:/container myimage` |
| -p | Publish a container's port to the host | EXPOSE | `docker run -p 8080:80 myimage` |
| --rm | Automatically remove the container when it exits | N/A | `docker run --rm myimage` |
| --name | Assign a name to the container | N/A | `docker run --name mycontainer myimage` |
| --network | Connect the container to a network | N/A | `docker run --network mynetwork myimage` |
| --env | Set an environment variable in the container | ENV | `docker run --env MYVAR=myvalue myimage` |

# Dockerfiles
Dockerfiles are text files that contain a series of instructions that are used to build Docker images. The Dockerfile is used to automate the process of creating a Docker image.

## Dockerfile Instructions
The Dockerfile instructions are used to build a Docker image. The following in the table are some of the most commonly used Dockerfile instructions

| Instruction | Description | Example |
|---|---|---|
| FROM | Specifies the base image | `FROM ubuntu:20.04` |
| RUN | Executes a command in the container | `RUN apt-get update` |
| CMD | Specifies the command to run when the container starts | `CMD ["echo", "Hello World"]` |
| COPY | Copies files from the host to the container | `COPY app.py /app.py` |
| ADD | Copies files from the host to the container | `ADD app.py /app.py` |
| WORKDIR | Sets the working directory for the container | `WORKDIR /app` |
| EXPOSE | Exposes a port in the container | `EXPOSE 80` |
| ENV | Sets an environment variable in the container | `ENV MYVAR=myvalue` |
| VOLUME | Creates a mount point in the container | `VOLUME /data` |

## Dockerfile Example
```Dockerfile
# Use the official Ubuntu 20.04 image
FROM ubuntu:20.04

# Update the package list
RUN apt-get update

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Copy the app.py file to the container
COPY app.py /app.py

# Set the working directory
WORKDIR /app

# Expose port 80
EXPOSE 80

# Run the app.py file
CMD ["python3", "app.py"]
```

## Building a Docker Image
To build a Docker image from a Dockerfile, use the `docker build` command.

```bash
$ docker build -t myimage .
```

* `-t` flag is used to tag the image with a name and a version number.
* `.` specifies the location of the Dockerfile.

### Webserver Example
```Dockerfile
# Use the official Nginx image
FROM nginx:latest

# Copy the index.html file to the container
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]
```

Then build and run the image using the following commands:
```bash
$ docker build -t mywebserver . # Build the image
$ docker run -d -p 80:80 mywebserver # Run the container and expose port 80
```

Now you can access the webserver by navigating to `http://localhost:80` in your web browser.

### Optimizing Dockerfile
When building a Docker image, it is important to optimize the Dockerfile to reduce the image size and improve performance. Here are some tips to optimize a Dockerfile:

* Only installing the essential packages
* Removing cached files (such as APT cache or documentation installed with tools).
* Using minimal base operating systems in our FROM instruction. Even though operating systems for containers such as Ubuntu are already pretty slim, consider using an even more stripped-down version (i.e. ubuntu:22.04-minimal). Or, for example, using Alpine (which can be as small as 5.59MB!).
* Minimising the number of layers 
  * Each instruction in a Dockerfile creates a new layer in the image. The more layers there are, the larger the image size. To reduce the number of layers, combine multiple instructions into a single RUN instruction.

So instead of this:
```Dockerfile
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install apache2 -y
RUN apt-get install net-tools -y
```

Do this:
```Dockerfile
FROM ubuntu:latest
RUN apt-get update -y && apt-get upgrade -y && apt-get install apache2 -y && apt-get install net-tools
```

Note here how there are now only two build steps (this will be two layers, making the build much quicker).

# Docker Compose
Docker Compose is a tool that allows you to define and run multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

Often, applications require additional services to run, which we cannot do in a single container. For example, modern  and dynamic websites use services such as databases and a web server.

While we can spin up multiple containers or “microservices” individually and connect them, doing so one by one is cumbersome and inefficient. Docker Compose allows us to create these “microservices” as one singular “service”. 

Docker compose does not come pre-installed with Docker. To install Docker Compose, follow the instructions on the [official Docker documentation](https://docs.docker.com/compose/install/).

## Docker Compose Commands
The following are some of the most commonly used Docker Compose commands:

| Command | Description | Example |
|---|---|---|
| up | Create and start containers | `docker-compose up` |
| start | Start containers (requires built containers) | `docker-compose start` |
| down | Stop and remove containers | `docker-compose down` |
| stop | Stop containers without deletion | `docker-compose stop` |
| ps | List containers | `docker-compose ps` |
| logs | View container logs | `docker-compose logs` |
| exec | Run a command in a running container | `docker-compose exec webserver ls` |
| build | Build or rebuild services | `docker-compose build` |

## Docker Compose Example
The following is an example of a Docker Compose file that defines a web server and a database service:

```yaml
version: '3'

services:
  webserver:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - database
    networks:
      - mynetwork

  database:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: mydatabase
    networks:
      - mynetwork
networks:
    mynetwork:
```

In this example, we have defined two services: `webserver` and `database`. The `webserver` service uses the `nginx:latest` image, exposes port 80, mounts the `./html` directory to `/usr/share/nginx/html`, and depends on the `database` service. The `database` service uses the `mysql:latest` image, sets the root password to `password`, and creates a database named `mydatabase`. Lastly, we have defined a network named `mynetwork`.

## Docker-compose.yml files 101
The formatting of a docker-compose.yml file is different to that of a Dockerfile. It is important to note that YAML requires indentation (a good practice is two spaces which must be consistent!). Let's break down the structure of a docker-compose.yml file.

| Key | Description | Example |
|---|---|---|
| version | The version of the Compose file format | `version: '3'` |
| services | Defines the services that make up the application | `services:` |
| name | The name of the service | `webserver` 
| build | Specifies the build context for the service | `./webserver` |
| ports | Specifies the ports that the service exposes | `'80:80'`
| volumes | Defines the volumes that the services use | `./html:/usr/share/nginx/html` |
| networks | Defines the networks that the services are connected to | `mynetwork` |
| environment | Defines the environment variables for the service | `MYSQL_ROOT_PASSWORD: password` |




# Docker Socket
The Docker socket is a Unix socket that allows the Docker daemon to communicate with the Docker client. The Docker client sends commands to the Docker daemon using the Docker socket. The Docker socket is located at `/var/run/docker.sock` on the host system.

When you install Docker, there are two programs that get installed:

1. The Docker Client
2. The Docker Server

Docker works in a client/server model. Specifically, these two programs communicate with each other to form the Docker that we know and love. Docker achieves this communication using something called a socket. Sockets are an essential feature of the operating system that allows data to be communicated. 

For example, when using a chat program, there could be two sockets:
1. A socket for storing a message that you are sending
2. A socket for storing a message that someone is sending you.

The program will interact with these two sockets to store or retrieve the data within them! A socket can either be a network connection or what is represented as a file. What's important to know about sockets is that they allow for Interprocess Communication (IPC). This simply means that processes on an operating system can communicate with each other!

In the context of Docker, the Docker Server is effectively just an API. The Docker Server uses this API to listen for requests, whereas the Docker Client uses the API to send requests.

## Example
For example, when you run the command `docker run hello-world`, the Docker Client sends a request to the Docker Server to run the `hello-world` container. The Docker Server then runs the container and sends the output back to the Docker Client.

> It's important to note that because of this, the host machine running Docker can be configured to process commands sent from another device. This is an extremely dangerous vulnerability if it is not correctly configured because it means someone can remotely stop, start, and access Docker containers.