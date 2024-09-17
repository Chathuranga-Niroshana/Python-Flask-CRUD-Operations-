pip install flask flask_restx flask_sqlalchemy flask_jwt_extended

<!-- for Config.py secrete key -->
pip install python_decouple

<!-- for env SECRETE KEY type -->
python
import secrets
secrets.token_hex(12)
<!-- copy coming token and save it as SECRET_KEY = d6aacd17859369cfc6ac66f8 -->


after 
<!-- 
@app.shell_context_processor
def make_shell_contex():
    return {"db": db, "Recipe": Recipe}
 -->
in terminal type
 set FLASK_APP=main.py
 flask --app main shell
 db
 Recipe
 db.create_all()


pip freeze > requirements.txt

pip instal flask_migrate

<!-- after creating user model -->
flask --app main db init
flask --app main db migrate -m "Initial migration."
flask --app main db upgrade


1. First install flask and line
2. Create Config file and env
3. Create main.py file
4. Create exts.py file
5. Create models.py file
