=====
Usage
=====

Getting Started
===============

Login
-----

Before any API requests can be executed, it is necessary to set a
position and then to login. The coordinates are latitude, longitude
and altitude. For the login, it is possible to use "google" so your
google account or "ptc" (Pokemon Trainer Club).

.. code-block:: python

   api = pgoapi.PGoApi()
   api.set_position(40.7127837, -74.005941, 0.0)
   api.login('ptc', 'your_username', 'your_secure_password')

api.login will of course return True or False.

Execute API function
--------------------

After a successful login, API calls can be made. There are two ways
to do this.

Simple
``````

The first one is very simple and can be executed directly over the
api object:

.. code-block:: python

   ...
   response = api.get_player()

Advanced
````````
A more complex way which is thread-safe and supports chaining (more
than one subrequest in a API call) has to be done over a separate
request object, which can be created over api.create_request():

.. code-block:: python

   ...
   req = api.create_request()
   req.get_player()
   req.get_inventory()
   response = req.call()

Output
------

The output is currently just a dictionary which can be easily
dumped/printed:

.. code-block:: python

   ...
   import pprint
   print('Response dictionary:\n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(response)))

Argument mapping
----------------

Different API calls to the Pokemon Go server require certain
arguments, like which Pokemon you want to release. In the API
reference, all calls are described with the possible input arguments.

.. code-block:: python

   ...
   api.release_pokemon(pokemon_id=<your pokemonid>)

If there are more complex types, like repeated fields and subtypes
(which have further arguments) they can be specified by lists and
dictionaries.

Repeated fields
```````````````

.. code-block:: python

   ...
   api.get_map_objects(
       latitude=lat,
       longitude=lng,
       since_timestamp_ms=[0, 0, 0, 0],
       cell_id=[<cell_id_1>, <cell_id_2>, <cell_id_3>, <cell_id_4>]
   )

Sub Types
`````````

.. code-block:: python

   ...
   api.set_avatar(
       player_avatar={
           'skin': '<your_input>',
           ...
       }
   )

pokecli.py
==========

pokecli.py is a small pgoapi example script which shows the generic
usage of pgoapi with few RPC calls.

.. code-block:: console

   usage: pokecli.py [-h] -a AUTH_SERVICE -u USERNAME -p PASSWORD -l LOCATION [-d] [-t]

   optional arguments:
     -h, --help                                    show this help message and exit
     -a AUTH_SERVICE, --auth_service AUTH_SERVICE  Auth Service ('ptc' or 'google')
     -u USERNAME, --username USERNAME              Username
     -p PASSWORD, --password PASSWORD              Password
     -l LOCATION, --location LOCATION              Location
     -d, --debug                                   Debug Mode
     -t, --test                                    Only parse the specified location


pokecli with Docker (optional)
------------------------------

Build and run container:

.. code-block:: console

   docker build -t pokecli .
   docker run pokecli

Optionally create an alias:

.. code-block:: console

   alias pokecli='docker run pokecli'
