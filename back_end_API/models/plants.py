from .base import Base

class Plants(Base): 
    __tablename__ = "Current_Plants"

    common_name: str
    scientific_name: str
    purchase_location: str
    purchase_date: int
    #date_of_purchase: int
    #current_condition: int


    # this will be 
        # common name
        # scientific name
        # purchase date
        # condition 
        # purchase location
        
        # this is assuming I switch to a houseplant tracker, crops would 
        # be common name, family group, plant date, last maintained 

        # need to change both ends, so when it is called, both match 
        