import numpy as np
from scipy.spatial.distance import cosine
from .face_utils import deserialize_embedding


def _ensure_array(vec):
    if vec is None:
        return None
    if isinstance(vec, (bytes, memoryview)):
        return deserialize_embedding(vec)
    return np.asarray(vec, dtype="float32")


def find_top_matches(source_embedding, queryset, top_k=5, threshold=0.4):
    results = []

    for obj in queryset:
        if not obj.face_embedding:
            continue

        target = deserialize_embedding(obj.face_embedding)
        score = 1 - cosine(source_embedding, target)

        if score >= threshold:
            results.append((score, obj))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_k]
