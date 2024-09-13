you should see that both interfaces are synchronized and display the same data between gui and terminal 

### Python version 👍
Python 3.11.1

###  ⚙️  HOW TO START  ⚙️
python main.py

###  🚀 Model (model.py): 🚀

- เก็บข้อมูลคู่ค่า-คีย์ และให้วิธีการสำหรับการดึงข้อมูลและการตั้งค่า

###  🖼️ View (view.py): 🖼️

- แสดงข้อมูลทั้งในเทอร์มินัลและใน GUI ที่สร้างโดย Tkinter
- รับข้อมูลจากผู้ใช้ทั้งผ่านทางเทอร์มินัลและกล่องสนทนาใน GUI
- ใช้กล่องข้อความ (text box) เพื่อแสดงข้อมูลใน GUI

###  📐 Controller (controller.py):  📐

- จัดการการทำงานระหว่าง Model และ View
- รัน GUI ในเธรดแยกโดยใช้โมดูล threading ของ Python ดังนั้นเทอร์มินัลและ GUI สามารถทำงานพร้อมกันได้
- มีลูปที่ต่อเนื่องเพื่อให้สามารถรับข้อมูลจากเทอร์มินัลขณะที่ GUI ยังคงทำงานอยู่



