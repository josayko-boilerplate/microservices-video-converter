# type: ignore
import pika, json


def import(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
    )

