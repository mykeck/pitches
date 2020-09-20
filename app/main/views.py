from flask import render_template
from . import main

#Views
@main.route('/')
def index():
    all_posts = post.query.all()
    pickup_posts = post.query.filter_by(category = 'pickup_line').all()
    product_posts = post.query.filter_by(category = 'product').all()
    business_posts = post.query.filter_by(category = 'business').all()

    return render_template('index.html',all_posts = all_posts,pickup_posts =pickup_posts, product_posts = product_posts, business_posts)


@main.route('/user/')    

