# Flask-MySQL Docker Template

This project can be used to run a basic flask(CRUD API) app with MySQL as DB using docker-compose.

## Getting Started

### Prerequisites

**1. Git**

Please follow the below link for official documentation from Git to install latest version of git on your os. (For code cloning only)

```https://git-scm.com/downloads```

**2. Docker**

Please follow the below link for official documentation from Docker to install latest version of docker on your os.

```https://docs.docker.com/desktop/```

### Installing

**Step 1:** Clone the project into your local machine using below command.

```git clone https://github.com/fbasturk/addressBookApi.git```

**Step 2:** Change to the directory where the project was cloned in previous step.

```
cd addressBookApi
```

**Step 3:** Run

```
docker-compose up
```

**Step 4:** Open up the browser and paste the below url

```
http://localhost:5000/
```

The browser should display ```Connection Address Book API``` message.

### Note

**API Documetation** Open up the browser and paste the below url for API documentation

```
http://localhost:5000/swagger/
```

**Database Connection**

Use any of the database clients like MySQL workbench for SQL Developer.

Connect to MySQL database using the properties specified in ```docker-compose.yml``` file with host as ```localhost```.

The port to be used is ```3307``` which is the port on which app is running on localhost. Don't use ```3306``` as port to connect from the client as it's the port where container is running.
