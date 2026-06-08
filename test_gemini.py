# Test Gemini API dengan model yang benar
import google.generativeai as genai

API_KEY = "AQ.Ab8RN6IClGmy5gFp50SLZDkiJ8EbQaMg7w9vjv0WtrDmOviVBw"

genai.configure(api_key=API_KEY)

# Pakai model yang kamu bilang bekerja
model = genai.GenerativeModel('gemini-flash-lite-latest')

print("=" * 50)
print("TEST GEMINI API - Generate Rangkuman")
print("=" * 50)

# Test 1: Rangkuman teks
teks = """
Fotosintesis adalah proses tumbuhan hijau membuat makanan dari sinar matahari.
Proses ini membutuhkan air dan karbon dioksida.
Hasilnya adalah glukosa dan oksigen.
"""

response = model.generate_content(f"Rangkum teks berikut: {teks}")
print("📖 HASIL RANGKUMAN:")
print(response.text)

print("\n" + "=" * 50)
print("TEST GEMINI API - Generate Kode")
print("=" * 50)

# Test 2: Generate kode
response2 = model.generate_content("Buat fungsi Python untuk menghitung luas lingkaran")
print("💻 HASIL GENERATE KODE:")
print(response2.text)

print("\n✅ Gemini API siap digunakan!")