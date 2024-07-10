import os


class AppEnv:
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")

    # Api rest services.
    QUERY_UNIT_MEASURE_BY_ID: str = (
        os.getenv("QUERY_UNIT_MEASURE_BY_ID",
                  "http://127.0.0.1:8000/unitmeasure/"))
    QUERY_DEPARTMENT_BY_ID: str = (
        os.getenv("QUERY_DEPARTMENT_BY_ID",
                  "http://127.0.0.1:8000/departments/"))
