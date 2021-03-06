"""missing column artist_id

Revision ID: 9deb48daf229
Revises: b4239834d575
Create Date: 2020-05-02 02:27:31.815098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9deb48daf229'
down_revision = 'b4239834d575'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('artist_id', sa.Integer(), nullable=True))
    with op.batch_alter_table("event") as b_op:
        b_op.create_foreign_key("fk_event_artist_id_artists", 'artists', ['artist_id'], ['artist_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'artist_id')
    with op.batch_alter_table("event") as b_op:
        b_op.drop_constraint("fk_event_artist_id_artists", type_='foreignkey')
    # ### end Alembic commands ###
