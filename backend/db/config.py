# Defaults
DATABASE_PATH = ""
DATABASE_NAME = ""
USER_NAME = ""
USER_PASSWORD = ""
DATABASE_URL = (
    f"postgresql+psycopg2://{USER_NAME}:{USER_PASSWORD}@{DATABASE_PATH}/{DATABASE_NAME}"
)
