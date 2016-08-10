pgoapi - a pokemon go api lib in python
=======================================

pgoapi is a client/api/demo for Pokemon Go by tejado_.

It allows automatic parsing of requests/responses by finding the
correct protobuf objects over a naming convention and will return
the response in a parsed python dictionary format.

- This is unofficial - USE AT YOUR OWN RISK !
- I don't play pokemon go !
- No bot/farming code included !

.. image:: https://img.shields.io/travis/tejado/pgoapi/master.svg
   :target: https://travis-ci.org/tejado/pgoapi
   :alt: Build Status

Feature Support
---------------
- Python 2 and 3
- Google/PTC auth
- Address parsing for GPS coordinates
- Allows chaining of RPC calls
- Re-auth if ticket expired
- Check for server side-throttling
- Thread-safety
- Advanced logging/debugging
- Uses `POGOProtos
  <https://github.com/AeonLucid/POGOProtos>`_
- Mostly all available RPC calls (see `API reference`_ on the wiki)

Documentation
-------------

Documentation is available at the github `pgoapi wiki`_.

Requirements
------------

- Python 2 or 3
- requests
- protobuf (>=3)
- gpsoauth
- geopy (only for pokecli demo)
- s2sphere (only for pokecli demo)

Contribution
------------

| Contributions are highly welcome. Please use github or
  `pgoapi.slack.com
  <https://pgoapi.slack.com/>`_ for it!
| Join pgoapi.slack.com `here
  <https://pgoapislack.herokuapp.com/>`_!

Credits
-------

| Mila432_ for the login secrets
| elliottcarlson_ for the Google Auth PR
| AeonLucid_ for improved protos
| AHAAAAAAA_ for parts of the s2sphere stuff
| mikeres0_ for the slack channel including auto signup
| DeirhX_ for thread-safety

Ports
-----

| `Node Port
  <https://github.com/Armax/Pokemon-GO-node-api>`_ by Arm4x
| `Node Port - pogobuf
  <https://github.com/cyraxx/pogobuf>`_ by cyraxx

.. image:: https://ga-beacon.appspot.com/UA-1911411-4/pgoapi.git/README.md?pixel&useReferer
   :target: https://github.com/igrigorik/ga-beacon
   :alt: Analytics

.. _`API reference`: https://github.com/tejado/pgoapi/wiki/api_functions
.. _`pgoapi wiki`: https://github.com/tejado/pgoapi/wiki
.. _tejado: https://github.com/tejado
.. _Mila432: https://github.com/Mila432/Pokemon_Go_API
.. _elliottcarlson: https://github.com/elliottcarlson
.. _AeonLucid: https://github.com/AeonLucid/POGOProtos
.. _AHAAAAAAA: https://github.com/AHAAAAAAA/PokemonGo-Map
.. _mikeres0: https://github.com/mikeres0
.. _DeirhX: https://github.com/DeirhX
