#!/user/bin/env python3

def view_db(function):
    def wrapper(**kwargs):
        user = kwargs.get("user", {})
        if user["is_auth"] == False:
            print("You are not authorized to view the database.")
            return None
        else :
            print("You are authorized to view the database.")
            return function(**kwargs)
    return wrapper



if __name__== "__main__":
    user = {"name" : "humair" , "is_auth" : True}
    @view_db
    def get_db(**kwargs):
        print("Fetching database...")
        return {"data": "sample data"}
    get_db(user=user)



