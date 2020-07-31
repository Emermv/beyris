from flask import Flask, render_template, request, session,redirect, url_for,jsonify,make_response,send_from_directory
from core.Settings import APP_TITLE
from os import path
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='{{{',
        variable_end_string='}}}',
    ))

app = CustomFlask(__name__)
db=None
@app.template_filter("get")
def get(name):
    gl=globals()
    if name in gl:
     return globals()[name]

    return  ''
@app.route("/")
def index():
    return render_template("index.html",component="home")
@app.route("/<string:page>")
def page(page):
    if path.exists("templates/{}.html".format(page)):
        return render_template("{}.html".format(page),component=page)
    else:
        return render_template("404.html")

@app.route("/api/<string:api>")
@app.route("/api/<string:api>/<string:action>",methods=["GET","POST","DELETE"])
@app.route("/api/<string:api>/<string:action>/<string:args>",methods=["GET","PUT"])
def run_api(api,action="all",args=None):
    api_name=api.title()
    auto_api=__import__("api."+api_name,None,None,[api_name],0)
    auto_class=getattr(auto_api,api_name)
    instance=auto_class(db)
    
    result=None
    if(request.method=="DELETE"):
      result=instance.destroy(action)
    else:
        auto_action=getattr(instance,action)
        if(request.method=="PUT"):
          result=auto_action(args,request)
        elif(request.method=="POST"):
           result=auto_action(request)
        else:
           if args!=None:
              result=auto_action(args)
           else:
            result=auto_action()
  
    instance.set("state",True if result else False)
    instance.set("result",result)
    return jsonify(instance.toJSON())

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static",filename="favicon.ico")
if __name__=="__main__":
    app.run(debug=True)