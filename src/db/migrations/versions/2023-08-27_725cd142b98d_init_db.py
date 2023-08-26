"""Init db

Revision ID: 725cd142b98d
Revises:
Create Date: 2023-08-27 16:19:09.171377

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "725cd142b98d"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "theme",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__theme")),
    )
    op.create_index(op.f("ix__theme__name"), "theme", ["name"], unique=True)
    op.create_table(
        "user",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("role", sa.String(length=16), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__user")),
    )
    op.create_table(
        "consultant_request",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("status", sa.String(length=16), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk__consultant_request__user_id__user")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__consultant_request")),
    )
    op.create_index(
        op.f("ix__consultant_request__status"),
        "consultant_request",
        ["status"],
        unique=False,
    )
    op.create_index(
        op.f("ix__consultant_request__user_id"),
        "consultant_request",
        ["user_id"],
        unique=False,
    )
    op.create_table(
        "problem",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("description", sa.String(length=3000), nullable=False),
        sa.Column("consultant_id", sa.BigInteger(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["consultant_id"],
            ["user.id"],
            name=op.f("fk__problem__consultant_id__user"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk__problem__user_id__user")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__problem")),
    )
    op.create_index(
        op.f("ix__problem__consultant_id"), "problem", ["consultant_id"], unique=False
    )
    op.create_index(op.f("ix__problem__user_id"), "problem", ["user_id"], unique=False)
    op.create_table(
        "user_theme",
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("theme_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["theme_id"], ["theme.id"], name=op.f("fk__user_theme__theme_id__theme")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk__user_theme__user_id__user")
        ),
        sa.PrimaryKeyConstraint("user_id", "theme_id", name=op.f("pk__user_theme")),
    )
    op.create_index(
        op.f("ix__user_theme__theme_id"), "user_theme", ["theme_id"], unique=False
    )
    op.create_index(
        op.f("ix__user_theme__user_id"), "user_theme", ["user_id"], unique=False
    )
    op.create_table(
        "message",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("problem_id", sa.BigInteger(), nullable=False),
        sa.Column("from_user_id", sa.BigInteger(), nullable=False),
        sa.Column("to_user_id", sa.BigInteger(), nullable=False),
        sa.Column("content", sa.String(length=4000), nullable=False),
        sa.Column("is_delivered", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["from_user_id"], ["user.id"], name=op.f("fk__message__from_user_id__user")
        ),
        sa.ForeignKeyConstraint(
            ["problem_id"],
            ["problem.id"],
            name=op.f("fk__message__problem_id__problem"),
        ),
        sa.ForeignKeyConstraint(
            ["to_user_id"], ["user.id"], name=op.f("fk__message__to_user_id__user")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__message")),
    )
    op.create_index(
        op.f("ix__message__from_user_id"), "message", ["from_user_id"], unique=False
    )
    op.create_index(
        op.f("ix__message__problem_id"), "message", ["problem_id"], unique=False
    )
    op.create_table(
        "problem_theme",
        sa.Column("problem_id", sa.BigInteger(), nullable=False),
        sa.Column("consultant_id", sa.BigInteger(), nullable=True),
        sa.Column("theme_id", sa.BigInteger(), nullable=False),
        sa.Column("is_resolved", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["consultant_id"],
            ["user.id"],
            name=op.f("fk__problem_theme__consultant_id__user"),
        ),
        sa.ForeignKeyConstraint(
            ["problem_id"],
            ["problem.id"],
            name=op.f("fk__problem_theme__problem_id__problem"),
        ),
        sa.ForeignKeyConstraint(
            ["theme_id"], ["theme.id"], name=op.f("fk__problem_theme__theme_id__theme")
        ),
        sa.PrimaryKeyConstraint(
            "problem_id", "theme_id", name=op.f("pk__problem_theme")
        ),
    )
    op.create_index(
        op.f("ix__problem_theme__consultant_id"),
        "problem_theme",
        ["consultant_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix__problem_theme__problem_id"),
        "problem_theme",
        ["problem_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix__problem_theme__theme_id"), "problem_theme", ["theme_id"], unique=False
    )
    op.create_table(
        "review",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("problem_id", sa.BigInteger(), nullable=False),
        sa.Column("from_user_id", sa.BigInteger(), nullable=False),
        sa.Column("about_user_id", sa.BigInteger(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.String(length=3000), nullable=False),
        sa.ForeignKeyConstraint(
            ["about_user_id"], ["user.id"], name=op.f("fk__review__about_user_id__user")
        ),
        sa.ForeignKeyConstraint(
            ["from_user_id"], ["user.id"], name=op.f("fk__review__from_user_id__user")
        ),
        sa.ForeignKeyConstraint(
            ["problem_id"], ["problem.id"], name=op.f("fk__review__problem_id__problem")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk__review")),
    )
    op.create_index(
        op.f("ix__review__about_user_id"), "review", ["about_user_id"], unique=False
    )
    op.create_index(
        op.f("ix__review__from_user_id"), "review", ["from_user_id"], unique=False
    )
    op.create_index(
        op.f("ix__review__problem_id"), "review", ["problem_id"], unique=False
    )
    op.create_index(op.f("ix__review__rating"), "review", ["rating"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix__review__rating"), table_name="review")
    op.drop_index(op.f("ix__review__problem_id"), table_name="review")
    op.drop_index(op.f("ix__review__from_user_id"), table_name="review")
    op.drop_index(op.f("ix__review__about_user_id"), table_name="review")
    op.drop_table("review")
    op.drop_index(op.f("ix__problem_theme__theme_id"), table_name="problem_theme")
    op.drop_index(op.f("ix__problem_theme__problem_id"), table_name="problem_theme")
    op.drop_index(op.f("ix__problem_theme__consultant_id"), table_name="problem_theme")
    op.drop_table("problem_theme")
    op.drop_index(op.f("ix__message__problem_id"), table_name="message")
    op.drop_index(op.f("ix__message__from_user_id"), table_name="message")
    op.drop_table("message")
    op.drop_index(op.f("ix__user_theme__user_id"), table_name="user_theme")
    op.drop_index(op.f("ix__user_theme__theme_id"), table_name="user_theme")
    op.drop_table("user_theme")
    op.drop_index(op.f("ix__problem__user_id"), table_name="problem")
    op.drop_index(op.f("ix__problem__consultant_id"), table_name="problem")
    op.drop_table("problem")
    op.drop_index(
        op.f("ix__consultant_request__user_id"), table_name="consultant_request"
    )
    op.drop_index(
        op.f("ix__consultant_request__status"), table_name="consultant_request"
    )
    op.drop_table("consultant_request")
    op.drop_table("user")
    op.drop_index(op.f("ix__theme__name"), table_name="theme")
    op.drop_table("theme")
    # ### end Alembic commands ###