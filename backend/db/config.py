DATABASE_PATH = "0.0.0.0:5432"
DATABASE_NAME = "postgres"
USER_NAME = "myuser"
USER_PASSWORD = "mypassword"
DATABASE_URL = (
    f"postgresql+psycopg2://{USER_NAME}:{USER_PASSWORD}@{DATABASE_PATH}/{DATABASE_NAME}"
)
