import os.path

from werkzeug.utils import redirect, secure_filename

import random
from datetime import datetime, timedelta

from flask import Flask, render_template,request, session, Response, current_app, send_from_directory, url_for
app = Flask(__name__, static_folder='static',template_folder='templates',static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY']='7d441f27d441f27567d441f2b6176a'
import ar_master
mm = ar_master.master_flask_code()
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/customer_purchase",methods = ['GET' ,'POST'])
def customer_purchase():
    user=session['user']
    qry="select * from sales_details where username='"+str(user)+"'"
    data=mm.select_direct_query(qry)
    return render_template('customer_purchase.html',items=data)

@app.route("/farmer_home")
def farmer_home():
    return render_template('farmer_home.html')

@app.route("/customer_home"), z l̥   z  cc
def customer_home():
    return render_template('customer_home.html')

@app.route("/farmer_add_product")
def add_product():
    return render_template('farmer_add_product.html')

@app.route("/user_search_product_1")
def search_select():
    return render_template('user_search_product_1.html')

@app.route("/farmer",methods = ['GET' ,'POST'])
def farmer():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from farmer_details where user_name='" + str(un) + " ' and password='" + str(pa)+ "'")
        print(usern)
        if usern:
            session['user'] = un
            return render_template( 'farmer_home.html', flash_message=True,data="Login Success")
    return render_template('farmer.html')


@app.route("/customer",methods = ['GET' ,'POST'])
def customer():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from customer_details where user_name='" + str(un) + " ' and password='" + str(pa)+ "'")
        if usern:
            session['user'] = un
            return render_template( 'customer_home.html', flash_message=True,data="Login Success")
    return render_template('customer.html')

@app.route("/farmer_add_product",methods = ['GET','POST'])
def Add_Product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        discount= request.form['discount']
        discription = request.form['discription']
        maxin = mm.find_max_id("product_details")
        qq = "insert into product_details values('" + str(maxin) + "','" + str(product_name) + "','" + str(category) +"','" + str(price) +"','" + str(discount) +"','" + str(discription) +"')"
        mm.insert_query(qq)
        return render_template('farmer_add_product.html',flash_message=True,data="Registration Successfully")
    return render_template('farmer_add_product.html')

@app.route('/farmer_register',methods = ['GET','POST'])
def farmer_register():
    if request.method == 'POST':
        farmer_name = request.form['farmer_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        user_name = request.form['user_name']
        password = request.form['password']
        maxin = mm.find_max_id("farmer_details")
        qq = "insert into farmer_details values('" + str(maxin) + "','" + str(farmer_name) + "','" + str(contact) +"','" + str(email) +"','" + str(address) +"','" + str(user_name) +"','" + str(password)+"')"
        mm.insert_query(qq)
        return render_template('farmer_register.html',flash_message=True,data="Registration Successfully")
    return render_template('farmer_register.html')


@app.route('/customer_register',methods = ['GET','POST'])
def customer_register():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        user_name = request.form['user_name']
        password = request.form['password']
        maxin = mm.find_max_id("customer_details")
        qq = "insert into customer_details values('" + str(maxin) + "','" + str(customer_name) + "','" + str(contact) +"','" + str(email) +"','" + str(address) +"','" + str(user_name) +"','" + str(password)+"')"
        mm.insert_query(qq)
        return render_template('customer_register.html',flash_message=True,data="Registration Successfully")
    return render_template('customer_register.html')

@app.route("/customer_search",methods = ['GET','POST'])
def customer_search():
    qry="select * from product_details"
    if request.method == 'POST':
        data = request.form['data']
        qry = "select * from product_details where product_name='"+str(data)+"'"
    data=mm.select_direct_query(qry)
    return render_template('user_search_product.html',items=data)

@app.route("/user_search_product_1/<string:id>",methods=['GET','POST'])
def user_search_product_1(id):
    user=session['user']
    session['id']=id
    data=mm.select_direct_query("select * from product_details where id='"+str(id)+"'")
    return render_template('user_search_product_1.html',items=data)


@app.route("/user_search_product_2",methods=['GET','POST'])
def user_search_product_2():
    if request.method == 'POST':
        id=session['id']
        user=session['user']
        quantity = request.form['quantity']
        total = request.form['total']
        delivery= 'waiting'
        data=mm.select_direct_query("select * from product_details where id='"+ str(id) +"'")
        maxin = mm.find_max_id("sales_details")
        qq = ("insert into sales_details values('" + str(maxin) + "','"+ str(data[0][1])+ "','"+ str(data[0][2]) + "','"
              + str(data[0][3])+ "','"+ str(data[0][4])+ "','"+ str(user)+ "','"  + str(quantity)+"','" + str(total)+"','" + str(delivery)+"')")

        mm.insert_query(qq)
        return redirect(url_for("customer_search"))
    return render_template('user_search_product_2.html')

@app.route("/farmer_sales_details",methods = ['GET','POST'])
def farmer_sales_details():
    user =session['user']
    qry="select * from sales_details where username='"+str(user)+"' and delivery='waiting'"
    data=mm.select_direct_query(qry)
    return render_template('farmer_sales_details.html',items=data)


@app.route("/farmer_sales_details_1/<string:id>",methods=['GET','POST'])
def farmer_sales_details_1(id):
    user=session['user']
    query="update sales_details set delivery='delivered' where id='"+str(id)+"'"
    mm.insert_query(query)
    return redirect(url_for("farmer_sales_details"))

@app.route("/farmer_status")
def farmer_status():
    user = session['user']
    qry="select * from sales_details where username='"+str(user)+"' and delivery='delivered'"
    data=mm.select_direct_query(qry)
    return render_template('farmer_status.html',items=data)

if __name__ =='__main__':
    app.run(debug=True, use_reloader=True,port=5656)