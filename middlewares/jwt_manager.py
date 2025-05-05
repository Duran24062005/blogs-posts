from jwt import decode, encode, PyJWTError

def create_jwt_token(data: dict):
    """
    Create a JWT token with the given data and secret key.
    """
    algorithm = "HS256"
    secret = "your_secret_key"  # Replace with your actual secret key
    try:
        token:str = encode(data, key=secret, algorithm=algorithm)
        return token
    except PyJWTError as e:
        raise Exception(f"Error creating JWT token: {str(e)}")
    
def decode_jwt_token(token: str):
    """
    Decode a JWT token and return the payload.
    """
    algorithm = "HS256"
    secret = "your_secret_key"  # Replace with your actual secret key
    try:
        payload = decode(token, key=secret, algorithms=[algorithm])
        return payload
    except PyJWTError as e:
        raise Exception(f"Error decoding JWT token: {str(e)}")