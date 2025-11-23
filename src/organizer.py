import os
import shutil
import sys

# Diccionario con extensiones comunes
FILE_TYPES = {
    "Fotos": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".md", ".csv", ".xls", ".xlsx", ".ppt", ".pptx", ".doc", ".docm", ".dot", ".dotx", ".dotm", ".odt", ".ott", ".rtf", ".pages", ".numbers", ".key"],
    "Musica": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".wma"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".wmv", ".flv", ".m4v", ".webm"],
    "Code": [".py", ".js", ".java", ".ts", ".cpp", ".cs", ".css", ".html", ".json", ".rb", ".go", ".rs", ".sql", ".xml", ".yaml"],
    "Comprimidos": [".zip", ".rar", ".7z"],
}

def get_folder_for_extension(ext):
    """Devuelve el nombre de carpeta según la extensión."""
    ext = ext.lower()
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Otros"


def organize_folder(path):
    """Organiza todos los archivos dentro del directorio dado."""

    if not os.path.isdir(path):
        print("La ruta ingresada no existe o no es un directorio.")
        return

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)

        # Evitar mover carpetas
        if os.path.isdir(file_path):
            continue

        # Obtener extensión
        _, ext = os.path.splitext(file_name)

        # Clasificar carpeta según extensión
        folder_name = get_folder_for_extension(ext)

        destination_folder = os.path.join(path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        # Mover archivo
        try:
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            print(f"Movido: {file_name} → {folder_name}/")

        except Exception as e:
            print(f"Error moviendo {file_name}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("python3 organizer.py <ruta-de-la-carpeta>")
        sys.exit(1)

    ruta = sys.argv[1]
    organize_folder(ruta)
