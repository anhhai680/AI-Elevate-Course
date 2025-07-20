from openai import OpenAI
from settings import settings

# Step 1: Initialize Settings
config = settings()
config.load_from_env()

# Step 2: Initialize OpenAI Client
client = OpenAI(
    api_key=config.openai_api_key,
)

# Step 3: Load transcript text (example: read from a file)
with open("data/meeting_transcript.txt", "r") as file:
    transcript = file.read()

def summarize_meeting(transcript):
    # Step 4: Craft prompt for summarization
    system_prompt = "You are a helpful assistant that summarizes meeting transcripts."
    user_prompt = f"Summarize the following meeting transcript with key points, decisions, and action items:\n\n{transcript}"

    # Call OpenAI API to generate summary
    response = client.chat.completions.create(
        model=config.openai_model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content.strip() # type: ignore

# Step 5: Generate and print summary
summary = summarize_meeting(transcript)
print(f"Meeting Summary: \n\n{summary}")