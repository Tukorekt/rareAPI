from datetime import datetime, timedelta, timezone
import uuid
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS

def _create_token(sub: str, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(sub),           # кто (user_id)
        "iat": now,                # issued at
        "exp": now + expires_delta,# expiration
        "jti": str(uuid.uuid4()),  # уникальный id токена (для отзыва)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_token(user_id: int) -> str:
    return _create_token(user_id, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        raise ValueError("Invalid token") from e