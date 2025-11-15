# 🔐 Password Security Checking System

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## 📋 คำอธิบายโปรเจกต์

**Password Security Checking System** เป็นระบบตรวจสอบความปลอดภัยของรหัสผ่านที่พัฒนาด้วย Python FastAPI โดยมีวัตถุประสงค์เพื่อช่วยให้ผู้ใช้สามารถตรวจสอบความแข็งแกร่ง ตรวจสอบว่ารหัสผ่านเคยรั่วไหลหรือไม่ และรับคำแนะนำจาก AI ในการปรับปรุงรหัสผ่านให้มีความปลอดภัยมากขึ้น ระบบจะวิเคราะห์รหัสผ่านตามเกณฑ์มาตรฐานความปลอดภัยและให้คำแนะนำอัจฉริยะในการปรับปรุง

---

## 🎯 วัตถุประสงค์ / เป้าหมาย

1. **ตรวจสอบความแข็งแกร่งของรหัสผ่าน** - วิเคราะห์รหัสผ่านตามเกณฑ์มาตรฐานความปลอดภัย (ความยาว, ความซับซ้อน, ความหลากหลายของอักขระ)
2. **ตรวจสอบรหัสผ่านที่รั่วไหล** - เชื่อมต่อกับฐานข้อมูลรหัสผ่านที่รั่วไหลเพื่อตรวจสอบว่ารหัสผ่านเคยถูกเปิดเผยหรือไม่
3. **ให้คำแนะนำจาก AI** - ใช้ AI ในการวิเคราะห์และให้คำแนะนำเฉพาะเจาะจงสำหรับแต่ละรหัสผ่าน
4. **ให้บริการผ่าน RESTful API** - รองรับการใช้งานผ่าน API สำหรับการบูรณาการกับระบบอื่น
5. **แสดงผลการตรวจสอบแบบ Real-time** - ให้ผลการตรวจสอบทันทีพร้อมรายละเอียดและคำแนะนำ

---

## 🛠️ Tech Stack

| เทคโนโลยี | เวอร์ชัน | วัตถุประสงค์ |
|-----------|---------|-------------|
| **Python** | 3.11+ | ภาษาโปรแกรมหลัก |
| **FastAPI** | 0.104+ | Framework สำหรับพัฒนา Web API ที่รวดเร็วและทันสมัย |
| **Uvicorn** | - | ASGI server สำหรับรัน FastAPI application |
| **Pydantic** | - | สำหรับการ validate และ serialize ข้อมูล |
| **Requests** | - | สำหรับการเรียกใช้ external API (เช่น Have I Been Pwned) |
| **hashlib** | - | สำหรับการ hash รหัสผ่าน (SHA-1) เพื่อตรวจสอบการรั่วไหล |
| **re** | - | สำหรับการตรวจสอบรูปแบบรหัสผ่านด้วย Regular Expression |
| **pytest** | - | สำหรับการทดสอบ Unit Test และ Integration Test |

---

## ✨ Core Features

- ✅ **การตรวจสอบความยาวของรหัสผ่าน** - ตรวจสอบว่ารหัสผ่านมีความยาวเพียงพอหรือไม่ (แนะนำอย่างน้อย 8-12 ตัวอักษร)
- ✅ **การตรวจสอบความซับซ้อน** - ตรวจสอบว่ามีการใช้ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก, ตัวเลข, และอักขระพิเศษ
- ✅ **การตรวจสอบรหัสผ่านที่ใช้บ่อย** - ตรวจสอบว่ารหัสผ่านอยู่ในรายการรหัสผ่านที่ใช้บ่อยหรือไม่
- ✅ **การตรวจสอบรหัสผ่านที่รั่วไหล** - เชื่อมต่อกับ Have I Been Pwned API เพื่อตรวจสอบว่ารหัสผ่านเคยรั่วไหลหรือไม่
- ✅ **การให้คะแนนความปลอดภัย** - ให้คะแนนความปลอดภัยของรหัสผ่าน (WEAK, MEDIUM, STRONG)
- ✅ **คำแนะนำจาก AI** - ใช้ AI ในการวิเคราะห์และให้คำแนะนำเฉพาะเจาะจงสำหรับแต่ละรหัสผ่าน
- ✅ **RESTful API** - ให้บริการผ่าน REST API สำหรับการบูรณาการ
- ✅ **Response แบบ JSON** - ส่งผลการตรวจสอบในรูปแบบ JSON ที่เข้าใจง่าย
- ✅ **Auto-generated API Documentation** - FastAPI สร้าง API documentation อัตโนมัติ (Swagger UI)

