from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.responses import PlainTextResponse
import json

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

@app.get("/transcript_for_subtitles/{video_id}")
async def get_transcript_for_subtitles(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        # Handle errors (e.g., video not found or no transcript available)
        raise HTTPException(status_code=404, detail=str(e))
    json_transcript = json.dumps(transcript, indent=4)
    return {"video_id": video_id, "transcript": json_transcript}

@app.get("/privacy-policy", response_class=PlainTextResponse)
async def get_privacy_policy():
    privacy_policy = """
    Privacy Policy for youtube-transcript

    Welcome toyoutube-transcript. We are committed to protecting your privacy. This Privacy Policy explains how we collect, use, and disclose information through our application youtube-transcript.
    
    Information We Collect
    User-Provided Information: When you use our service to obtain transcripts from YouTube videos, you provide us with the video ID. We do not require you to create an account, nor do we collect any personal information.
    
    Automatically Collected Information: Our application does not automatically collect any personal information about you. We may collect non-personal information about your use of the app, such as error logs, for the purpose of improving our service.
    
    How We Use Information
    We use the video ID provided by you solely for the purpose of fetching the corresponding transcript from YouTube. We do not store, share, or use this information for any other purposes.
    
    Data Storage and Security
    We do not store any personal data or transcripts obtained during your use of our service. Our application is designed to ensure that your use of the service remains private and secure.
    
    Changes to This Privacy Policy
    We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page. You are advised to review this Privacy Policy periodically for any changes.
    
    Contact Us
    If you have any questions about this Privacy Policy, please contact us at kevinlopez@braincorp.fr.
    """
    return privacy_policy
