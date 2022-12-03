from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from azure.core.credentials import AzureNamedKeyCredential
from azure.data.tables import TableServiceClient
from azure.data.tables import TableClient
from azure.data.tables import UpdateMode
import json
import random


app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/api/noParts', methods=['POST'])
def noParts():
    #print('helo'+request.args['data'])
    entity1 = {
                    u"PartitionKey": u"11",
                    u"RowKey": u"11",
                    u"PartDesc": "",
                    u"Partno": u"",
                }
    table_client = TableClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=speakbot8128;AccountKey=G8RWdFUuFqouE4gf5bBTfNjMaq/AScSPLUYg1g83yqQw8/zmFAWTS+2L769vo9CjE4tnCZ+MenzRbPJ8OHOgXQ==;EndpointSuffix=core.windows.net", table_name="IoTParts")
    table_client.update_entity(mode=UpdateMode.REPLACE, entity=entity1)
    return "1"

@app.route('/api/updateParts', methods=['POST'])
def updateParts():
    #print('helo'+request.args['data'])
    content_1=json.loads(request.data)
    entity1 = {
                    u"PartitionKey": u"11",
                    u"RowKey": u"11",
                    u"PartDesc": content_1["data"],
                    u"Partno": u"",
                }
    table_client = TableClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=speakbot8128;AccountKey=G8RWdFUuFqouE4gf5bBTfNjMaq/AScSPLUYg1g83yqQw8/zmFAWTS+2L769vo9CjE4tnCZ+MenzRbPJ8OHOgXQ==;EndpointSuffix=core.windows.net", table_name="IoTParts")
    table_client.update_entity(mode=UpdateMode.REPLACE, entity=entity1)
     
    return "1"
@app.route('/api/getParts', methods=['GET'])
def getParts():
    #print('helo'+request.args['data'])
    data_content=[]
    my_filter = "IsPart eq true"
    table_client = TableClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=speakbot8128;AccountKey=G8RWdFUuFqouE4gf5bBTfNjMaq/AScSPLUYg1g83yqQw8/zmFAWTS+2L769vo9CjE4tnCZ+MenzRbPJ8OHOgXQ==;EndpointSuffix=core.windows.net", table_name="IoTParts")
    entities = table_client.query_entities(my_filter)
    created = table_client.get_entity(partition_key="11", row_key="11")
    print(created)
    try:
        data_content=json.loads(created["PartDesc"])
    except:
        data_content=json.loads("[{\"Partno\":\"No Parts available\",\"PartDesc\":\"\"}]")
     
    return json.dumps(data_content)   
    #return render_template('form.html', data=1,project=1,userid=1,q=request.form['text'],pathcontent=1,resultcontent=1,filextensions=1,filepath=1,sppath=1,previewpath=1,processname=1)    
@app.route('/showParts')
def showParts():
    print('helo')   
    data=["hello","hello2","hello3"]
    data_content=[]
    my_filter = "IsPart eq true"
    table_client = TableClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=speakbot8128;AccountKey=G8RWdFUuFqouE4gf5bBTfNjMaq/AScSPLUYg1g83yqQw8/zmFAWTS+2L769vo9CjE4tnCZ+MenzRbPJ8OHOgXQ==;EndpointSuffix=core.windows.net", table_name="IoTParts")
    entities = table_client.query_entities(my_filter)
    created = table_client.get_entity(partition_key="11", row_key="11")
    print(created)
    try:
        data_content=json.loads(created["PartDesc"])
    except:
        data_content=json.loads("[{\"Partno\":\"No Parts available\",\"PartDesc\":\"\"}]")
    print("content partno")
    print(type(data_content))
    #for entity in entities:
        #data_content.append({"PartDesc":entity["PartDesc"]})
        #for key in entity.keys():
    return render_template('Parts.html',data=data_content)
@app.route('/home')
def loadYT_home():
    return render_template('home.html')
@app.route('/loadYT/<no>')
def loadYT(no):
    if(no!=""): 
        with open('data'+no+'.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)
    else:
        with open('data0.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)
    return render_template('loadview.html',data=datacontent,videono=no)

@app.route('/loadYT/test/<no>')
def test(no):
    with open('test.json', encoding='utf8') as datafile:
        datacontent = json.loads(datafile.read())
        print(datacontent)
    return render_template('test.html',data=datacontent,videono=no)  

@app.route('/loadYT/mobile/<no>')
def loadYT_mobile(no): 
    if str(no)!="": 
        with open('data'+no+'.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)
    else:
        with open('data0.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)
    return render_template('loadview_m.html',data=datacontent,videono=no)  


@app.route('/loadYT_view/<videono>/<no>', methods=['GET'])
def loadYT_view(videono,no): 
    if(no!=""): 
        with open('data'+no+'.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)
    else:
        with open('data0.json', encoding='utf8') as datafile:
            datacontent = json.loads(datafile.read())
            print(datacontent)

    return render_template('loadvideo.html',data=datacontent,count=videono,videoprop=datacontent["videos"][int(videono)])    

@app.route('/loadYT_test/<videono>/<no>', methods=['GET'])
def loadYT_test(videono,no): 
    with open('test.json', encoding='utf8') as datafile:
        datacontent = json.loads(datafile.read())
        print(datacontent)

    return render_template('loadvideotest.html',data=datacontent,count=videono,videoprop=datacontent["videos"][int(videono)])  

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)