---

## 📁 Project Structure

```
password-security-checking-system/
│
├── app.py                      # Main FastAPI application file
├── password_checker.py         # Password checking logic module
├── breach_checker.py           # Breach checking module (Have I Been Pwned)
├── ai_recommender.py           # AI-based recommendation module
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (optional)
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
│
└── tests/                      # Test files (optional)
    ├── test_app.py
    ├── test_password_checker.py
    └── test_breach_checker.py
```

---

## 🔄 System Flow

### ขั้นตอนการทำงานของระบบ

1. **ผู้ใช้ส่งคำขอตรวจสอบรหัสผ่าน**
   - ส่ง HTTP POST request ไปยัง endpoint `/check-password`
   - ข้อมูลรหัสผ่านถูกส่งในรูปแบบ JSON: `{ "password": "..." }`

2. **FastAPI รับและ Validate คำขอ**
   - FastAPI รับ request และทำการ validate ข้อมูลด้วย Pydantic
   - ตรวจสอบว่ามี field `password` และไม่เป็นค่าว่าง

3. **ตรวจสอบความแข็งแกร่งของรหัสผ่าน**
   - `check_strength(password)` ทำการวิเคราะห์:
     - ตรวจสอบความยาว (อย่างน้อย 8 ตัวอักษร)
     - ตรวจสอบความซับซ้อน (ตัวพิมพ์ใหญ่, ตัวพิมพ์เล็ก, ตัวเลข, อักขระพิเศษ)
     - ตรวจสอบกับรายการรหัสผ่านที่ใช้บ่อย
     - คำนวณระดับความแข็งแกร่ง (WEAK, MEDIUM, STRONG)

4. **ตรวจสอบรหัสผ่านที่รั่วไหล**
   - `check_breach(password)` ทำการตรวจสอบ:
     - Hash รหัสผ่านด้วย SHA-1
     - ส่ง 5 ตัวอักษรแรกของ hash ไปยัง Have I Been Pwned API
     - ตรวจสอบว่ารหัสผ่านเต็มอยู่ในรายการที่รั่วไหลหรือไม่
     - ส่งผลลัพธ์กลับ (BREACHED หรือ SAFE)

5. **สร้างคำแนะนำจาก AI**
   - `ai_recommendation(password, strength, breach_status)` วิเคราะห์:
     - รับข้อมูลความแข็งแกร่งและสถานะการรั่วไหล
     - วิเคราะห์จุดอ่อนของรหัสผ่าน
     - สร้างคำแนะนำเฉพาะเจาะจงและเป็นประโยชน์
     - ส่งคำแนะนำกลับในรูปแบบข้อความที่เข้าใจง่าย

6. **สร้าง Response**
   - รวมผลลัพธ์ทั้งหมด:
     - `strength`: ระดับความแข็งแกร่ง (WEAK/MEDIUM/STRONG)
     - `breachStatus`: สถานะการรั่วไหล (BREACHED/SAFE)
     - `aiSuggestion`: คำแนะนำจาก AI

7. **ส่งผลลัพธ์กลับ**
   - ส่ง JSON response กลับไปยังผู้ใช้
   - Status code: 200 OK

---

## 🤖 AI Agent Description

### วัตถุประสงค์ของ AI Agent

