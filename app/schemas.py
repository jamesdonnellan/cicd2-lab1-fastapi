from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints

class UserCreate(BaseModel):
    user_id: int = Field(gt=0) #must be an integer greater than 0
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)] # Must be a string between 2 and 50 characters, has to follow validation rules. 
    email: EmailStr # Must be a valid email address. 
    age: int = Field(gt=18, lt=120) # Must be greater than 18 and less than 120. 
    student_id: Annotated[str, StringConstraints(pattern=r"^S\d{7}$")] # Must start with S followed by exactly 7 digits, for example S1234567. 