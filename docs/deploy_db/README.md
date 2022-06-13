# Deploy Postgresql from Docker Hub

## Pull Postgresql Images
```bash=
$ docker pull postgres
```

## Start a postgres instance
- launch command
```bash=
$ docker run --name sql-inject-postgres -e POSTGRES_PASSWORD=ntcuser2222 -p 5432:5432 -d postgres
```

- container check
```
$ docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
926c2b1b065a   postgres   "docker-entrypoint.s…"   20 seconds ago   Up 19 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   sql-inject-postgres
```

- port  check
```
$ sudo netstat -ntlp | grep 5432
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      888201/docker-proxy 
tcp6       0      0 :::5432                 :::*                    LISTEN      888209/docker-proxy 
```

## Run Ppstgresql
- h : host
- U : username

```bash=
$ docker run -it --network host postgres psql -h localhost -U postgres
```

- login
```
$ docker run -it --network host postgres psql -h localhost -U postgres
Password for user postgres: 
psql (14.3 (Debian 14.3-1.pgdg110+1))
Type "help" for help.

postgres=# 
```

## Create Tables
```
CREATE TABLE users (
    username varchar(30),
    admin boolean
);
```

- output
```
Password for user postgres: 
psql (14.3 (Debian 14.3-1.pgdg110+1))
Type "help" for help.

postgres=# CREATE TABLE users (
    username varchar(30),
    admin boolean
);
CREATE TABLE
```


## Input user data
```
INSERT INTO users
    (username, admin)
VALUES
    ('john', true),
    ('mary', false);
INSERT 0 2
```

- output
```
postgres=# INSERT INTO users
    (username, admin)
VALUES
    ('john', true),
    ('mary', false);
INSERT 0 2
INSERT 0 2
```

## Check data
```
SELECT * FROM users;
```

- output
```
postgres=# SELECT * FROM users;
 username | admin 
----------+-------
 john     | t
 mary     | f
(2 rows)

```