AI Agent ในระบบนี้มีหน้าที่วิเคราะห์รหัสผ่านและให้คำแนะนำอัจฉริยะเพื่อช่วยให้ผู้ใช้สร้างรหัสผ่านที่ปลอดภัยมากขึ้น โดยใช้ข้อมูลจากผลการตรวจสอบความแข็งแกร่งและสถานะการรั่วไหลมาประมวลผลและสร้างคำแนะนำที่เฉพาะเจาะจง

### งานหลักของ AI Agent

1. **การวิเคราะห์รหัสผ่าน**
   - วิเคราะห์จุดแข็งและจุดอ่อนของรหัสผ่าน
   - ระบุปัญหาที่พบ (เช่น ความยาวไม่เพียงพอ, ขาดอักขระพิเศษ, ใช้รหัสผ่านที่รั่วไหล)

2. **การสร้างคำแนะนำ**
   - สร้างคำแนะนำที่เฉพาะเจาะจงตามปัญหาที่พบ
   - ให้ตัวอย่างรหัสผ่านที่ปลอดภัยมากขึ้น (โดยไม่เปิดเผยรหัสผ่านเดิม)
   - แนะนำเทคนิคการสร้างรหัสผ่านที่ปลอดภัย

3. **การให้คำแนะนำตามบริบท**
   - ปรับคำแนะนำตามระดับความแข็งแกร่งของรหัสผ่าน
   - ให้คำแนะนำที่แตกต่างกันสำหรับรหัสผ่านที่รั่วไหลและไม่รั่วไหล
   - แนะนำขั้นตอนการปรับปรุงตามลำดับความสำคัญ

### ขั้นตอนการทำงานของ AI Agent

```
Input: password, strength, breach_status
    ↓
1. วิเคราะห์จุดอ่อนของรหัสผ่าน
    ↓
2. ตรวจสอบสถานะการรั่วไหล
    ↓
3. สร้างคำแนะนำตามปัญหาเฉพาะ
    ↓
4. จัดลำดับความสำคัญของคำแนะนำ
    ↓
5. สร้างข้อความคำแนะนำที่เข้าใจง่าย
    ↓
Output: aiSuggestion (ข้อความคำแนะนำ)
```

### ตัวอย่างผลลัพธ์จาก AI Agent

**ตัวอย่างที่ 1: รหัสผ่านอ่อนแอ**
- **Input:** `password123` (WEAK, SAFE)
- **Output:** `"รหัสผ่านของคุณอ่อนแอและเสี่ยงต่อการถูกโจมตี แนะนำให้: 1) เพิ่มความยาวเป็นอย่างน้อย 12 ตัวอักษร 2) เพิ่มตัวอักษรพิมพ์ใหญ่ เช่น 'P' 3) เพิ่มอักขระพิเศษ เช่น '@', '!', '#' 4) หลีกเลี่ยงคำที่พบบ่อย เช่น 'password' ตัวอย่างรหัสผ่านที่ปลอดภัย: 'MyStr0ng!P@ssw0rd'"`

**ตัวอย่างที่ 2: รหัสผ่านที่รั่วไหล**
- **Input:** `12345678` (WEAK, BREACHED)
- **Output:** `"⚠️ ภัยคุกคามร้ายแรง! รหัสผ่านนี้เคยรั่วไหลในฐานข้อมูลที่ถูกแฮ็ก แนะนำให้เปลี่ยนรหัสผ่านทันทีและไม่ใช้รหัสผ่านนี้อีก ควรสร้างรหัสผ่านใหม่ที่: 1) มีความยาวอย่างน้อย 12 ตัวอักษร 2) ประกอบด้วยตัวพิมพ์ใหญ่, ตัวพิมพ์เล็ก, ตัวเลข, และอักขระพิเศษ 3) ไม่ใช่ตัวเลขหรือลำดับตัวอักษรที่ง่าย 4) ไม่ซ้ำกับรหัสผ่านเก่า"`

