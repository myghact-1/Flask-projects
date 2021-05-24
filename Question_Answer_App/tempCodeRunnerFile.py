if request.method == 'POST':
    #     db = get_db()
    #     name = request.form['name']
    #     hashed_password = generate_password_hash(
    #         request.form['password'], method='sha256')
    #     db.execute(''' insert into users (name, password, expert, admin) values (?,?,?,?)''',
    #                [name, hashed_password, '0', '0'])
    #     db.commit()
    #     return 'User Created'