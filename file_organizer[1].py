import os
import shutil
import logging

# Configure logging
logging.basicConfig(filename="file_organizer.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Define file categories
FILE_CATEGORIES = {
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov'],
}

def create_folder(path):
    """Create folder if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created folder: {path}")

def organize_files(target_dir):
    """Organize files in the target directory."""
    try:
        if not os.path.exists(target_dir):
            print("Target directory does not exist!")
            return

        # Create category folders
        for category in FILE_CATEGORIES.keys():
            create_folder(os.path.join(target_dir, category))
        create_folder(os.path.join(target_dir, "Others"))

        # Scan and move files
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                moved = False

                for category, extensions in FILE_CATEGORIES.items():
                    if ext.lower() in extensions:
                        shutil.move(file_path, os.path.join(target_dir, category, filename))
                        logging.info(f"Moved {filename} to {category}")
                        moved = True
                        break

                if not moved:
                    shutil.move(file_path, os.path.join(target_dir, "Others", filename))
                    logging.info(f"Moved {filename} to Others")

        print("Files organized successfully!")
        logging.info("File organization completed successfully.")

    except Exception as e:
        logging.error(f"Error organizing files: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")
    organize_files(target_directory)
