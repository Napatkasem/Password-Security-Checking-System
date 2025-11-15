"""
Password Security Checking System
Main FastAPI application for checking password strength, breach status, and AI recommendations
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import hashlib
import re
import requests

# ==================== Pydantic Models ====================

class PasswordRequest(BaseModel):
    """Request model for password check"""
    password: str = Field(..., description="รหัสผ่านที่ต้องการตรวจสอบ", min_length=1)


class PasswordResponse(BaseModel):
    """Response model for password check result"""
    strength: Literal["WEAK", "MEDIUM", "STRONG"] = Field(..., description="ระดับความแข็งแกร่งของรหัสผ่าน")
    breachStatus: Literal["BREACHED", "SAFE"] = Field(..., description="สถานะการรั่วไหลของรหัสผ่าน")
    aiSuggestion: str = Field(..., description="คำแนะนำจาก AI สำหรับการปรับปรุงรหัสผ่าน")


# ==================== Password Strength Checker ====================

def check_strength(password: str) -> str:
    """
    ตรวจสอบความแข็งแกร่งของรหัสผ่าน
    
    Args:
        password (str): รหัสผ่านที่ต้องการตรวจสอบ
    
    Returns:
        str: ระดับความแข็งแกร่ง ("WEAK", "MEDIUM", "STRONG")
    """
    score = 0
    
    # ตรวจสอบความยาว
    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1
    
    # ตรวจสอบตัวพิมพ์เล็ก
    if re.search(r'[a-z]', password):
        score += 1
    
    # ตรวจสอบตัวพิมพ์ใหญ่
    if re.search(r'[A-Z]', password):
        score += 1
    
    # ตรวจสอบตัวเลข
    if re.search(r'\d', password):
        score += 1
    
    # ตรวจสอบอักขระพิเศษ
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    
    # ตรวจสอบรหัสผ่านที่ใช้บ่อย
    common_passwords = [
        "password", "123456", "12345678", "123456789", "1234567890",
        "qwerty", "abc123", "password123", "admin", "letmein",
        "welcome", "monkey", "1234567", "sunshine", "princess",
        "dragon", "passw0rd", "master", "hello", "freedom"
    ]
    
    if password.lower() in common_passwords:
        score = 0
    
    # ตรวจสอบลำดับตัวอักษรหรือตัวเลขที่ง่าย
    if re.search(r'(.)\1{2,}', password):  # ตัวอักษรซ้ำ 3 ตัวขึ้นไป
        score -= 1
    
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        score -= 1
    
    # คำนวณระดับความแข็งแกร่ง
    if score <= 2:
        return "WEAK"
    elif score <= 5:
        return "MEDIUM"
    else:
        return "STRONG"


# ==================== Breach Checker ====================

def check_common_breached_passwords(password: str) -> str:
    """
    ตรวจสอบว่ารหัสผ่านอยู่ในรายการรหัสผ่านที่รั่วไหลและใช้บ่อยหรือไม่
    
    Args:
        password (str): รหัสผ่านที่ต้องการตรวจสอบ
    
    Returns:
        str: สถานะการรั่วไหล ("BREACHED" หรือ "SAFE")
    """
    # รายการรหัสผ่านที่รั่วไหลและใช้บ่อย (ตัวอย่าง)
    breached_passwords = [
        "123456", "123456789", "12345678", "1234567890",
        "password", "password123", "Password123", "PASSWORD",
        "qwerty", "abc123", "1234567", "monkey", "1234567890",
        "letmein", "trustno1", "dragon", "baseball", "iloveyou",
        "master", "sunshine", "ashley", "bailey", "passw0rd",
        "shadow", "123123", "654321", "superman", "qazwsx",
        "michael", "football", "welcome", "jesus", "ninja"
    ]
    
    if password in breached_passwords or password.lower() in breached_passwords:
        return "BREACHED"
    
    return "SAFE"


def check_breach(password: str) -> str:
    """
    ตรวจสอบว่ารหัสผ่านเคยรั่วไหลหรือไม่โดยใช้ Have I Been Pwned API
    
    Args:
        password (str): รหัสผ่านที่ต้องการตรวจสอบ
    
    Returns:
        str: สถานะการรั่วไหล ("BREACHED" หรือ "SAFE")
    
    Note:
        ฟังก์ชันนี้ใช้ k-anonymity model ของ Have I Been Pwned API
        โดยส่งเฉพาะ 5 ตัวอักษรแรกของ SHA-1 hash เพื่อความเป็นส่วนตัว
    """
    try:
        # Hash รหัสผ่านด้วย SHA-1
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # ใช้ 5 ตัวอักษรแรกสำหรับ k-anonymity
        hash_prefix = sha1_hash[:5]
        hash_suffix = sha1_hash[5:]
        
        # เรียกใช้ Have I Been Pwned API
        url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
        headers = {
            "User-Agent": "Password-Security-Checker/1.0"
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            # ตรวจสอบว่ารหัสผ่านอยู่ในรายการหรือไม่
            # Response format: "HASH:COUNT" (เช่น "0018A45C4D1DEF81644B54AB7F969B88D65:1")
            hashes = response.text.splitlines()
            for hash_line in hashes:
                # แยก hash และ count
                if ':' in hash_line:
                    hash_part = hash_line.split(':')[0]
                    if hash_part == hash_suffix:
                        return "BREACHED"
            return "SAFE"
        else:
            # หาก API ไม่สามารถเข้าถึงได้ ให้ตรวจสอบกับรายการรหัสผ่านที่ใช้บ่อยแทน
            return check_common_breached_passwords(password)
    
    except Exception as e:
        # หากเกิดข้อผิดพลาด ให้ตรวจสอบกับรายการรหัสผ่านที่ใช้บ่อยแทน
        print(f"Error checking breach: {e}")
        return check_common_breached_passwords(password)


# ==================== AI Recommendation Generator ====================

def ai_recommendation(password: str, strength: str, breach_status: str) -> str:
    """
    สร้างคำแนะนำจาก AI สำหรับการปรับปรุงรหัสผ่าน
    
    Args:
        password (str): รหัสผ่านที่ตรวจสอบ
        strength (str): ระดับความแข็งแกร่ง ("WEAK", "MEDIUM", "STRONG")
        breach_status (str): สถานะการรั่วไหล ("BREACHED" หรือ "SAFE")
    
    Returns:
        str: คำแนะนำจาก AI สำหรับการปรับปรุงรหัสผ่าน
    """
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    suggestions = []
    
    # กรณีที่รหัสผ่านรั่วไหล - ให้ความสำคัญสูงสุด
    if breach_status == "BREACHED":
        return (
            "⚠️ ภัยคุกคามร้ายแรง! รหัสผ่านนี้เคยรั่วไหลในฐานข้อมูลที่ถูกแฮ็ก "
            "แนะนำให้เปลี่ยนรหัสผ่านทันทีและไม่ใช้รหัสผ่านนี้อีก "
            "ควรสร้างรหัสผ่านใหม่ที่: "
            "1) มีความยาวอย่างน้อย 12 ตัวอักษร "
            "2) ประกอบด้วยตัวพิมพ์ใหญ่, ตัวพิมพ์เล็ก, ตัวเลข, และอักขระพิเศษ "
            "3) ไม่ใช่ตัวเลขหรือลำดับตัวอักษรที่ง่าย "
            "4) ไม่ซ้ำกับรหัสผ่านเก่า"
        )
    
    # กรณีที่รหัสผ่านอ่อนแอ
    if strength == "WEAK":
        if length < 8:
            suggestions.append(f"เพิ่มความยาวเป็นอย่างน้อย 8-12 ตัวอักษร (ปัจจุบัน: {length} ตัวอักษร)")
        if not has_upper:
            suggestions.append("เพิ่มตัวอักษรพิมพ์ใหญ่ เช่น 'A', 'B', 'C'")
        if not has_lower:
            suggestions.append("เพิ่มตัวอักษรพิมพ์เล็ก เช่น 'a', 'b', 'c'")
        if not has_digit:
            suggestions.append("เพิ่มตัวเลข เช่น '1', '2', '3'")
        if not has_special:
            suggestions.append("เพิ่มอักขระพิเศษ เช่น '@', '!', '#', '$'")
        
        # ตรวจสอบคำที่พบบ่อย
        common_words = ["password", "admin", "user", "login", "welcome"]
        if any(word in password.lower() for word in common_words):
            suggestions.append("หลีกเลี่ยงคำที่พบบ่อย เช่น 'password', 'admin'")
        
        suggestion_text = "รหัสผ่านของคุณอ่อนแอและเสี่ยงต่อการถูกโจมตี แนะนำให้: " + " ".join([f"{i+1}) {s}" for i, s in enumerate(suggestions)])
        suggestion_text += " ตัวอย่างรหัสผ่านที่ปลอดภัย: 'MyStr0ng!P@ssw0rd'"
        
        return suggestion_text
    
    # กรณีที่รหัสผ่านปานกลาง
    elif strength == "MEDIUM":
        if length < 12:
            suggestions.append(f"เพิ่มความยาวเป็นอย่างน้อย 12 ตัวอักษร (ปัจจุบัน: {length} ตัวอักษร)")
        if not has_special:
            suggestions.append("เพิ่มอักขระพิเศษ เช่น '@', '!', '#' เพื่อเพิ่มความซับซ้อน")
        if length < 10:
            suggestions.append("เพิ่มความยาวเพื่อเพิ่มความปลอดภัย")
        
        suggestion_text = "รหัสผ่านของคุณมีความปลอดภัยปานกลาง แต่ยังสามารถปรับปรุงได้ แนะนำให้: " + " ".join([f"{i+1}) {s}" for i, s in enumerate(suggestions)])
        suggestion_text += " ตัวอย่าง: 'MyP@ssw0rd!2024'"
        
        return suggestion_text
    
    # กรณีที่รหัสผ่านแข็งแกร่ง
    else:  # STRONG
        return (
            "✅ ยอดเยี่ยม! รหัสผ่านของคุณมีความปลอดภัยสูง "
            f"ประกอบด้วยความยาวที่เพียงพอ ({length} ตัวอักษร), "
            "ตัวพิมพ์ใหญ่/เล็ก, ตัวเลข, และอักขระพิเศษ "
            "และไม่พบในฐานข้อมูลที่รั่วไหล "
            "อย่างไรก็ตาม แนะนำให้: "
            "1) เปลี่ยนรหัสผ่านทุก 90 วัน "
            "2) ไม่ใช้รหัสผ่านเดียวกันกับบัญชีอื่น "
            "3) ใช้ Password Manager เพื่อจัดการรหัสผ่านหลายตัว"
        )


# ==================== FastAPI Application ====================

# Initialize FastAPI app
app = FastAPI(
    title="Password Security Checking System",
    description="API สำหรับตรวจสอบความปลอดภัยของรหัสผ่าน ตรวจสอบการรั่วไหล และรับคำแนะนำจาก AI",
    version="1.0.0"
)


# ==================== API Endpoints ====================

@app.get("/")
async def root():
    """Root endpoint - welcome message"""
    return {
        "message": "Welcome to Password Security Checking System API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoint": "/check-password"
    }


@app.post("/check-password", response_model=PasswordResponse)
async def check_password(request: PasswordRequest):
    """
    ตรวจสอบความปลอดภัยของรหัสผ่าน
    
    รับรหัสผ่านและส่งกลับ:
    - ระดับความแข็งแกร่ง (strength)
    - สถานะการรั่วไหล (breachStatus)
    - คำแนะนำจาก AI (aiSuggestion)
    
    Args:
        request (PasswordRequest): ข้อมูลรหัสผ่านที่ต้องการตรวจสอบ
    
    Returns:
        PasswordResponse: ผลการตรวจสอบรหัสผ่าน
    """
    try:
        password = request.password
        
        # ตรวจสอบความแข็งแกร่ง
        strength = check_strength(password)
        
        # ตรวจสอบการรั่วไหล
        breach_status = check_breach(password)
        
        # สร้างคำแนะนำจาก AI
        ai_suggestion = ai_recommendation(password, strength, breach_status)
        
        # สร้าง response
        return PasswordResponse(
            strength=strength,
            breachStatus=breach_status,
            aiSuggestion=ai_suggestion
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"เกิดข้อผิดพลาดในการตรวจสอบรหัสผ่าน: {str(e)}")


# ==================== Run Server ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
