from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
main=Flask(__name__)
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///code.db"
db=SQLAlchemy(main)

class codewith(db.Model):
          id: Mapped[int] = mapped_column(Integer, primary_key=True)
          Title: Mapped[str] = mapped_column(String,nullable=False)
          Description: Mapped[str] = mapped_column(String)

with main.app_context():
    db.create_all()


@main.route("/home")
def home():
    return render_template("home.html")
@main.route("/saveData", methods=["POST"])
def savedata():
    if request.method == "POST":
        Title = request.form.get("title")
        Description = request.form.get("description")

    save = codewith(Title = Title, Description = Description)
    db.session.add(save)
    db.session.commit()

    return redirect("/showdata")
@main.route("/showdata")
def showdata():
    data = codewith.query.all()
    print(data, "xxxxxxxxxxxxxx")
    return render_template("showdata.html",alldata=data)

@main.route("/deletedata/<int:x>", methods=["POST"])
def delete(x):
    zx = codewith.query.filter(codewith.id == x).first()
    zx.title = "this is update title"
    # db.session.delete(zx)
    db.session.commit()
    return redirect("/showdata")

@main.route("/update/<int:x>",methods=["POST"])
def update(x):
     x=codewith.query.get(x)
     db.session.commit()
     return render_template("update.html",alldata=x)
if __name__=="__main__":
    main.run(debug=True)