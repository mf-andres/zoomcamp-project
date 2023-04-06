from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    keywords: List[str]
    project_id: str
    bucket_id: str
    dataset_id: str
