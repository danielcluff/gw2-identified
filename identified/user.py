from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from .auth import login_required
from .db import get_db
from .constants import stackable, unstacked, materials, sum_expressions

bp = Blueprint("user", __name__)


@bp.route("/")
def index():
    db = get_db()

    query_all = f"""
        SELECT rarity, {sum_expressions}
        FROM post
        WHERE rarity IN ("blue", "green", "rare")
        GROUP BY rarity
        ORDER BY CASE rarity
            WHEN "blue" THEN 1
            WHEN "green" THEN 2
            WHEN "rare" THEN 3
        End
    """
    allresults = db.execute(query_all).fetchall()
    allposts = {"blue": "null", "green": "null", "rare": "null"}

    for row in allresults:
        rarity = row["rarity"]
        # Only add data if any material has a value > 0
        if any(row[material] > 0 for material in materials):
            allposts[rarity] = dict(row)

    query = f"""
        SELECT rarity, {sum_expressions}
        FROM post
        WHERE rarity IN ("blue", "green", "rare")
        GROUP BY rarity
        ORDER BY CASE rarity
            WHEN "blue" THEN 1
            WHEN "green" THEN 2
            WHEN "rare" THEN 3
        End
    """
    results = db.execute(query).fetchall()
    posts = {"blue": "null", "green": "null", "rare": "null"}

    for row in results:
        rarity = row["rarity"]
        # Only add data if any material has a value > 0
        if any(row[material] > 0 for material in materials):
            posts[rarity] = dict(row)

    return render_template(
        "index.html", posts=posts, allposts=allposts, materials=stackable
    )


@bp.route("/user")
@login_required
def user():
    db = get_db()

    query = f"""
        SELECT rarity, {sum_expressions}
        FROM post
        WHERE rarity IN ("blue", "green", "rare")
        GROUP BY rarity
        ORDER BY CASE rarity
            WHEN "blue" THEN 1
            WHEN "green" THEN 2
            WHEN "rare" THEN 3
        End
    """
    results = db.execute(query).fetchall()
    posts = {"blue": "null", "green": "null", "rare": "null"}

    for row in results:
        rarity = row["rarity"]
        # Only add data if any material has a value > 0
        if any(row[material] > 0 for material in materials):
            posts[rarity] = dict(row)

    return render_template("user/index.html", posts=posts, materials=stackable)


@bp.route("/create", methods=("POST",))
@login_required
def create():
    def get_int_value(key):
        return int(request.form.get(key, 0) or 0)

    rarity = request.form["rarity"] or "green"
    values = {}

    for material in unstacked:
        values[material] = get_int_value(material)

    for material in stackable:
        values[material] = get_int_value(material)
        values[f"stack_{material}"] = get_int_value(f"stack_{material}")

    for material in stackable:
        stack_value = values[f"stack_{material}"]
        if stack_value > 0:
            values[material] += stack_value * 250

    if values["r_salvaged"] > values["rare"]:
        values["r_salvaged"] = 0
        values["r_ecto"] = 0

    if values["e_salvaged"] > values["exotic"]:
        values["e_salvaged"] = 0
        values["e_ecto"] = 0

    error = None

    if error is not None:
        flash(error)

    else:
        db = get_db()
        db.execute(
            "INSERT INTO post (author_id, rarity, " + ", ".join(materials) + ") "
            "VALUES (?, ?, " + ", ".join("?" * len(materials)) + ")",
            (g.user["id"], rarity) + tuple(values[material] for material in materials),
        )
        db.commit()
        return redirect(url_for("user.user"))


def get_post(id, check_author=True):
    post = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, f"post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("user.index"))
