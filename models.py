from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
import uuid


class DateTimeBaseModel(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)


class NameSlugBaseModel(BaseModel):
    name: str
    slug: Optional[str] = Field(None, max_length=50)

    @field_validator("slug", mode="before")
    def generate_slug(cls, v, values):
        return v or values["name"].replace(" ", "-").lower()


class Variety(DateTimeBaseModel, NameSlugBaseModel):
    pass


class Coffee(DateTimeBaseModel, NameSlugBaseModel):
    varieties: List[Variety] = Field(default_factory=list)
    cop_price: Decimal = Field(ge=0, description="Price in COP")
    usd_price: Optional[Decimal] = Field(None, ge=0, description="Price in USD")

    @field_validator("usd_price", mode="before")
    def convert_usd_price(cls, v, values):
        return v or values["cop_price"] / 4000
