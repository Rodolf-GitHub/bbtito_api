from __future__ import annotations

from io import BytesIO

from django.core.files.base import ContentFile


def compress_image(uploaded_file, max_size_kb: int = 100, quality: int = 85) -> ContentFile:
	"""
	Comprime una imagen y retorna un ContentFile listo para asignar a ImageField.
	max_size_kb: tamaño máximo en KB (por defecto 1024 KB = 1 MB)
	"""
	try:
		from PIL import Image
	except Exception:
		# Si Pillow no está disponible, devuelve el archivo original sin modificar
		return uploaded_file

	max_size_bytes = max_size_kb * 1024

	image = Image.open(uploaded_file)
	if image.mode in ("RGBA", "LA"):
		image = image.convert("RGB")

	buffer = BytesIO()
	current_quality = quality

	image.save(buffer, format="JPEG", optimize=True, quality=current_quality)

	while buffer.tell() > max_size_bytes and current_quality > 20:
		current_quality -= 10
		buffer = BytesIO()
		image.save(buffer, format="JPEG", optimize=True, quality=current_quality)

	file_name = getattr(uploaded_file, "name", "imagen.jpg")
	return ContentFile(buffer.getvalue(), name=file_name)
