CREATE DATABASE "dbBorrowing" OWNER postgres;
\connect order
ALTER DATABASE "dbBorrowing" SET TIMEZONE TO 'Europe/Rome';
SET TIMEZONE TO 'Europe/Rome';

ALTER TABLE "borrowing"
    OWNER to postgres;