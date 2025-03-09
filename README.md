# EdgeAutomation
The script performs automated searches on edge browser to collect daily reward points.
# Automated Bing Search Bot 🚀  

This Python script automates Bing searches using Selenium WebDriver and `wonderwords`. It performs randomized searches with human-like delays to simulate real browsing behavior.  

## 📌 Features  
- **Automates Bing searches** with randomly generated words.  
- **Randomized delays & scrolling** to avoid bot detection.  
- **User-Agent spoofing** to appear as a real browser.  
- **Disables Selenium WebDriver detection** for stealth execution.
- **Supports headless mode** for running searches in the background without opening a visible browser window.

## 🛠️ Requirements  
Ensure you have the following installed:  
- Python 3.x  
- Latest Microsoft Edge browser & Edge WebDriver (`msedgedriver.exe`)  
- Required Python libraries:  

```bash
pip install selenium wonderwords
```

## 🔧 Setup  
### 1️⃣ Download Edge WebDriver  
- Ensure `msedgedriver.exe` matches your browser version.  
- Place it in `C:\WebDrivers\` or update the path in the script.  

### 2️⃣ Clone this repository  

```bash
git clone https://github.com/apurvwajage/EdgeAutomation.git
cd EdgeAutomation/script
```

### 3️⃣ Run the script  

```bash
python search_engine.py
```

## ⚙️ Configuration  
- Modify `EDGE_DRIVER_PATH` in the script if necessary.  
- Adjust `time.sleep()` values for different delay ranges.  

## 🔒 Disclaimer  
This script is for educational purposes only. Use responsibly and avoid violating any platform’s terms of service.  
