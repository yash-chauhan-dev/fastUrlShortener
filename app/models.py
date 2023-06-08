import uuid

from pydantic import AnyHttpUrl, BaseModel, Field


class URL(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    original_url: AnyHttpUrl = Field(..., default=None)
    fuzzy_url: AnyHttpUrl = Field(..., default=None)
