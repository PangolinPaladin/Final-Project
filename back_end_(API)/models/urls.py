from .base import Base

class Urls(Base, table=True): 
    __tablename__ = "urls"

    title: str
    long_url: str
    short_url: str
    user_id: int


    # this will be 
        # common name
        # scientific name
        # purchase date
        # condition 
        # purchase location
        
        # this is assuming I switch to a houseplant tracker, crops would 
        # be common name, family group, plant date, last maintained 

        # need to change both ends, so when it is called, both match 
        