**ตัวอย่างที่ 3: รหัสผ่านปานกลาง**
- **Input:** `Password123` (MEDIUM, SAFE)
- **Output:** `"รหัสผ่านของคุณมีความปลอดภัยปานกลาง แต่ยังสามารถปรับปรุงได้ แนะนำให้: 1) เพิ่มอักขระพิเศษ เช่น '@', '!', '#' เพื่อเพิ่มความซับซ้อน 2) เพิ่มความยาวเป็นอย่างน้อย 12 ตัวอักษร 3) หลีกเลี่ยงการใช้คำที่พบบ่อย เช่น 'Password' ตัวอย่าง: 'MyP@ssw0rd!2024'"`

**ตัวอย่างที่ 4: รหัสผ่านแข็งแกร่ง**
- **Input:** `P@ssw0rd!2024#Secure` (STRONG, SAFE)
- **Output:** `"✅ ยอดเยี่ยม! รหัสผ่านของคุณมีความปลอดภัยสูง ประกอบด้วยความยาวที่เพียงพอ, ตัวพิมพ์ใหญ่/เล็ก, ตัวเลข, และอักขระพิเศษ และไม่พบในฐานข้อมูลที่รั่วไหล อย่างไรก็ตาม แนะนำให้: 1) เปลี่ยนรหัสผ่านทุก 90 วัน 2) ไม่ใช้รหัสผ่านเดียวกันกับบัญชีอื่น 3) ใช้ Password Manager เพื่อจัดการรหัสผ่านหลายตัว"`

---

## 📊 Example Use Case

### สถานการณ์การใช้งาน

| สถานการณ์ | รหัสผ่านที่ทดสอบ | ผลลัพธ์ที่คาดหวัง |
|-----------|------------------|-------------------|
| **รหัสผ่านอ่อนแอ** | `password123` | ❌ WEAK, SAFE - มีคำแนะนำให้ปรับปรุงความยาวและเพิ่มอักขระพิเศษ |
| **รหัสผ่านปานกลาง** | `Password123` | ⚠️ MEDIUM, SAFE - แนะนำให้เพิ่มอักขระพิเศษและความยาว |
| **รหัสผ่านแข็งแกร่ง** | `P@ssw0rd!2024` | ✅ STRONG, SAFE - ปลอดภัย แต่แนะนำให้เปลี่ยนเป็นระยะ |
| **รหัสผ่านสั้นเกินไป** | `Pass1!` | ❌ WEAK, SAFE - ความยาวไม่เพียงพอ, แนะนำให้เพิ่มความยาว |
| **รหัสผ่านที่ใช้บ่อย** | `12345678` | ❌ WEAK, BREACHED - อยู่ในรายการรหัสผ่านที่ใช้บ่อยและเคยรั่วไหล |
| **รหัสผ่านที่รั่วไหล** | `qwerty123` | ❌ WEAK, BREACHED - เคยรั่วไหล, แนะนำให้เปลี่ยนทันที |

---

## 🌐 Example API

### Request

**Endpoint:** `POST /check-password`

**Headers:**
```http
Content-Type: application/json
```

**Body:**
```json
{
  "password": "MyP@ssw0rd123!"
}
```

### Response

**Success Response (200 OK):**
```json
{
  "strength": "STRONG",
  "breachStatus": "SAFE",
  "aiSuggestion": "✅ ยอดเยี่ยม! รหัสผ่านของคุณมีความปลอดภัยสูง ประกอบด้วยความยาวที่เพียงพอ (15 ตัวอักษร), ตัวพิมพ์ใหญ่/เล็ก, ตัวเลข, และอักขระพิเศษ และไม่พบในฐานข้อมูลที่รั่วไหล อย่างไรก็ตาม แนะนำให้: 1) เปลี่ยนรหัสผ่านทุก 90 วัน 2) ไม่ใช้รหัสผ่านเดียวกันกับบัญชีอื่น 3) ใช้ Password Manager เพื่อจัดการรหัสผ่านหลายตัว"
}
```

