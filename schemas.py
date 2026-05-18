from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Any, Optional

class KeyFeature(BaseModel):
    title: str
    value: str

class PropertyCreate(BaseModel):
    title: str
    price: str
    category: str
    key_features: List[KeyFeature]
    description: str
    property_for: Optional[str] = None
    sqft: Optional[str] = None
    address: str
    city: str
    zip_code: str
    map_url: Optional[str] = None
    media_files: List[Dict[str, Any]]
    owner_name: str
    contact_number: str
    amenities: List[str]
    dynamic_fields: Optional[Dict[str, Any]] = None

class PropertyResponse(PropertyCreate):
    id: int
    bgm_id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    bio: str
    profile_picture_url: Optional[str] = None

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class VisitorBase(BaseModel):
    name: str
    phone: str
    interested_in: Optional[str] = None
    property_type: Optional[str] = None
    budget_min: Optional[str] = None
    budget_max: Optional[str] = None
    description: Optional[str] = None
    created_at_date: str
    created_at_time: str

class VisitorCreate(VisitorBase):
    pass

class VisitorResponse(VisitorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
