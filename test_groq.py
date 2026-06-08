from groq import Groq

API_KEY = "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"  # Ganti dengan API key Groq kamu

client = Groq(api_key=API_KEY)

print("=" * 50)
print("TEST 1: Generate teks sederhana")
print("=" * 50)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Jelaskan apa itu kecerdasan buatan dalam 2 kalimat"}]
)
print(response.choices[0].message.content)

print("\n" + "=" * 50)
print("TEST 2: Generate kode program")
print("=" * 50)

response2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Buatkan fungsi Python untuk menghitung luas lingkaran"}]
)
print(response2.choices[0].message.content)

print("\n✅ GROQ BERHASIL! Siap lanjut ke app.py")
