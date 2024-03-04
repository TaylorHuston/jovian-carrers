from sqlalchemy import create_engine, text

# Bad that this is in plain text, following along with tutorial though
db_connection_string = "mysql+pymysql://ehcazu8mvtvv4i44ghs3:pscale_pw_i960dmnsHwOCf3IWmKZi4AzOMVi1ZueGLYRiPZAy3i9@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ca": "/etc/ssl/certs/ca-certificates.crt"
                           }
                       })

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     print(type(result))
#     print(result)
#     result_all = result.all()
#     print(type(result_all))
#     print(result_all)
#     print(type(result_all[0]))
#     print(dict(result_all[0]))

#     result_all_dicts = [dict(row) for row in result_all]

#     print(result_all_dicts)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = [dict(row) for row in result.all()]
    return jobs