**Weak Password Response (200 OK):**
```json
{
  "strength": "WEAK",
  "breachStatus": "SAFE",
  "aiSuggestion": "รหัสผ่านของคุณอ่อนแอและเสี่ยงต่อการถูกโจมตี แนะนำให้: 1) เพิ่มความยาวเป็นอย่างน้อย 12 ตัวอักษร 2) เพิ่มตัวอักษรพิมพ์ใหญ่ เช่น 'P' 3) เพิ่มอักขระพิเศษ เช่น '@', '!', '#' 4) หลีกเลี่ยงคำที่พบบ่อย เช่น 'password' ตัวอย่างรหัสผ่านที่ปลอดภัย: 'MyStr0ng!P@ssw0rd'"
}
```

**Breached Password Response (200 OK):**
```json
{
  "strength": "WEAK",
  "breachStatus": "BREACHED",
  "aiSuggestion": "⚠️ ภัยคุกคามร้ายแรง! รหัสผ่านนี้เคยรั่วไหลในฐานข้อมูลที่ถูกแฮ็ก แนะนำให้เปลี่ยนรหัสผ่านทันทีและไม่ใช้รหัสผ่านนี้อีก ควรสร้างรหัสผ่านใหม่ที่: 1) มีความยาวอย่างน้อย 12 ตัวอักษร 2) ประกอบด้วยตัวพิมพ์ใหญ่, ตัวพิมพ์เล็ก, ตัวเลข, และอักขระพิเศษ 3) ไม่ใช่ตัวเลขหรือลำดับตัวอักษรที่ง่าย 4) ไม่ซ้ำกับรหัสผ่านเก่า"
}
```

---

## 🚀 Installation & Run Instructions

### ความต้องการของระบบ

- **Python** เวอร์ชัน 3.11 หรือสูงกว่า
- **pip** (Python package manager)
- **Windows 10/11** (สำหรับคำสั่ง Windows)

### วิธีติดตั้งและรันโปรเจกต์

#### ขั้นตอนที่ 1: ตรวจสอบการติดตั้ง Python

1. **เปิด Command Prompt หรือ PowerShell**
   ```cmd
   python --version
   ```
   
   หรือ
   ```cmd
   python3 --version
   ```

