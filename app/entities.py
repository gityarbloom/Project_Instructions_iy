class Contact:
    def __init__(self, id:int=None , first_name:str, last_name:str, phone_number:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_dict(self):
        self = self.__dict__
        return self

# cont = Contact("211846894", "israel", "yarbloom", "053-5930755")
# print(cont.to_dict())

