# Thesis project

## Server

How to:

- **Create project.env**

   For example:

    ```sh
    export GUNICORN_INSTANCE=app:create_app() # constant for prod app
    export POSTGRES_USER=prod_user
    export POSTGRES_PASSWORD=super_prod_pass
    export POSTGRES_DB=prod_db
    ```

- **Manage docker**

    ```sh
    ./compose_run.sh prod # boot on 0.0.0.0
    ```

    ```sh
    ./compose_restart.sh # restart with previus .env
    ```

    ```sh
    ./compose_stop.sh # stop with save volumes
    ```


## Local

How to:

- **Use your psql or boot docker container:**

    ```sh
        cd /backend/app
        ./run_localpsql.sh # boot psql container 
        # with enviroment in localpsql.env
        # for stop use 'docker stop localpsql'
    ```
    
- **Boot app:**

    ```sh
        python3 -m venv venv/
        source venv/bin/activate
        pip install -r requirements.txt
        python run.py # check on 127.0.0.1:5000
    ```