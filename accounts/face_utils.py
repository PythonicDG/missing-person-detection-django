import pickle
import numpy as np
import warnings

try:
    from deepface import DeepFace
    _DEEPFACE_AVAILABLE = True
except Exception:
    DeepFace = None
    _DEEPFACE_AVAILABLE = False

from PIL import Image


def extract_embedding(image_path):
    """Extract facial embedding from an image using DeepFace/ArcFace."""
    if not _DEEPFACE_AVAILABLE:
        warnings.warn("DeepFace is not available. Cannot extract embeddings.")
        return None
    try:
        result = DeepFace.represent(
            img_path=image_path,
            model_name="ArcFace",
            enforce_detection=True,
        )
        return np.array(result[0]["embedding"], dtype="float32")
    except Exception:
        return None


def serialize_embedding(embedding):
    """Convert a numpy embedding array to bytes for database storage."""
    if embedding is None:
        return None
    if isinstance(embedding, np.ndarray):
        return pickle.dumps(embedding)
    return pickle.dumps(np.array(embedding))


def deserialize_embedding(binary):
    """Restore a numpy embedding array from its binary representation."""
    if binary is None:
        return None
    if isinstance(binary, memoryview):
        binary = binary.tobytes()
    return pickle.loads(binary)
