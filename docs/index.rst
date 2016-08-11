Welcome to pgoapi's documentation!
==================================

pgoapi is an unofficial Pokemon Go API library written in python. It
provides game authentication and usage of the ingame API over the
protocol description `POGOProtos
<https://github.com/AeonLucid/POGOProtos>`_ (protobuf).

Automatic & dynamic parsing of API requests/responses by finding the
correct protocol description is part of this library. The response
is returned in a python dictionary format, which can be easily
converted to JSON.

API Reference
-------------

For an overview about all possible calls, please have a look at
[[api_functions]] wiki page. All possible calls are documented
including the necessary input arguments.

History
-------

It came into being due to the efforts of the `/r/pokemongodev
<https://www.reddit.com/r/pokemongodev/>`_ community.

Welcome to the Pokemon Go Map wiki

Please don't submit bug reports about Pokémon not showing up, it's a
known issue. Pokemon Go Map is aiming to bring a live visualization
map of nearby Pokémon, Pokéstops and gyms in a form of a web-app as
well as native phone applications.

.. toctree::
   :maxdepth: 2

   installation
   usage
   types

Pokemon GO MAP
==============

Video Setup
-----------

| Video Walkthrough https://www.youtube.com/watch?v=RJKAulPCkRI
| German Amazon EC2 Tutorial https://www.youtube.com/watch?v=FxcVGrszl3I

Basic Installation
------------------

Prerequisites

Installation will require Python 2.7 and Pip. If you already have
these you can skip to installation. Python 3 is not supported at all.

Ubuntu or Debian
----------------

You can install the required packages on Ubuntu by running the
following command:

.. code-block:: console

   sudo apt-get install python python-pip python-dev nodejs nodejs-legacy npm

How to get it up & running (grunt included) on a fresh Ubuntu 16.04 VPS/VM. root is implied.
--------------------------------------------------------------------------------------------

.. code-block:: console

   apt install git nodejs npm python-pip nodejs-legacy python-dev
   git clone -b develop https://github.com/AHAAAAAAA/PokemonGo-Map.git
   cd PokemonGo-Map/
   pip install --upgrade pip
   pip install -r requirements.txt
   npm install
   npm install -g grunt-cli
   npm install node-sass
   grunt build

Red Hat or CentOs or Fedora
---------------------------

You can install the required packages on Red Hat by running the
following command:

You may also need to install the EPEL repository to install
python-pip and python-devel.

.. code-block:: console

   yum install epel-release
   yum install python python-pip nodejs npm python-devel

openSUSE
--------

You can install the required packages on openSUSE by running the
following command:

.. code-block:: console

   sudo zypper in python python-pip nodejs npm python-devel python-wsgiref

Arch
----

You can install the required packages on Arch Linux by running the
following command

.. code-block:: console

   sudo pacman -S python2 python2-pip nodejs npm

OS X (instructions with image `here
<https://jonaharagon.github.io/PoGoMapWiki/#!Macintosh-Installation-and-requirements.md>`_)

OS X comes with some outdated Python packages (these instructions
were tested on OS X El Capitan).

You will need to install pip and then upgrade a few python packages.

Instructions (run everything, each on its own line):

.. code-block:: console

   curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
   sudo python ./get-pip.py
   sudo -H easy_install --upgrade six
   sudo -H easy_install --upgrade setuptools
   sudo -H pip install -r requirements.txt

To install node and npm, download and install the installer from
https://nodejs.org/en/download/.

Windows (instructions with image `here
<https://jonaharagon.github.io/PoGoMapWiki/#!Windows-Installation-and-requirements.md>`_)

Download Git for Windows `here
<https://git-for-windows.github.io/>`_ and install it.

Download Python 2 (latest 2.7.12) `here
<https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi>`_
and install it. When installing check that the python location gets
appended to the PATH environment variable!

Then download `pip
<https://bootstrap.pypa.io/get-pip.py>`_ (right click that link and
choose "Save Link As"), and double click the file you downloaded,
assuming you installed Python correctly.

Download NodeJS (latest 6.3.1) `here
<https://nodejs.org/en/download/current>`_ and install.

Open a git bash on your PokemonGo-Map folder with mouse's right
click -> Git Bash Here

Launch