2. **ตรวจสอบว่า Python เวอร์ชัน 3.11 หรือสูงกว่า**
   - หากยังไม่ได้ติดตั้ง Python ให้ดาวน์โหลดจาก [python.org](https://www.python.org/downloads/)

#### ขั้นตอนที่ 2: ติดตั้ง Dependencies

1. **เปิด Command Prompt หรือ PowerShell และไปที่โฟลเดอร์โปรเจกต์**
   ```cmd
   cd "C:\Users\WINDOWS11\OneDrive\Desktop\Check password"
   ```

2. **สร้าง Virtual Environment (แนะนำ)**
   ```cmd
   python -m venv venv
   ```

3. **เปิดใช้งาน Virtual Environment**
   ```cmd
   venv\Scripts\activate
   ```
   
   หลังจากเปิดใช้งานแล้ว จะเห็น `(venv)` หน้าคำสั่ง

4. **ติดตั้ง dependencies จาก requirements.txt**
   ```cmd
   pip install -r requirements.txt
   ```
   
   หรือติดตั้งทีละตัว:
   ```cmd
   pip install fastapi uvicorn[standard] requests pydantic
   ```

#### ขั้นตอนที่ 3: รัน FastAPI Server

**วิธีที่ 1: ใช้คำสั่ง uvicorn โดยตรง**

1. **รัน server ด้วยคำสั่ง:**
   ```cmd
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```
   
   หรือ
   ```cmd
   python -m uvicorn app:app --reload --port 8000
   ```

2. **รอให้ server เริ่มทำงาน**
   - จะเห็นข้อความ `Uvicorn running on http://0.0.0.0:8000` ในคอนโซล

3. **เปิดเบราว์เซอร์และไปที่:**
   ```
   http://localhost:8000
   ```

4. **เข้าถึง API Documentation (Swagger UI):**
   ```
   http://localhost:8000/docs
   ```
   
   หรือ ReDoc:
   ```
   http://localhost:8000/redoc
   ```

**วิธีที่ 2: ใช้ Python script โดยตรง**

1. **รันไฟล์ app.py:**
   ```cmd
   python app.py
   ```

2. **เปิดเบราว์เซอร์และไปที่:**
   ```
   http://localhost:8000
   ```

#### ขั้นตอนที่ 4: ทดสอบ API

**วิธีที่ 1: ใช้ Swagger UI (แนะนำ)**
1. เปิดเบราว์เซอร์ไปที่ `http://localhost:8000/docs`
2. คลิกที่ endpoint `/check-password`
3. คลิก "Try it out"
4. ใส่ข้อมูล JSON: `{ "password": "MyP@ssw0rd123!" }`
5. คลิก "Execute"

**วิธีที่ 2: ใช้ PowerShell (Windows)**

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/check-password" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"password": "MyP@ssw0rd123!"}'
```

**วิธีที่ 3: ใช้ curl (ถ้ามี Git Bash หรือ WSL)**

```bash
curl -X POST "http://localhost:8000/check-password" \
  -H "Content-Type: application/json" \
  -d "{\"password\": \"MyP@ssw0rd123!\"}"
```

**วิธีที่ 4: ใช้ Python requests**

สร้างไฟล์ `test_api.py`:
```python
import requests

response = requests.post(
    "http://localhost:8000/check-password",
    json={"password": "MyP@ssw0rd123!"}
)
print(response.json())
```

รันด้วย:
```cmd
python test_api.py
```

### การหยุด Server

- กด `Ctrl + C` ใน Command Prompt หรือ PowerShell ที่รัน server อยู่

---

## 🔮 Future Improvements

### การพัฒนาต่อในอนาคต

- [ ] **การเชื่อมต่อกับ Have I Been Pwned API จริง** - ปรับปรุง `check_breach()` ให้เชื่อมต่อกับ Have I Been Pwned API จริง (ต้องใช้ API key)
- [ ] **การใช้งาน Machine Learning** - ใช้ ML model เพื่อประเมินความแข็งแกร่งของรหัสผ่านที่แม่นยำมากขึ้น
- [ ] **การใช้งาน Large Language Model (LLM)** - เชื่อมต่อกับ OpenAI API หรือ local LLM เพื่อให้คำแนะนำที่ชาญฉลาดมากขึ้น
- [ ] **Dashboard สำหรับแสดงสถิติ** - สร้างหน้าเว็บสำหรับแสดงสถิติการตรวจสอบรหัสผ่าน
- [ ] **การบันทึกประวัติการตรวจสอบ** - บันทึกประวัติการตรวจสอบรหัสผ่าน (โดยไม่เก็บรหัสผ่านจริง, เก็บเฉพาะ hash)
- [ ] **Rate Limiting** - จำกัดจำนวนคำขอต่อ IP เพื่อป้องกันการโจมตี
- [ ] **Authentication & Authorization** - เพิ่มระบบยืนยันตัวตนสำหรับการใช้งาน API
- [ ] **Database Integration** - เชื่อมต่อกับ database เพื่อเก็บสถิติและประวัติ
- [ ] **Unit Tests & Integration Tests** - เพิ่มการทดสอบให้ครอบคลุมมากขึ้นด้วย pytest
- [ ] **Docker Support** - สร้าง Docker image และ docker-compose.yml สำหรับการ deploy
- [ ] **CI/CD Pipeline** - สร้าง CI/CD pipeline สำหรับการ deploy อัตโนมัติ
- [ ] **Multi-language Support** - รองรับหลายภาษาในการแสดงผลและคำแนะนำ
- [ ] **Password Generator** - เพิ่มฟีชันสร้างรหัสผ่านที่ปลอดภัยอัตโนมัติ
- [ ] **Password Strength Meter** - สร้าง visual strength meter สำหรับแสดงผลใน UI

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Contributors

- **Developer Team** - Initial work

---

## 📧 Contact

สำหรับคำถามหรือข้อเสนอแนะ กรุณาติดต่อทีมพัฒนา

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

**หมายเหตุ:** โปรเจกต์นี้พัฒนาสำหรับวัตถุประสงค์ทางการศึกษาและเป็นส่วนหนึ่งของงานวิชาการ
