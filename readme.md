# 🌟 Opacity Script

## 📄 Description
This script allows you to modify the opacity of the default GNOME terminal profile. It uses the `dconf` command-line tool to read and write configuration settings.

## ✨ Features
- 🔍 Retrieve the UUID of the default GNOME terminal profile.
- 🎨 Update the opacity value of the terminal profile.

## 📋 Requirements
- 🐍 Python 3.x
- ⚙️ `dconf` command-line tool installed and accessible in your system.

## 📥 Installation
1. 📂 Clone this repository or copy the script to your local machine.
2. ✅ Ensure Python 3.x is installed on your system.
3. 🔧 Verify that the `dconf` tool is installed and properly configured.

## 🚀 Usage
1. 🖥️ Open a terminal.
2. ▶️ Run the script using Python:
    ```bash
    python3 opacity_script.py
    ```
3. 🎯 The script will automatically set the opacity of the default GNOME terminal profile to `0.85`.

## 🛠️ Code Overview
### 📜 Functions
- **`get_default_profile_uuid()`**: Retrieves the UUID of the default GNOME terminal profile.
- **`set_opacity(profile_uuid, opacity)`**: Updates the opacity value for the specified profile UUID.
- **`main()`**: Main function that orchestrates the retrieval and update process.

### 💻 Example
```python
def main():
     profile_uuid = get_default_profile_uuid()
     if profile_uuid:
          set_opacity(profile_uuid, 0.85)
```

## 📝 Notes
- ⚠️ Ensure you have the necessary permissions to modify GNOME terminal settings.
- 🔧 Adjust the opacity value in the script as needed (e.g., `0.85` for 85% opacity).

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## ⚠️ Disclaimer
This script modifies GNOME terminal settings. Use it at your own risk. Always back up your settings before making changes.
