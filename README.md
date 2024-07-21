# Algorithm Practice

## How to debug

``` bash
$ docker compose build
$ docker compose up -d
$ docker compose down
```

``` bash
$ docker exec -it algorithms bash
```

``` bash
# Run following command and debug using Python Debugger in vscode
$ poetry run python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client xxxx.py
```
