from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://academia:QCE28hb4006kRAP4@cluster0.wxzv8sd.mongodb.net/?retryWrites=true&w=majority"

def get_db():
    mongodb_client = MongoClient(MONGODB_URL)
    
    return mongodb_client["academia"]

def insert(items: list):
    database = get_db()
    
    for item in items:
        database.inventory.insert_one(item)
        
def get():
    database = get_db()
    
    for item in database.inventory.find():
        print(item)                            
              
def delet():
    database = get_db()
    result = database.inventory.delete_one({"name": "Tenedor"})
    
    if result.deleted_count > 0:
        print("Registro eliminado")
    else:
        print("Registro no encontrado")
        
def edit(filter_query: dict, update_query: dict): 
    database = get_db()
    result = database.inventory.update_one(filter_query, {"$set": update_query})
    
    if result.modified_count > 0:
        print("Registro editado")
    else:
        print("Registro no encontrado")
        
# insert([
#     {
#         "name": "Tenedor",
#         "category": "Cocina",
#         "quantity": 20,
#         "price": 5,
#     },
#     {
#         "name": "Cuchara",
#         "category": "Cocina",
#         "quantity": 10,
#         "price": 3,
#     },
#     {
#         "name": "Papel",
#         "category": "Blancos",
#         "quantity": 50,
#         "price": 15,
#     }
# ])

filter_query = {"name": "Cuchillo"}
update_query = {"name": "Tenedor"}

# delet()
# edit(filter_query, update_query)
get()