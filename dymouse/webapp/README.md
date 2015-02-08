# Dymo USB Scale

This is a webapp for interfacing with the 
Dymo USB scale using a Raspberry Pi.

You can run this module from anywhere,
all you need is to install Flask.
Then you can drop the following into 
a script:

```
from dymousbscale import *

# run debug
app.run(debug=True)

# run on port XYZ
app.run(port="8000")

# run visible to outside world
app.run(host="0.0.0.0")
```

Now you can visit the app at (if you run
with no arguments):

```
localhost:5000/scale
```

## api scale

Defines a REST API for the scale, by defining Flask routes.

## pages scale

Defines Flask routes leading to pages.

## blueprint scale

Defines a Flask blueprint for creating a URL prefix for 
the REST API.


