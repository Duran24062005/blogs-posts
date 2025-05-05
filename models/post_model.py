from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class PostModel(BaseModel):
    id: Optional[int] = Field(None, description="The ID of the post")
    title: str = Field(..., description="The title of the post")
    content: str = Field(..., description="The content of the post")
    author_id: int = Field(..., description="The ID of the author")
    created_at: datetime = Field(default_factory=datetime.now, description="The creation date of the post")
    updated_at: Optional[datetime] = Field(None, description="The last update date of the post")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Sample Post",
                "content": "This is a sample post content.",
                "author_id": 1,
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z"
            }
        }