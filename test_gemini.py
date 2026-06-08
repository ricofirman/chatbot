from google import genai

API_KEY = "AQ.Ab8RN6IClGmy5gFp50SLZDkiJ8EbQaMg7w9vjv0WtrDmOviVBw"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Jelaskan kecerdasan buatan dalam 2 kalimat"
)

print(response.text)
print("\n✅ Gemini berhasil!")