# Project Name 👍

A brief description of what your project does and its purpose.

## Python version ❗❗
Python 3.11.1

## Introduction 👁️‍🗨️
This project is an MVC (Model-View-Controller) architecture example combining both terminal and graphical user interfaces (GUI) using Tkinter. The purpose is to demonstrate how to manage data and interactions between a model, view, and controller in a Python application. The project allows for data input and display through both terminal and GUI interfaces.

**Model (model.py):**

- เก็บข้อมูลคู่ค่า-คีย์ และให้วิธีการสำหรับการดึงข้อมูลและการตั้งค่า

**View (view.py):**

- แสดงข้อมูลทั้งในเทอร์มินัลและใน GUI ที่สร้างโดย Tkinter
- รับข้อมูลจากผู้ใช้ทั้งผ่านทางเทอร์มินัลและกล่องสนทนาใน GUI
- ใช้กล่องข้อความ (text box) เพื่อแสดงข้อมูลใน GUI

**Controller (controller.py)**

- จัดการการทำงานระหว่าง Model และ View
- รัน GUI ในเธรดแยกโดยใช้โมดูล threading ของ Python ดังนั้นเทอร์มินัลและ GUI สามารถทำงานพร้อมกันได้
- มีลูปที่ต่อเนื่องเพื่อให้สามารถรับข้อมูลจากเทอร์มินัลขณะที่ GUI ยังคงทำงานอยู่


## Features 🚀

- **Dual Interfaces**: Provides both a terminal-based interface and a Tkinter GUI for data input and display.
- **Real-Time Synchronization**: Updates data in real-time across both interfaces.
- **Data Management**: Allows for input, display, and management of key-value data.

## Installation ⚙️

1. **Create a Virtual Environment**
   python -m venv venv

2. **Activate the Virtual Environment**

   - **Windows:**
     venv\Scripts\activate

   - **macOS/Linux:**
     source venv/bin/activate

3. **Install Dependencies**
   pip install -r requirements.txt

4. **Run the Project**
   python main.py


## Usage 🖼️

- **Terminal Interface**: Enter key-value pairs directly in the terminal when prompted.
- **GUI Interface**: Use the Tkinter GUI to enter key-value pairs through dialog boxes.
