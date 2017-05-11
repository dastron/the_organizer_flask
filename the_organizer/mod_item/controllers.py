# Import flask dependencies
from flask import Blueprint, request, render_template, redirect
from flask import session as login_session
from flask_login import login_required
from ..webapp import database as db
from sqlalchemy import or_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound


# Import the database object from the main app module
from the_organizer.models import Item
from the_organizer.service import gcs

# Import module models (i.e. User)
# from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_items = Blueprint('items', __name__)
item_exist = ''
# Set the route and accepted methods


@mod_items.route('/items/', methods=['GET', 'POST'])
def items():

    query = request.args.get('q')

    try:
        item_exist = db.session.query(Item).filter(or_(
            Item.title.ilike('%' + query + '%'), Item.headline.ilike('%' + query + '%'), Item.description.ilike('%' + query + '%'))).all()

    except:
        print "Error"
        item_exist = db.session.query(Item).all()
        # print e

    return render_template('item.html', items=item_exist)


@mod_items.route('/items/create/', methods=['POST'])
@login_required
def items_create_post():
    print 'inpost'
    # Process Form Data

    # try:
    #     item_exist = db.session.query(Item).filter(
    #         Item.id == id).one()
    # except MultipleResultsFound, e:
    #     print e

    # except NoResultFound, e:
    #     print 'No Items'

    data = request.form
    print data

    title = data['title']
    headline = data['headline']
    description = data['description']
    url = data['url']
    amazon_url = data['amazon_url']
    user_id = data['user']
    image = data['image']
    amazon_url = data['amazon_url']
    thumbnail
    # I know this isn't the best option, I know importing current user is a
    # better method.

    try:
        print 'fail'
        item_exist = Item.add(user_id, title, headline,
                              description, 'primary_key', url, amazon_url)
        item_id = item_exist.insert()
        print item_id
        return redirect("/items/")
    except:
        print 'failed'
        return render_template('item_create.html', error=404)


@mod_items.route('/items/create/', methods=['GET'])
@login_required
def items_create():
    print 'outpost'
    return render_template('item_create.html')


@mod_items.route('/items/<id>/', methods=['GET', 'POST'])
def items_find(id):

    try:
        item_exist = db.session.query(Item).filter(
            Item.id == id).one()

    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'no user, create one'

    return render_template('item_view.html', item=item_exist)


@mod_items.route('/items/<id>/edit', methods=['POST'])
@login_required
def items_edit_post(id):
    print request.method
    print request.form
    # Process Form Data
    print request.form['title']

    try:
        item_exist = db.session.query(Item).filter(
            Item.id == id).one()
    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'No Items'

    data = request.form

    if data['title']:
        item_exist.title = data['title']
    if data['headline']:
        item_exist.headline = data['headline']
    if data['description']:
        item_exist.description = data['description']
    if data['url']:
        item_exist.url = data['url']
    if data['amazon_url']:
        item_exist.url = data['amazon_url']

    db.session.commit()

    return render_template('item_view.html', item=item_exist)


@mod_items.route('/items/<id>/edit', methods=['GET'])
@login_required
def items_edit(id):

    try:
        item_exist = db.session.query(Item).filter(
            Item.id == id).one()

    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'No Items'

    return render_template('item_edit.html', item=item_exist)


# Delete
@mod_items.route('/items/<id>/delete', methods=['GET', 'POST'])
@login_required
def items_delete(id):

    try:
        item_exist = db.session.query(Item).filter(
            Item.id == id).one()

    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'no user, create one'

    return render_template('item_view.html', item=item_exist)
