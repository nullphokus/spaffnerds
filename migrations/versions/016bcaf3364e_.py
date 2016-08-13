"""empty message

Revision ID: 016bcaf3364e
Revises: 87f942232bcf
Create Date: 2016-02-02 21:38:17.627671

"""

# revision identifiers, used by Alembic.
revision = '016bcaf3364e'
down_revision = '87f942232bcf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('loc_address', sa.String(length=250), nullable=True),
    sa.Column('loc_city', sa.String(length=80), nullable=True),
    sa.Column('loc_state', sa.String(length=4), nullable=True),
    sa.Column('loc_zip', sa.String(length=80), nullable=True),
    sa.Column('latitude', sa.String(length=80), nullable=True),
    sa.Column('longitude', sa.String(length=80), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('loc_state', sa.String(length=4), nullable=True),
    sa.Column('loc_zip', sa.String(length=10), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('archive_id', sa.String(length=80), nullable=True),
    sa.Column('streamable', sa.Boolean(), nullable=True),
    sa.Column('song_performance_note', sa.Text(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('is_cover', sa.Boolean(), nullable=True),
    sa.Column('original_artist', sa.String(length=250), nullable=True),
    sa.Column('loc_city', sa.String(length=80), nullable=True),
    sa.Column('loc_state', sa.String(length=80), nullable=True),
    sa.Column('loc_zip', sa.String(length=80), nullable=True),
    sa.Column('latitude', sa.String(length=80), nullable=True),
    sa.Column('longitude', sa.String(length=80), nullable=True),
    sa.Column('set_desc', sa.String(length=80), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show_associations',
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show_associations')
    op.drop_table('songs')
    op.drop_table('shows')
    op.drop_table('venues')
    ### end Alembic commands ###