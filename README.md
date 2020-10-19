# Launch Project

This test was done using Python3.8 and so you should run this test using at least this version of Python.

### Install dependencies

You should use a virtualenv to run the project.
It exists several solution for this, I personnaly use [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)

```sh
pip install -r requirements.txt
```

### Run the Project

```sh
uvicorn sennder.asgi:application
```

and go to [localhost:8000/movies](http://localhost:8000/movies)

### Run the tests

```sh
DJANGO_SETTINGS_MODULE=sennder.settings pytest
```

## Architecture Choices

### Why Django ?

I use Django as a web server even if it's a heavy tool because I've been told that's what is used in the company.

### Why return a JSON instead of a template ?

Since I use asyncio and async views on django, rendering some template is not as simple as synchronous views. To keep it stupid, simple (KISS), I decide to return a JSON object.
It is a modular approach. A frontend app can display the data as it whishes.
It exists some solutions for render template on async views such as [aiohttp_jinja_2](https://aiohttp-jinja2.readthedocs.io/en/stable/) which works for aiohttp webserver.

### Caching API call

There are multiples way to handle the problem. My decision was to go for the simplest solution which can be easily change.
I use asyncio and aiocache to cache the function doing the API call.

### Testing

Tests are simple. On the view endpoint, I did not test the payload because each change on the ghibli API call could make our build fail.
Also I used some dependencies injections to have some predictable tests for the `movies.fetch_data` module.
Tests can be improve to have more cases and edges cases and provide a useful documentation for future developers.

### Documentation

Documentation is a useful but also dangerous tool. Often not update, I generaly use my tests as documentation as they are always up-to-date
