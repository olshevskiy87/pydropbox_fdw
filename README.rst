=============
pydropbox_fdw
=============

Dropbox foreign data wrapper for postgresql written in python.

************
dependencies
************

* `dropbox <https://pypi.python.org/pypi/dropbox>`__
* `multicorn <http://multicorn.org/#idinstallation>`__

************
installation
************

1. install python module

    ::

        $ git clone https://github.com/olshevskiy87/pydropbox_fdw
        $ cd pydropbox_fdw
        $ python setup.py install

2. create extension "multicorn"

    ::

        $$ create extension multicorn;

3. create foreign server in database

    ::

        $$ CREATE SERVER pydropbox_fdw
        FOREIGN DATA WRAPPER multicorn
        OPTIONS (
            wrapper 'pydropbox_fdw.PydropboxFDW'
        );

4. create foreign table

    ::

        $$ CREATE FOREIGN TABLE dropbox_test (
            path TEXT,
            bytes BIGINT,
            size TEXT,
            modified TIMESTAMP WITH TIME ZONE,
            is_dir BOOLEAN,
            mime_type TEXT,
            revision INT,
            root TEXT,
            is_deleted BOOLEAN
        ) SERVER pydropbox_fdw OPTIONS (
            token 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            path '/',  -- optional
            include_deleted 'y',  -- optional
            file_limit '10'  -- optional
        );

*****
usage
*****

* get all root files from dropbox application's directory

::

    $$ select path, size
           , to_char(modified, 'dd.mm.yyyy hh24:mi:ss') mod_dt, mime_type
       from dropbox_test
       where bytes > 0;

         path     |   size    |       mod_dt        |   mime_type
    --------------+-----------+---------------------+---------------
     /aac-320.m3u | 176 bytes | 31.08.2016 21:38:48 | audio/mpegurl
    (1 row)


**************
external links
**************

* `PostgreSQL foreign data wrappers <https://wiki.postgresql.org/wiki/Foreign_data_wrappers>`__
* `Multicorn <http://multicorn.org>`__ - postgres extension that allows to make FDW with python language
* `Dropbox <https://www.dropbox.com/>`__ - a file hosting service, that offers cloud storage

*******
license
*******

Copyright (c) 2016 Dmitriy Olshevskiy. MIT LICENSE.

See LICENSE.txt for details.
