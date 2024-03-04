from sqlalchemy import create_engine, text
import os

def load_jobs():
    DB_CONNECTION_STR = os.environ.get('DB_CONNECTION_STR')

    db_connection_string = DB_CONNECTION_STR

    engine = create_engine(db_connection_string,
                        connect_args={
                            "ssl": {
                                "ca": "/etc/ssl/certs/ca-certificates.crt"
                            }
                        })

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = [dict(row) for row in result.all()]
    return jobs