.. code-block:: console

   pip install -r requirements.txt
   npm install -g grunt
   npm install -g grunt-cli

(OPTIONAL) For more security fix, upgrade some packages with

.. code-block:: console

   npm install graceful-fs@4.1.5
   npm install minimatch@3.0.2

After that, launch

.. code-block:: console

   npm install

You are ready!

.. note:: There is a one-click setup for Windows. After you've
   installed Python, go into the Easy Setup folder and run setup.bat.
   This should install pip and the dependencies for you, and put your
   Google API key into the right place.

Installation Complete

Once installed, opening a terminal (cmd.exe prompt) and typing in
   python ./runserver.py --help should net you this output:

.. code-block:: console

   $ python ./runserver.py --help
   usage: runserver.py [-h] [-a AUTH_SERVICE] [-u USERNAME] [-p PASSWORD]
                       [-l LOCATION] [-st STEP_LIMIT] [-sd SCAN_DELAY]
                       [-ld LOGIN_DELAY] [-dc] [-H HOST] [-P PORT] [-L LOCALE]
                       [-c] [-d] [-m] [-ns] [-os] [-nsc] [-fl] -k GMAPS_KEY [-C]
                       [-D DB] [-cd] [-np] [-ng] [-nk] [--db-type DB_TYPE]
                       [--db-name DB_NAME] [--db-user DB_USER]
                       [--db-pass DB_PASS] [--db-host DB_HOST]
                       [--db-max_connections DB_MAX_CONNECTIONS]
                       [-wh [WEBHOOKS [WEBHOOKS ...]]]

   Args that start with '--' (eg. -a) can also be set in a config file
   (../config/config.ini).
   The recognized syntax for setting (key, value) pairs is based on the INI and
   YAML formats (e.g. key=value or foo=TRUE). For full documentation of the
   differences from the standards please refer to the ConfigArgParse
   documentation. If an arg is specified in more than one place, then commandline
   values override config file values which override defaults.

   optional arguments:
     -h, --help            show this help message and exit
     -a AUTH_SERVICE, --auth-service AUTH_SERVICE
                           Auth Services, either one for all accounts or one per
                           account. ptc or google. Defaults all to ptc.
     -u USERNAME, --username USERNAME
                           Usernames, one per account.
     -p PASSWORD, --password PASSWORD
                           Passwords, either single one for all accounts or one
                           per account.
     -l LOCATION, --location LOCATION
                       Location, can be an address or coordinates
     -st STEP_LIMIT, --step-limit STEP_LIMIT
                           Steps
     -sd SCAN_DELAY, --scan-delay SCAN_DELAY
                           Time delay between requests in scan threads default 10
     -ld LOGIN_DELAY, --login-delay LOGIN_DELAY
                           Time delay between each login attempt default is 5
     -dc, --display-in-console
                           Display Found Pokemon in Console
     -H HOST, --host HOST  Set web server listening host
     -P PORT, --port PORT  Set web server listening port
     -L LOCALE, --locale LOCALE
                           Locale for Pokemon names (default: en, check
                           static/dist/locales for more)
     -c, --china           Coordinates transformer for China
     -d, --debug           Debug Mode
     -m, --mock            Mock mode. Starts the web server but not the
                           background thread.
     -ns, --no-server      No-Server Mode. Starts the searcher but not the
                           Webserver.
     -os, --only-server    Server-Only Mode. Starts only the Webserver without
                           the searcher.
     -nsc, --no-search-control
                           Disables search control
     -fl, --fixed-location
                           Hides the search bar for use in shared maps.
     -k GMAPS_KEY, --gmaps-key GMAPS_KEY
                           Google Maps Javascript API Key
     -C, --cors            Enable CORS on web server
     -D DB, --db DB        Database filename
     -cd, --clear-db       Deletes the existing database before starting the
                           Webserver.
     -np, --no-pokemon     Disables Pokemon from the map (including parsing them
                           into local db)
     -ng, --no-gyms        Disables Gyms from the map (including parsing them
                           into local db)
     -nk, --no-pokestops   Disables PokeStops from the map (including parsing
                           them into local db)
     --db-type DB_TYPE     Type of database to be used (default: sqlite)
     --db-name DB_NAME     Name of the database to be used
     --db-user DB_USER     Username for the database
     --db-pass DB_PASS     Password for the database
     --db-host DB_HOST     IP or hostname for the database
     --db-max_connections DB_MAX_CONNECTIONS
                           Max connections for the database
     -wh [WEBHOOKS [WEBHOOKS ...]], --webhook [WEBHOOKS [WEBHOOKS ...]]
                       Define URL(s) to POST webhook information to

