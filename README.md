# Fridge Manager


## Quick Start

See the [Configuration](#configuration) section for setting up the environment variables.

After setting up the environment variables, simply start the containers with docker compose:

```bash
docker compose up
```

## Configuration

Create a `.env` file in the root directory of the project with the following content:

```
DJANGO_SECRET_KEY=your_secret_key

DJANGO_ALLOWED_HOSTS=example.com localhost # Allowed hosts, in a space separated list

CSRF_TRUSTED_ORIGINS=https://example.com http://localhost8000 # Trusted origins for CSRF, in a space separated list

DJANGO_DEBUG=True

DJANGO_SUPERUSER_USERNAME=user
DJANGO_SUPERUSER_EMAIL=user@example.com
DJANGO_SUPERUSER_PASSWORD=password
```
