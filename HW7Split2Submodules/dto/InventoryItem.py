from .ItemOrigin import ItemOrigin
from pydantic import BaseModel

class InventoryItem(BaseModel):  #When defining data classes, also need to define type of data property in each data class. 
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin  # A nested Dataclass.