Credentials and Downloading
---------------------------

It is advised to create a separate
`Pokemon Club account (on their official website)
<https://club.pokemon.com/us/pokemon-trainer-club/sign-up/>`_ to be
used by the program to search for Pokemon. It's ill-advised to use
the same account as that you use for the app. If the page is
unavailable refresh the page every 5-10 minutes and it should allow
signups eventually. It's also possible to use a Google account, in
case of both services you can login without ever connecting to the
actual game.

Then, download one of the following branches below:

To be updated:

    Download master (Stable builds)
    Download dev branch (Active development)

The dev branch will have latest features from the development team,
however it may be unstable at some times.

Extract this zip file to any location.

Install Dependencies
--------------------

Now, open a Terminal/Command Line (Win+R and cmd on Windows) and cd
to the folder you extracted the zip file to.

.. code-block:: console

   cd some/directory/

In Windows you can also right click within the folder and select
"Open Command Window Here."

Then enter the following:

.. code-block:: console

   pip install -r requirements.txt
   npm install

.. note:: On openSUSE and possibly other Linux distributions you may
   have to run 'pip2' instead of 'pip' as 'pip' might run the
   incompatible Python 3 version of pip.

Google Maps API key
-------------------

You will need to generate your own Google Maps API key and place it
in your program directory to use this program. Here's a wiki entry on
how to do this part.

Running

To start the server, run the following command:

.. code-block:: console

   python runserver.py -u [USERNAME] -p [PASSWORD] -st 10 -k [Google Maps API key] -l "[LOCATION]"

or for Google account:

.. code-block:: console

   python runserver.py -a google -u [USERNAME] -p [PASSWORD] -st 10 -k [Google Maps API key] -l "[LOCATION]"

Replacing [USERNAME] and [PASSWORD] with the Pokemon Club credentials
you created previously, and [LOCATION] with any location, for example
Washington, D.C or latitude and longitude coordinates, such as
38.9072 77.0369.

Additionally, you can change the 10 after -st to any number. This
number indicates the number of steps away from your location it
should look, higher numbers being farther.

HowTo make Map accessible in Windows Host with VMWare Linux Guest
-----------------------------------------------------------------

Set VMWare network to "Bridged Mode"

Enter the following in Linux guest terminal:

.. code-block:: console

   sudo iptables -A INPUT -i eth0 -p tcp --dport 5000 -j ACCEPT
   sudo sysctl -w net.ipv4.conf.eth0.route_localnet=1
   sudo iptables -t nat -A PREROUTING -p tcp --dport 5000 -j DNAT --to-destination 127.0.0.1:5000

Accesss PokemonGo-Map in your host (Windows) Browser using the IP
address of your Linux guest: 192.168.0.X:5000

.. note:: You need to replace all occurrences of eth0 with the name
   of your network adapter for all commands used in VMWare guest
   (Linux). You can find out your network adapter name and IP address
   using the following command in Linux terminal:

.. code-block:: console

   ifconfig

Other Information
-----------------

Most effective input setups for finding pokemon:

For one account:

.. code-block:: console

   *"C:\Python27\python.exe" runserver.py -a ptc/google -u UserName -p Password -l "LOCATION" -st 6 -H 0.0.0.0 -L en -sd 10 -ld 1

For many accounts:

.. code-block:: console

   *"C:\Python27\python.exe" runserver.py -a ptc/google -u UserName -u Username2 -u Username2 -p Password1 -p Password2 -p Password3 -l "LOCATION" -st 6 -H 0.0.0.0 -L en -sd 10 -ld 1

| --increase -sd from 10? --Help? Maybe there should be a discussion?
| --Not really a discussion. The scan delay is ten seconds as
  determined by Niantic on August 3rd. Doing more will result in
  missed pokemon.

Project refactor
----------------

As of 2016-07-20, support for the first implementation 'example.py'
was dropped. Please use the refactored version present in the branch
develop. Periodic tagged releases will be made.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
