import json


class File_Handling:
    def save_ing(self,l_objects :list):
        data={}
        for object_i in l_objects:
            object=object_i.__dict__
            data.update(object)
        json.dumps(data)




    def load_ing(self):
        pass

