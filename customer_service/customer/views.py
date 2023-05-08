import json

from django.http import HttpResponse
from django.shortcuts import render

from customer.models import Customer, Accout, FullName, Address


# Create your views here.
# This function is inserting the data into our table.
def data_insert(fname, lname, username ,email, mobile, password):
    fullname = FullName(fname,lname)
    accout = Accout(username,password)
    address = Address()
    user_data = Customer( email=email,accout=accout, mobile=mobile,fullname=fullname,address=address )
    user_data.save()
    return 1

def create_customer(request):
    # The Following are the input fields.
    fname = request.POST.get("First Name")
    lname = request.POST.get("Last Name")
    user = request.POST.get("User Name")
    email = request.POST.get("Email Id")
    mobile = request.POST.get("Mobile Number")
    password = request.POST.get("Password")
    cnf_password = request.POST.get("Confirm Password")
    resp = {}
    # In this if statement, checking that all fields are available.
    if fname and lname and email and mobile and password and cnf_password and user:
        # This will check that the mobile number is only 10 digits.
        if len(str(mobile)) == 10:
            # It will check that Password and Confirm Password both are the same.
            if password == cnf_password:
                # After all validation, it will call the data_insert function.
                respdata = data_insert(fname, lname, email, mobile, password)
                # If it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'User is registered Successfully.'
                # If it is not returning any value then the show will fail.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Unable to register user, Please try again.'
            # If the Password and Confirm Password is not matched then it will be through error.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Password and Confirm Password should be same'
        # If the mobile number is not in 10 digits then it will be through error.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Mobile Number should be 10 digit.'
    # If any mandatory field is missing then it will be through a failed message.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


