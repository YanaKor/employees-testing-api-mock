from dataclasses import dataclass
import os
from dotenv import load_dotenv
from support.custom_errors import CredsNotFoundError

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SCENARIOS_PATH = os.path.join(ROOT_PATH, "support", "scenarios.json")
ALL_EMPLOYEES_PATH = os.path.join(ROOT_PATH, "schemas", "all_employees_schema.json")
SINGLE_EMPLOYEES_PATH = os.path.join(ROOT_PATH, "schemas", "single_employee_schema.json")

@dataclass
class Endpoints:
    BASE_URL: str = 'https://employees-api-i9ae.onrender.com'
    TOKEN_URL: str = f'{BASE_URL}/generate-token'
    EMPLOYEES_URL: str = f'{BASE_URL}/employees'

@dataclass
class Credentials:
    load_dotenv()
    APP_USERNAME: str = os.getenv("APP_SUPERUSER")
    APP_PASSWORD: str = os.getenv("APP_PASSWORD")

    @classmethod
    def get_env_variables(cls):

        if not Credentials.APP_USERNAME or not Credentials.APP_PASSWORD:
            raise CredsNotFoundError

        return cls(Credentials.APP_USERNAME, Credentials.APP_PASSWORD)


