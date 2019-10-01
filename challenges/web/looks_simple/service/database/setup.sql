-- CREATE DATABASE --
CREATE DATABASE looks_simple
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

-- amazing postgres... --
\c looks_simple

-- CREATE SCHEMA --
CREATE SCHEMA looks_simple
    AUTHORIZATION postgres;

-- POSTS TABLE --
CREATE TABLE looks_simple.posts
(
    id character varying(32) COLLATE pg_catalog."default" NOT NULL,
    title character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content character varying(100000) COLLATE pg_catalog."default" NOT NULL,
    date_posted timestamp with time zone NOT NULL,
    CONSTRAINT posts_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE looks_simple.posts
    OWNER to postgres;

-- USERS TABLE --
CREATE TABLE looks_simple.users
(
    username character varying(60) COLLATE pg_catalog."default" NOT NULL,
    description character varying(10000) COLLATE pg_catalog."default",
    password character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (username)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE looks_simple.users
    OWNER to postgres;

-- READ ONLY USER --
CREATE ROLE looks_simple_ro WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	NOINHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
    ENCRYPTED PASSWORD 'looks_simple';

GRANT USAGE ON SCHEMA "looks_simple" TO "looks_simple_ro";
GRANT SELECT ON ALL TABLES IN SCHEMA "looks_simple" TO "looks_simple_ro";

-- WRITE USER --
CREATE ROLE looks_simple_w WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	NOINHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
    ENCRYPTED PASSWORD 'looks_simple';

GRANT USAGE ON SCHEMA "looks_simple" TO "looks_simple_w";
GRANT SELECT, INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA "looks_simple" TO "looks_simple_w";

INSERT INTO looks_simple.users (username, password) VALUES
('admin', 'f52fbd32b2b3b86ff88ef6c490628285f482af15ddcb29541f94bcf526a3f6c7'),
('superadmin', 'f52fbd32b2b3b86ff88ef6c490628285f482af15ddcb29541f94bcf526a3f6c7');

UPDATE looks_simple.users SET description = 'GCTF{4M4Z1NG_SQ1_X55_W0T}' WHERE username = 'superadmin';