# src/utils/file_handler.py
import os
import tempfile

def save_temp_file(uploaded_file, prefix="tmp"):
    suffix = os.path.splitext(uploaded_file.name)[1] if hasattr(uploaded_file, "name") else ".jpg"
    tmp = tempfile.NamedTemporaryFile(delete=False, prefix=prefix, suffix=suffix)
    tmp.write(uploaded_file.getbuffer())
    tmp.flush()
    tmp.close()
    return tmp.name

def cleanup_file(path):
    try:
        os.remove(path)
    except Exception:
        pass
