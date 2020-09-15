from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo

from functions.getNumberPlate import getNumPlate, random_with_N_digits
from functions.timeFunc import getTime
from theBank import canPay

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI = 'mongodb+srv://dbUser:3lq8Df5UK2SWOacN@cluster0.dght0.gcp.mongodb.net/cluster0?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    vehicleCollection = mongo.db.vehicles
    parking = mongo.db.price

    vehicleNum = vehicleCollection.estimated_document_count()

    doc = parking.find_one()
    parkingPrice = doc['value']

    return render_template('index.html', vhCount=vehicleNum, amount=parkingPrice)

@app.route('/api/201', methods=['GET','POST'])
def addVehicle():
    vehicleCollection = mongo.db.vehicles
    parking = mongo.db.price

    doc = parking.find_one()
    parkingPrice = doc['value']

    value = random_with_N_digits(3)
    LP = getNumPlate()
    toSend = '(' + LP + ')' + ' has entered the garage'

    vehicleCollection.insert_one({
        'License Plate' : LP,
        'Bank Account' : value,
        'Time Stamp': getTime()
    })
    vehicleNum = vehicleCollection.estimated_document_count()
    return render_template('index.html', toUpdate=toSend, vhCount=vehicleNum, amount=parkingPrice)

    # return redirect('/?api/200')

# Change Parking Price ########################
@app.route('/api/201p', methods=['GET','POST'])
def changePrice():
    toChange = request.form['amount']
    print(toChange)
    price = mongo.db.price
    query = price.find_one()

    price.delete_one(query)

    price.insert_one({
        'value' : toChange
    })
    return redirect('/?api/201p')

# Remove vehicle #############################
@app.route('/api/204', methods=['GET','POST'])
def remVehicle():
    vehicleCollection = mongo.db.vehicles
    price = mongo.db.price

    vehicleCollection = mongo.db.vehicles
    parking = mongo.db.price
    vehicleNum = vehicleCollection.estimated_document_count()
    doc = parking.find_one()
    parkingPrice = doc['value']

    query = vehicleCollection.find_one()
    priceMin = price.find_one()

    if query:
        licensePlate = query['License Plate']
        amountHave = query['Bank Account']
        timeIn = query['Time Stamp']
        payMin = priceMin['value']

        ispayable = canPay(amountHave, timeIn, payMin)

    if ispayable == True:
        vehicleCollection.delete_one(query)   
        vehicleNum = vehicleCollection.estimated_document_count()
        toSend = '(' + licensePlate + ')' + ' was allowed to leave.'
        
        return render_template('index.html', toUpdate=toSend, vhCount=vehicleNum, amount=parkingPrice)

    if ispayable == False:
        toSend = '(' + licensePlate + ')' + ' was not allowed to leave.'
        
        return render_template('index.html', toUpdate=toSend, vhCount=vehicleNum, amount=parkingPrice)
    return redirect('/?api/204')

# if __name__ == "__main__":
#     app.run(debug=True)
