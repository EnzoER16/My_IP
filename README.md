# My IP

<div align="center">
  <img src="src/assets/icon.png" width="160" height="160" />
</div>

**My IP** is a simple tool written in **Python** designed to quickly display your public IP address.

## 🚀 Features

- **Fast:** Retrieves your IP instantly.
- **Cross-Platform (Flet):** Built with **Flet**, specifically optimized for **Windows** and **Android**.
- **Simple:** Minimalist code that is easy to understand.

> [!WARNING]
> **Current Availability:**
> This tool is currently available for **Windows** and **Android**.
> Builds for **Linux**, **macOS**, and **iOS** are **not yet available**.

## 📋 Prerequisites

Make sure you have Python installed on your system.
- Python 3.8 or higher is recommended.

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/EnzoER16/My_IP.git](https://github.com/EnzoER16/My_IP.git)
   cd My_IP
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   This project uses `requirements.txt` to manage necessary libraries.
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To run the tool from the source code, navigate to the project folder and run the main script:

```bash
flet run src/main.py
```

> [!NOTE]
> It is recommended to run the application with flet run to ensure the UI renders properly.

## 📱 Building Executables (EXE & APK)

This project leverages **[Flet](https://flet.dev/)** to package the Python script into standalone executables.

- **Windows (.exe):** You can build a standalone executable for Windows.
- **Android (.apk):** Flet allows compiling the app for Android devices.

> [!NOTE]
> Check the official [Flet documentation](https://flet.dev/docs/guides/python/packaging-desktop-app) for instructions on how to build these packages locally.

## 🤝 Contributing

Contributions are welcome! If you have ideas to improve the tool:

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the **GPL-3.0 License**. See the [LICENSE](LICENSE) file for details.