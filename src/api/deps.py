from fastapi import Depends, HTTPException, status

from jose import jwt, JWTError
from sqlalchemy.orm import Session
from src.core import security
from src.db.session import get_db
from src.crud import crud_user
from src.models.user import User

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

reusable_oauth2 = HTTPBearer()

def get_current_user(
    db: Session = Depends(get_db), 
    token: HTTPAuthorizationCredentials = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token.credentials, security.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud_user.get(db, user_id=int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
