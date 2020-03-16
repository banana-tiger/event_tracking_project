"""create boilerplate migration

Revision ID: 7aef5033f225
Revises: 
Create Date: 2020-03-16 21:38:47.411930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '7aef5033f225'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'places',
        sa.Column('place_id', sa.BIGINT, primary_key=True),
        sa.Column('name', sa.Text),
    )

    op.create_table(
        'artists',
        sa.Column('artist_id', sa.BIGINT, primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column('is_alive', sa.Boolean),
    )

    op.create_table(
        'users',
        sa.Column('user_id', sa.BIGINT, primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column('place_id', sa.BIGINT, ForeignKey('places.place_id')),
    )

    op.create_table(
        'events',
        sa.Column('event_id', sa.BIGINT, primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column('place_id', sa.BIGINT, ForeignKey('places.place_id')),
    )

    op.create_table(
        'actings',
        sa.Column('acting_id', sa.BIGINT, primary_key=True),
        sa.Column('artist_id', sa.BIGINT, ForeignKey('artists.artist_id')),
        sa.Column('event_id', sa.BIGINT, ForeignKey('events.event_id')),
    )

    op.create_table(
        'subscriptions',
        sa.Column('acting_id', sa.BIGINT, primary_key=True),
        sa.Column('entity_type', sa.Text),
        sa.Column('entity_id', sa.BIGINT),
        sa.Column('user_id', sa.BIGINT, ForeignKey('users.user_id')),
    )

    op.create_table(
        'visit_plans',
        sa.Column('visit_plans_id', sa.BIGINT, primary_key=True),
        sa.Column('user_id', sa.BIGINT, ForeignKey('users.user_id')),
        sa.Column('event_id', sa.BIGINT, ForeignKey('events.event_id')),
        sa.Column('place_id', sa.BIGINT, ForeignKey('places.place_id')),
        sa.Column('aviasales_query', sa.Text),
        sa.Column('rzhd_query', sa.Text),
    )


def downgrade():
    tables_to_drop = ['visit_plans', 'subscriptions', 'actings', 'events', 'users', 'artists', 'places',]
    for table in tables_to_drop:
        op.drop_table(
            table,
        )
