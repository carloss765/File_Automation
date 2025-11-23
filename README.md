# File Automation

Este es un script de Python simple para organizar automáticamente tus archivos en carpetas según sus extensiones (Fotos, Documentos, Música, Videos, Código, Comprimidos, etc.).

## Requisitos

- Python 3 instalado en tu sistema.

## Uso

Para usar la herramienta, ejecuta el script `organizer.py` pasando como argumento la ruta de la carpeta que deseas organizar.

### Comando

```bash
python3 src/organizer.py <ruta-de-la-carpeta>
```

### Ejemplo

Si quieres organizar tu carpeta de Descargas:

```bash
python3 src/organizer.py /Users/mi-usuario/Downloads
```

## Categorías soportadas

El script organizará los archivos en las siguientes carpetas:

- **Fotos**: .jpg, .jpeg, .png, .gif, .heic, .webp
- **Documentos**: .pdf, .docx, .txt
- **Musica**: .mp3, .wav, .aac, .flac, .m4a, .ogg, .wma
- **Videos**: .mp4, .mov, .mkv, .avi, .wmv, .flv, .m4v, .webm
- **Code**: .py, .js, .java, .ts, .cpp, .html, .css, etc.
- **Comprimidos**: .zip, .rar, .7z
- **Otros**: Cualquier otra extensión no listada.
