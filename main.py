from file_organizer import FileOrganizer

def main():
    organizer = FileOrganizer()
    
    while True:
        print("\n🗂️ FILE ORGANIZER")
        print("=" * 30)
        print("1. Organize files")
        print("2. Simulate organization (doesn't move files)")
        print("3. View current configuration")
        print("4. Add new category")
        print("5. Exit")
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            source_dir = input("Enter the directory path to organize: ").strip()
            if source_dir:
                organizer.organize_directory(source_dir, dry_run=False)
            else:
                print("❌ Invalid path!")
                
        elif choice == "2":
            source_dir = input("Enter the directory path to simulate: ").strip()
            if source_dir:
                organizer.organize_directory(source_dir, dry_run=True)
            else:
                print("❌ Invalid path!")
                
        elif choice == "3":
            organizer.show_config()
            
        elif choice == "4":
            name = input("Category name: ").strip()
            extensions = input("Extensions (comma separated): ").strip().split(',')
            extensions = [ext.strip() for ext in extensions]
            destination = input("Destination folder: ").strip()
            
            if name and extensions and destination:
                organizer.add_category(name, extensions, destination)
            else:
                print("❌ All fields are required!")
                
        elif choice == "5":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()