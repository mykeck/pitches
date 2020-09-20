from flask import render_template
from . import main
from ..models import User
from flask_login import login_required, current_user


#Views
@main.route('/')
def index():
    all_posts = post.query.all()
    pickup_posts = post.query.filter_by(category = 'pickup_line').all()
    product_posts = post.query.filter_by(category = 'product').all()
    business_posts = post.query.filter_by(category = 'business').all()

    return render_template('index.html',all_posts = all_posts,pickup_posts =pickup_posts, product_posts = product_posts, business_posts)



# @main.route('/user/<uname>/update/pic',methods= [POST]) 
# @login_required
# def update_pic(uname):
#     User = User.query.filter_by(username = uname).first()if 'photo' in request.files:
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()

#     return redirect(url_for('main.profile',uname=uname))    



