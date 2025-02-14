from flask import *
from database import *



admin=Blueprint('admin',__name__)

@admin.route("/adminhome")
def adminhome():
    return render_template("admin.html")

@admin.route("/viewseller")
def viewseller():
    data={}
    qur="select * from seller"
    a=select(qur)
    data['view']=a

    if 'action' in  request.args:
        action=request.args['action']
        sellid=request.args['id']

    else:
        action=None

    if action=='approve':
        qry="update seller set status='approved' where seller_id='%s' "%(sellid)
        update(qry)

    if action=='reject':
        qry="update seller set status='rejected' where seller_id='%s' "%(sellid)
        update(qry)
    
    return render_template("view_seller.html",data=data)

@admin.route("/viewuser")
def viewuser():
    data={}
    qur="select * from user"
    ab=select(qur)
    data['view']=ab
    return render_template("view_user.html",data=data)

@admin.route("/viewauction")
def viewauction():
    data={}
    qur="select * from auction"
    ab=select(qur)
    data['view']=ab
    return render_template("view_auction.html",data=data)

@admin.route("/viewcomplaints")
def viewcomplaints():
    data={}
    qur="select * from complaints"
    ab=select(qur)
    data['view']=ab
    return render_template("view_complaints.html",data=data)


@admin.route("/send_reply")
def send_reply():
    
    return render_template("send_reply.html")

