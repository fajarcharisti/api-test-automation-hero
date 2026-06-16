from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# FEATURE FILE PATH
# =====================
FEATURES_PATH = BASE_DIR / "features" / "post_create.feature"


# =====================
# API ENDPOINT PATH
# =====================
POST_ENDPOINT_PATH = "/posts"