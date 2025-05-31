# AirBnB Clone - The Console

This is the first step towards building a full web application: the AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Console

The console is a command-line interface that allows you to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Storage

The storage system is an abstraction between "My object" and "How they are stored and persisted". This means:
- From your console code (the command interpreter itself) and from the front-end and RestAPI that you will write later, the storage system is abstracted
- This means you can change the type of storage easily without updating all of your codebase

The console will be a tool to validate this storage engine

## Web Static

This project also includes scripts for deploying web static content:
- `0-setup_web_static.sh`: Sets up web servers for deployment
- `1-pack_web_static.py`: Generates a .tgz archive from web_static folder
- `2-do_deploy_web_static.py`: Distributes an archive to web servers
- `3-deploy_web_static.py`: Creates and distributes an archive to web servers
- `100-clean_web_static.py`: Deletes out-of-date archives
- `101-setup_web_static.pp`: Puppet manifest for web static deployment

## Database Setup

The project includes SQL scripts for setting up development and test databases:
- `setup_mysql_dev.sql`: Sets up the development database
- `setup_mysql_test.sql`: Sets up the test database

## Usage

1. Clone the repository
2. Run the console:
```bash
./console.py
```

3. Use the console commands:
```bash
(hbnb) help
(hbnb) create User
(hbnb) show User <id>
(hbnb) all
(hbnb) quit
```

## Author

- GitHub: [Samkwizera](https://github.com/Samkwizera)
- Email: s.ihimbazwe@alustudent.com 