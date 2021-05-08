"""
    Just for start local!

    mkdir local_psql

    Boot psql: ./run_localpsql.sh

"""

from app import create_test_app

if __name__ == "__main__":
    app = create_test_app()
    app.run()