import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

parser = argparse.ArgumentParser(description="Send a prompt to Gemini AI")
parser.add_argument("prompt", type=str, help="The prompt to send")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=args.prompt)])
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)

if args.verbose:
    print(f'User prompt: "{args.prompt}"')
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")