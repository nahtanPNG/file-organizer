import os
import shutil
import json
from pathlib import Path
from typing import Dict, List

class FileOrganizer:
    def __init__(self, config_file: str = "file_categories.json"):
        self.config_file = config_file
        self.categories = self.load_or_create_config()
    
    def load_or_create_config(self) -> Dict:
        default_config = {
            "images": {
                "extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
                "destination": "/home/nathan/Pictures"
            },
            "documents": {
                "extensions": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
                "destination": "/home/nathan/Documents"
            },
            "videos": {
                "extensions": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
                "destination": "/home/nathan/Videos"
            },
            "audios": {
                "extensions": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
                "destination": "/home/nathan/Music"
            },
            "archives": {
                "extensions": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
                "destination": "/home/nathan/Downloads/Archives"
            },
            "executables": {
                "extensions": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".pkg"],
                "destination": "/home/nathan/Downloads/Executables"
            },
            "code": {
                "extensions": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb", ".go"],
                "destination": "/home/nathan/Documents/Code"
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Error reading {self.config_file}. Using default configuration.")
                return default_config
        else:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=4, ensure_ascii=False)
            print(f"Configuration file created: {self.config_file}")
            return default_config
    
    def get_file_category(self, file_path: str) -> str:
        file_extension = Path(file_path).suffix.lower()
        
        for category, config in self.categories.items():
            if file_extension in [ext.lower() for ext in config["extensions"]]:
                return category
        
        return "others"
    
    def create_directory(self, path: str) -> bool:
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory {path}: {e}")
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        try:
            # Check if the file already exists at destination
            if os.path.exists(destination):
                # If it exists, add a number to the name
                base, ext = os.path.splitext(destination)
                counter = 1
                while os.path.exists(f"{base}_{counter}{ext}"):
                    counter += 1
                destination = f"{base}_{counter}{ext}"
            
            shutil.move(source, destination)
            return True
        except Exception as e:
            print(f"Error moving {source} to {destination}: {e}")
            return False
    
    def organize_directory(self, source_dir: str, dry_run: bool = False):
        source_path = Path(source_dir)
        
        if not source_path.exists():
            print(f"Source directory not found: {source_dir}")
            return
        
        moved_files = 0
        skipped_files = 0
        error_files = 0
        
        print(f"{'[SIMULATION] ' if dry_run else ''}Organizing files in: {source_dir}")
        print("-" * 50)
        
        for file_path in source_path.iterdir():
            if file_path.is_file():
                category = self.get_file_category(str(file_path))
                
                if category == "others":
                    if "others" not in self.categories:
                        self.categories["others"] = {
                            "extensions": [],
                            "destination": "/home/nathan/Documents/Others"
                        }
                    destination_dir = self.categories["others"]["destination"]
                else:
                    destination_dir = self.categories[category]["destination"]

                destination_path = os.path.join(destination_dir, file_path.name)
                
                print(f"📁 {category.upper()}: {file_path.name}")
                
                if not dry_run:
                    if self.create_directory(destination_dir):
                        if self.move_file(str(file_path), destination_path):
                            moved_files += 1
                            print(f"   ✅ Moved to: {destination_path}")
                        else:
                            error_files += 1
                            print(f"   ❌ Error moving file")
                    else:
                        error_files += 1
                        print(f"   ❌ Error creating directory: {destination_dir}")
                else:
                    print(f"   🔄 Would be moved to: {destination_path}")
                    moved_files += 1
        
        print("\n" + "=" * 50)
        print("FINAL REPORT:")
        print(f"Files {'simulated' if dry_run else 'moved'}: {moved_files}")
        if not dry_run:
            print(f"Files with errors: {error_files}")
        print("=" * 50)
    
    def show_config(self):
        print("\n📋 CURRENT CONFIGURATION:")
        print("=" * 50)
        
        for category, config in self.categories.items():
            print(f"\n🏷️  CATEGORY: {category.upper()}")
            print(f"   📁 Destination: {config['destination']}")
            print(f"   📄 Extensions: {', '.join(config['extensions'])}")
    
    def add_category(self, name: str, extensions: List[str], destination: str):
        self.categories[name.lower()] = {
            "extensions": [ext if ext.startswith('.') else f'.{ext}' for ext in extensions],
            "destination": destination
        }
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.categories, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Category '{name}' added successfully!")