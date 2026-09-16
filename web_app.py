import streamlit as st
import requests

# 1. ตั้งค่าพื้นฐานของหน้าเว็บ (แท็บเบราว์เซอร์)
st.set_page_config(page_title="แอปสุ่มเรื่องตลก", page_icon="😂")

# 2. ใส่หัวข้อหลักและข้อความอธิบาย
st.title("😂 แอปพลิเคชันสุ่มเรื่องตลก")
st.write("แอปนี้เขียนด้วย Python ล้วนๆ! พร้อมจะหัวเราะหรือยัง? กดปุ่มด้านล่างเลย")

# 3. สร้างปุ่มกด
# เมื่อปุ่มถูกกด if จะเป็นจริง และโค้ดด้านในจะทำงาน
if st.button("สุ่มเรื่องตลก 🎲", type="primary"):
    
    url = "https://official-joke-api.appspot.com/random_joke"
    
    # แสดงไอคอนหมุนๆ ระหว่างรอข้อมูล (Loading spinner)
    with st.spinner("กำลังดึงข้อมูล..."):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                
                # 4. แสดงผลลัพธ์บนหน้าเว็บ
                st.subheader(data['setup']) # แสดงคำถามแบบตัวหนา
                st.info(data['punchline'])  # แสดงคำตอบในกล่องสีฟ้าสวยๆ
                
            else:
                st.error("ไม่สามารถดึงข้อมูลได้ในขณะนี้")
                
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")