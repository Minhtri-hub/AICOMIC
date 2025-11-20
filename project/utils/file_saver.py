import base64
from datetime import datetime
from io import BytesIO
from pathlib import Path

from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
GENERATED_DIR = BASE_DIR / "generated"
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def _build_filename() -> Path:
    now = datetime.utcnow()
    date_label = now.strftime("%d-%m-%Y")  
    pattern = f"*_{date_label}.png"
    existing_today = sorted(GENERATED_DIR.glob(pattern))
    counter = len(existing_today) + 1
    return GENERATED_DIR / f"{counter:02d}_{date_label}.png"


def save_image(base64_string: str) -> str:
    if not base64_string:
        raise ValueError("Missing base64 image data")

    if "," in base64_string:
        base64_string = base64_string.split(",", 1)[1]

    image_bytes = base64.b64decode(base64_string)
    with BytesIO(image_bytes) as buffer:
        image = Image.open(buffer)
        image = image.convert("RGBA")

        filename = _build_filename()
        image.save(filename, format="PNG")

    return str(filename.relative_to(BASE_DIR))
