from models import Video
from fastapi import Body, Query
from typing import Annotated, Union
import uuid
from fastapi import StreamingResponse

# empty YT videos db
# key: URL; value: Video Object
videos_db = {}

# empty YT 'starred' videos db
starred_db = {}

## ERRORS CLASSES


class ItemNotFoundError(Exception):
    pass

    ## PRIVATE FUNCTIONS
# getting random YT music URL


def get_random_url() -> str:
    # for now return generic url
    return "https://www.youtube.com/watch?v=ikI5xdew6RM"

# goal is to take a local file path and output the download stream


def iterfile(file_path: str):
    with open(file_path, mode="rb") as file:
        yield from file

# download from a filepath using iterfile


def download(file_path: str) -> StreamingResponse:
    return StreamingResponse(iterfile(file_path), media_type="video/mp4")


class APIService:
    ## PUBLIC FUNCTIONS
    # post_url: gets random YT music URL ->
    #           gets information about YT video
    #           places information into Video object
    #           places Video object into videos_db
    #           returns Video object
    def post_url(self, video: Video) -> Video:
        videos_db[video.url] = video
    
    # toggle_star: takes url as string ->
    # checks it exists within videos_db
    # checks if it already exists within starred_db
    # adds it to starred_db if it does
    # otherwise; removes it from starred_db
    # NOT IDEMPOTENT
    def toggle_star(self, url: str) -> None:
        if url not in videos_db:
            raise ItemNotFoundError("Item not found in database")

        if url in starred_db:
            del starred_db[url]

        starred_db[url] = videos_db[url]

    # get_video: gets Video object from videos_db if it exists
    def get_video(self, url: str) -> (Video | None):
        # check if it exists
        if url not in videos_db:
            raise ItemNotFoundError("URL is not in the database")

        return videos_db[url]

    # clear_db: clears all videos in database to refresh user
    def clear_db() -> None:
        videos_db.clear()
        starred_db.clear()
