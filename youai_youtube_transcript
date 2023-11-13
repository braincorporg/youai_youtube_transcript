from fastapi import FastAPI, HTTPException
from YouTubeTranscriptApi import YouTubeTranscriptApi

app = FastAPI()

@app.get("/transcript/{video_id}")
async def get_transcript(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        # Handle errors (e.g., video not found or no transcript available)
        raise HTTPException(status_code=404, detail=str(e))

    full_text = " ".join([entry['text'] for entry in transcript])
    return {"video_id": video_id, "transcript": full_text}
