from model import db_connection
from helper import id_generator,paginated_results
from flask import Flask, request


class Contacts:
    def __init__(self):
        self.db=db_connection.Database()

    def record_exists(self,field,data):
        count = self.db.get_doc_count("contacts",field,data)
        if count:
            return True
        return False
        
    def generate_id(self):
        id = id_generator.ran_gen()
        while True:
            if self.record_exists("contact_id",id):
                id = id_generator.ran_gen()
            else:
                return id

    def create_contact(self,input):
        output ={"status": "" , "message" : ""}
        try:
            name=input['name']
            email=input['email']
            user=input['user']

            if self.record_exists("email",email):
                output["status"] = "error"
                output["message"] = "Email Exists"
            
            else:
                data_to_insert = {}
                data_to_insert['contact_id'] = self.generate_id()
                data_to_insert['name'] = name
                data_to_insert['email'] = email
                
                self.db.insert_one_data("contacts",data_to_insert)
                self.db.insert_one_to_array("users","user",user,"contacts",data_to_insert['contact_id'])
                output["status"] = "success"

        except:
            output["status"] = "success"

        return output

    def remove_contact(self,input):
        output ={"status": "" , "message" : ""}
        try:
            user=input['user']
            contact_id=input['contact_id']
            self.db.delete_one_from_array("users","user",user,"contacts",contact_id)
            output["status"] = "success"
        except :
            output["status"] = "error"

        return output
        

    def list_contact(self,input):   
        output ={"status": "" , "message" : ""}

        try:     
            try:
                page = int(request.args.get("page"))
            except:
                page = 1

            try:
                limit = int(request.args.get("limit"))
            except:
                limit = 10
                
            user=input['user']
            query={"user":user}
            contact_ids = self.db.get_values("users",query,["contacts"],["_id"])[0]['contacts']
        
            query={"contact_id":{"$in":contact_ids}}
            contacts = self.db.get_values("contacts",query,["contact_id","name","email"],["_id"])

            output["results"]= paginated_results.paginated_results(contacts,page,limit)
            output["status"] = "success"
        except:
            output["status"] = "error"

        return output

    def search_contact(self,input):
        output ={"status": "" , "message" : ""}

        try:
            search_string = input['search_string']
            output["results"] = self.db.search("contacts",search_string)
            output["status"] = "success"
        except:
            output["status"] = "error"

        return output

    def update_contact(self,input):
        output ={"status": "" , "message" : ""}

        try:
            fields_to_update = input['fields_to_update']
            contact_id = input['contact_id']
            
            new_fields = {}
            for field in fields_to_update:
                new_fields[field] = input[field]
            self.db.update_one("contacts","contact_id",contact_id,new_fields)   
            output["status"] = "success"
        except:
            output["status"] = "error"

        return  output


    def add_contacts(self,input):
        output ={"status": "" , "message" : ""}

        try:
            contact_ids = input['contact_ids']
            user=input['user']
            self.db.insert_many_to_array("users","user",user,"contacts",contact_ids) 
            output["status"] = "success"          
        except :
            output["status"] = "error"

        return output
