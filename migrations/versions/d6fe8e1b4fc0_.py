"""empty message

Revision ID: d6fe8e1b4fc0
Revises: 
Create Date: 2024-03-07 22:31:26.208446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6fe8e1b4fc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_name'), ['name'], unique=True)

    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_title'), ['title'], unique=False)

    op.create_table('borrow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('borrower', sa.String(length=100), nullable=True),
    sa.Column('borrow_date', sa.DateTime(), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_borrow_borrow_date'), ['borrow_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_borrow_borrower'), ['borrower'], unique=False)
        batch_op.create_index(batch_op.f('ix_borrow_return_date'), ['return_date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrow', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_borrow_return_date'))
        batch_op.drop_index(batch_op.f('ix_borrow_borrower'))
        batch_op.drop_index(batch_op.f('ix_borrow_borrow_date'))

    op.drop_table('borrow')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_title'))
        batch_op.drop_index(batch_op.f('ix_book_date'))

    op.drop_table('book')
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_name'))

    op.drop_table('author')
    # ### end Alembic commands ###
