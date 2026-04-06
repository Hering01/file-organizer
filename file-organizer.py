import os
import shutil


def organize_files(folder_path):
    # Dateitypen definieren
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
    }

    # Durch alle Dateien gehen
    for filename in os.listdir(folder_path):

        # Nur Dateien – keine Ordner
        if os.path.isfile(os.path.join(folder_path, filename)):

            # Dateiendung herausfinden
            file_ext = os.path.splitext(filename)[1].lower()

            # In richtigen Ordner verschieben
            moved = False
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    # Ordner erstellen falls nicht vorhanden
                    dest_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)

                    # Datei verschieben
                    shutil.move(
                        os.path.join(folder_path, filename),
                        os.path.join(dest_folder, filename)
                    )
                    print(f"✅ {filename} → {folder_name}/")
                    moved = True
                    break

            if not moved:
                # Unbekannte Dateien
                other_folder = os.path.join(folder_path, 'Other')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(
                    os.path.join(folder_path, filename),
                    os.path.join(other_folder, filename)
                )
                print(f"📁 {filename} → Other/")


# Test
folder = input("Welchen Ordner möchtest du organisieren? ")
organize_files(folder)
print("\n🐟 Fertig! Deine Dateien wurden organisiert!")