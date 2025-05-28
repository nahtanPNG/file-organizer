# File Organizer 🗂️

A Python script that automatically organizes files in your computer by categories, moving them to appropriate directories based on their file extensions.

## Features ✨

- **Automatic categorization** - Sorts files by type (images, documents, videos, etc.)
- **Interactive menu** - Easy-to-use command-line interface
- **Dry run mode** - Preview changes before actually moving files
- **Flexible configuration** - Add custom categories and file types
- **Duplicate handling** - Automatically renames files if duplicates exist

## Default Categories 📁

| Category        | Extensions                          | Destination                          |
| --------------- | ----------------------------------- | ------------------------------------ |
| **Images**      | jpg, png, gif, svg, webp, bmp, tiff | `/home/nathan/Pictures`              |
| **Documents**   | pdf, doc, txt, xlsx, ppt, odt       | `/home/nathan/Documents`             |
| **Videos**      | mp4, avi, mkv, mov, wmv, flv        | `/home/nathan/Videos`                |
| **Audio**       | mp3, wav, flac, aac, ogg, m4a       | `/home/nathan/Music`                 |
| **Archives**    | zip, rar, 7z, tar, gz               | `/home/nathan/Downloads/Archives`    |
| **Executables** | exe, deb, rpm, dmg, pkg             | `/home/nathan/Downloads/Executables` |
| **Code**        | py, js, html, css, java, cpp        | `/home/nathan/Documents/Code`        |

## Installation 🚀

1. **Clone or download** the script:
   ```bash
   git clone https://github.com/nahtanpng/file-organizer
   ```

2. **Make sure you have Python 3.6+** installed:
   ```bash
   python3 --version
   ```

## Usage 💻

1. **Run the script**:
   ```bash
   python3 main.py
   ```

2. **Choose from the menu options**:
   - `1` - Organize files (moves files permanently)
   - `2` - Simulate organization (preview only)
   - `3` - View current configuration
   - `4` - Add new category
   - `5` - Exit

3. **Test first with simulation**:
   - Choose option `2`
   - Enter the directory path (e.g., `/home/nathan/Downloads`)
   - Review what would be moved
   - Then use option `1` to actually organize

## Configuration ⚙️

The script creates a `file_categories.json` configuration file that you can edit to:

- Add new file extensions to existing categories
- Create new categories
- Change destination directories
- Modify the organization structure

**Example configuration**:
```json
{
    "images": {
        "extensions": [".jpg", ".png", ".gif"],
        "destination": "/home/nathan/Pictures"
    },
    "documents": {
        "extensions": [".pdf", ".doc", ".txt"],
        "destination": "/home/nathan/Documents"
    }
}
```

## Safety Features 🛡️

- **Dry run mode** - Test before making changes
- **Duplicate protection** - Renames files to avoid overwrites
- **Error handling** - Continues processing even if some files fail
- **Detailed logging** - Shows exactly what happens to each file

## Customization 🔧

### Adding a New Category

Use the interactive menu (option 4) or manually edit `file_categories.json`:

```json
{
    "ebooks": {
        "extensions": [".epub", ".mobi", ".azw"],
        "destination": "/home/nathan/Documents/Books"
    }
}
```

### Changing User Path

Edit the default paths in the script or configuration file to match your username:
```
/home/your-username/Pictures
C:/Users/your-username/Pictures
```

## Requirements 📋

- Python 3.6 or higher

## License 📄

This project is open source and available under the MIT License.

## Contributing 🤝

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

**Built with ❤️ by [nahtanPNG](https://github.com/nahtanPNG)**

*Give this project a ⭐ if you found it helpful!*