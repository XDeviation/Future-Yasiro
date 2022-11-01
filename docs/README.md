# Future Yasiro

Future Yasiro development documentation

## Environment

At first, you should run ```src/scripts/install_env.sh``` to install all package
### PostgreSQL

Future Yasiro use PostgreSQL to manage all data, so you should install PostgreSQL first.

In this document, we use PostgreSQL **version 15.0**, maybe lower versions will work.

All steps marked with **(recommand)** can be skipped if you know what you are doing.

All steps are recommended for those using psql for the first time


1. **(recommand)** create a new role
    ```bash
    sudo -i -u postgres
    psql
    ```
    then you will into psql cli, create db and user
    ```psql
    CREATE USER <user_name> WITH PASSWORD '<passwd>';
    CREATE DATABASE <database_name> OWNER <user_name>;
    GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <user_name>;
    \q
    ```
    
2. make psql connectable

    try:
    ```bash
    psql -U <user_name> -d <database_name> -h <database_host>
    ```
    If you can't connect to psql, see [this](https://stackoverflow.com/questions/69676009/psql-error-connection-to-server-on-socket-var-run-postgresql-s-pgsql-5432) answer, remember we use version 15 but not 14, so you should choice correct path
