# Docker Example App: Color ⇢ Grayscale

This is a sample application that runs via multiple Docker containers, all of which are coordinated by Fig. If all goes correctly, the app should simply convert any color image into grayscale.

## Installation Steps

### 1. Install Docker

Docker instructions here for various operating systems: <https://docs.docker.com/installation/>

### 2. Install Fig

Fig installation instructions are located here: <http://www.fig.sh/install.html>

### 3. Clone this repository

### 4. Run `fig up` inside the directory containing the `fig.yml` file

The application runs on port 8000. If running on Linux, it should be available
at http://localhost:8000. If running on OS X, you'll need to access it via the
boot2docker IP address, which can be retrieved via `boot2docker ip`.

### 5. Migrate the db

Upon the initial run, the newly created DB won't be synced. You can sync it
using fig, with the command:

`fig run --rm web python manage.py migrate`

That will run a command inside the web container (which contains the Django
app, etc) and will migrate the db (which is in the postgres container, but it's
linked to the web container via Docker/Fig).

Just for reference the `--rm` flag means that the container will be destroyed
after it runs that command, which is what we want. Since this is a one-off
command, we don't need the container sticking around after it exits.
