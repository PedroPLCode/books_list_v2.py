"""empty message

Revision ID: a03181355309
Revises: d6fe8e1b4fc0
Create Date: 2024-03-10 20:25:23.930495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03181355309'
down_revision = 'd6fe8e1b4fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=100), nullable=True))
        batch_op.create_index(batch_op.f('ix_author_comment'), ['comment'], unique=False)

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=100), nullable=True))
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.create_index(batch_op.f('ix_book_comment'), ['comment'], unique=False)

    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=100), nullable=True))
        batch_op.alter_column('borrow_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('return_date',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.create_index(batch_op.f('ix_borrow_comment'), ['comment'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_borrow_comment'))
        batch_op.alter_column('return_date',
               existing_type=sa.String(length=100),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('borrow_date',
               existing_type=sa.String(length=100),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('comment')

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_comment'))
        batch_op.alter_column('date',
               existing_type=sa.String(length=100),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('comment')

    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_comment'))
        batch_op.drop_column('comment')

    # ### end Alembic commands ###
