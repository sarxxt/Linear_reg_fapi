from pydantic import BaseModel, field_validator

class DataNote(BaseModel):
    petal_length: float

    @field_validator("petal_length")
    def validate_acc_id(cls, value):
        if value <=0.0:
            raise ValueError(f"petal length should be positive: {value}")
        return value



    
