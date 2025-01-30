import os

def rename_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            if os.path.isfile(old_path):
                new_name = f"renamed_{file_name}"
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
        print("Redenumire finalizată cu succes.")
    except FileNotFoundError:
        print("Folderul specificat nu a fost găsit.")
    except PermissionError:
        print("Permisiune insuficientă pentru redenumirea fișierelor.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

def main():
    folder_path = input("Introduceți calea folderului: ").strip()
    rename_files_in_folder(folder_path)

if __name__ == "__main__":
    main()