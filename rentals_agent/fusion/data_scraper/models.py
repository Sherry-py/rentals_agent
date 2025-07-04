from pydantic import BaseModel, HttpUrl

class RentalItem(BaseModel):
    address: str
    price: str
    bedrooms: str
    bathrooms: str
    area: str
    link: HttpUrl
    image: HttpUrl