# Jekasoro
> Engage in beautiful conversations with like minded people.

## Description
Built with [Django](https://docs.djangoproject.com/en/6.0/) and [Reddit](https://reddit.com) at its core. Jekasoro **which means let's talk** is a community based space which exposes a set of REST API endpoints to enable users create communities or join communities they find interesting. The motivation behind this was to build something that models Reddit and decouples complexity bringing amazing functionality down to the very basic level. It is also to implement (actively) a lot of the things I learned working with [DRF](https://www.django-rest-framework.org/tutorial/quickstart/).

## Installation Guide
1. You need Python installed on your machine. You can find installation instructions [here](https://www.python.org/downloads/).
2. Next, you need to have a virtual environment running. Simply put, virtual environments act like containers for python projects. They help with dependency management. You should read more on them [here](https://docs.python.org/3/library/venv.html). I like to use *venv*
3. After activating a virtual enviroment, you need to set up your machine with the dependencies need for this project. They are found in the [requirements.txt](https://github.com/webForDave/Jekasoro/blob/main/requirements.txt) file. Install them with ```python -m pip install -r requirements.txt```
4. Now, go ahead and clone this repository or download it.
5. With that out of the way, you can go ahead to create the database tables with ```python manage.py migrate```
6. Finally, start the server with ```python manage.py runserver```

## Contributing
Contributions are highly welcomed as I look into adding a lot of functionalities like strict spam protection.