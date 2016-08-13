"""empty message

Revision ID: cf888d3f2a72
Revises: 484fe0160426
Create Date: 2016-02-06 19:09:56.542664

"""

# revision identifiers, used by Alembic.
revision = 'cf888d3f2a72'
down_revision = '484fe0160426'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show_song_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('track_order', sa.Integer(), nullable=True),
    sa.Column('song_notes', sa.Text(), nullable=True),
    sa.Column('show_set', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id', 'show_id', 'song_id')
    )
    op.drop_table('show_song_assoc')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show_song_assoc',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('show_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('song_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('track_order', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('song_notes', mysql.TEXT(), nullable=True),
    sa.Column('show_set', mysql.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], [u'shows.id'], name=u'show_song_assoc_ibfk_1'),
    sa.ForeignKeyConstraint(['song_id'], [u'songs.id'], name=u'show_song_assoc_ibfk_2'),
    sa.PrimaryKeyConstraint('id', 'show_id', 'song_id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('show_song_link')
    ### end Alembic commands ###