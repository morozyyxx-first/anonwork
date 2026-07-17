from typing import List
from pydantic import BaseModel

class ItemSchema(BaseModel):
    title: str
    name_of_company: str
    salary: str
    location: str
    contacts: str
    job_time: str
    description: str
    skills: List[str]