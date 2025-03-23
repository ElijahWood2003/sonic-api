from pydantic import BaseModel, Field
from typing import Annotated


# Video is a YT video with JSON infomration
class Video(BaseModel):
    url: Annotated[
        str,
        Field(
            description="YT music url",
        ),
    ]
    title: Annotated[
        str,
        Field(
            description="Title of the YT video",
        ),
    ]
    artist: Annotated[
        str,
        Field(
            description="Artist of music",
        ),
    ]
    release: Annotated[
        list | None,
        Field(
            description="Release date of music",
        ),
    ]
    views: Annotated[
        int,
        Field(
            description="Number of views of video",
        ),
    ]
