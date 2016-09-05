drop database if exists pydropbox_test;
create database pydropbox_test;

\connect pydropbox_test

set client_min_messages to debug;

drop extension if exists multicorn cascade;
create extension multicorn;

CREATE SERVER pydropbox_fdw
FOREIGN DATA WRAPPER multicorn
OPTIONS (
    wrapper 'pydropbox_fdw.PydropboxFDW'
);

CREATE FOREIGN TABLE dropbox_test (
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
    token 'xxxxxxxxxxxxxxxxxxxxxxxx',
    path '/',
    include_deleted 'y',
    file_limit '3'
);

select * from dropbox_test;
