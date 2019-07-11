from flask import Flask, request, redirect, render_template

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)





class Blog(db.Model):



    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))

    blogList = db.Column(db.Boolean)



    def __init__(self, name):

        self.name = name

        self.blogList = False





@app.route('/', methods=['POST', 'GET'])

def index():



    if request.method == 'POST':

        blog_name = request.form['blogTitle']

        new_blog = Blog(blog_name)

        db.session.add(new_blog)

        db.session.commit()



    blogs = Blog.query.filter_by(blogList=False).all()

    blog_list = Blog.query.filter_by(blogList=True).all()

    return render_template('todos.html',title="Build A Blog", 

        blogs=blogs, blog_list=blog_list)


#@app.route('/delete-blog', methods=['POST'])
#def delete_blog():
#    blog_id = int(request.form['blog-id'])
#    blog = Blog.query.get(blog_id)
#    blog.completed = True
#    db.session.add(blog)
#    db.session.commit()
#    return redirect('/')


if __name__ == '__main__':

    app.run()