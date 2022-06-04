import json
from flask import Flask, abort
from about_me import me
from mock_data import catalog

app = Flask('class2python')

@app.route("/", methods=['GET']) #root
def home():
    return "This is the home page"

#Create an about endpoint and show your name

@app.route("/about") 
def about():
    return me["first"] + " " + me["last"]

@app.route("/myaddress")
def address():
    return f'{me["address"]["street"]} {me["address"]["number"]}'


 ########################################################### API ENDPOINTS################################################################################################################################

 # Postman -> Test endpoints of REST APIs

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count", methods=["GET"])
def get_count():

    #Here... count how many products are in the list catalog
    counts = len(catalog)
    return json.dumps(counts) #return the value

#Request 127.0.0.1:5000/api/product/
@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    # find the product whose _id is equal to id
    # catalog
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    # travel catalog with for loop
    # Get the product inside the list
    # if the _id of the product is equal to th id variable
    # found it, return that product as json
    return abort(404, "Id does not match any product")





# Create an endpoint that returns the sum of all the products' price
# GET /api/catalog/total
#@app.route('/api/catalog/total', methods=['GET'])
@app.get("/api/catalog/total")
def get_total():

    total = 0
    for prod in catalog:
       # total = total + prod["price"]
       total += prod["price"]

    return json.dumps(total)

# get product by category
# get /api/products/<category>
@app.get("/api/products/<category>")
def products_by_category(category):
    results = []
    for prod in catalog:
        if prod["category"] == category:
            results.append(prod)

            return json.dumps(results)

# get the list of categories
# get /api/categories
@app.get("/api/categories")
def get_unique_categories():
    results[]
    for prod in catalog:
        cat = prod["category"]
        # if cat does not exist in results, then
        if not cat in results:
            results.append(cat)

    return json.dumps(results)





    # get the cheapest product
@app.get("/api/product/cheapest")
def get_cheapest_product():
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)






app.run(debug=True)