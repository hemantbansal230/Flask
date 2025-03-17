from flask import Flask, render_template, request, redirect, session, url_for, flash
from models import User, Contact, Ticket, Cart
from app import app, db

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user'] = user.username
            return redirect('/')
        else:
            return render_template('login.html', error="Invalid credentials!")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error="Username already taken!")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/delete', methods=['POST'])
def delete_account():
    if 'user' not in session:
        return redirect('/login')

    user = User.query.filter_by(username=session['user']).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        session.pop('user', None)
        return redirect('/register')

    return redirect('/')

@app.route('/tickets')
def tickets():
    tickets = Ticket.query.all() or []  # Fetch tickets or default to an empty list
    return render_template('tickets.html', tickets=tickets)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    ticket_id = request.form['ticket_id']
    quantity = int(request.form['quantity'])

    # Check if the ticket is already in the cart
    cart_item = Cart.query.filter_by(ticket_id=ticket_id).first()
    if cart_item:
        cart_item.quantity += quantity  # Update the quantity
    else:
        cart_item = Cart(ticket_id=ticket_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return redirect(url_for('tickets'))

@app.route('/cart')
def cart():
    cart_items = Cart.query.all() or []  # Fetch cart items or default to an empty list
    detailed_cart = []
    for item in cart_items:
        ticket = Ticket.query.get(item.ticket_id)  # Fetch the associated ticket
        detailed_cart.append({
            'event_name': ticket.event_name,
            'price': ticket.price,
            'quantity': item.quantity
        })
    return render_template('cart.html', cart_items=detailed_cart)
@app.route('/delete-cart', methods=['POST'])
def delete_cart():
    db.session.query(Cart).delete()  # Delete all cart items
    db.session.commit()  # Save changes
    flash("Cart has been emptied!", "success")  # Show a message
    return redirect(url_for('cart'))  # Redirect back to the cart page