from app.core import config
from app import crud
from app.db.session import db_session
from app.schemas.farm import FarmCreate
from app.tests.utils.utils import random_lower_string


def test_create_delete_default_farm_with_token():
    """Leave the active flag unset. Test form correct system default flag."""

    farm_name = random_lower_string()
    url = random_lower_string()

    # Provide a token on creation
    token = {
        'access_token': random_lower_string(),
        'expires_in': random_lower_string(),
        'refresh_token': random_lower_string(),
        'expires_at': random_lower_string(),
    }

    farm_in = FarmCreate(
        farm_name=farm_name,
        url=url,
        token=token,
    )
    farm = crud.farm.create(db_session, farm_in=farm_in)
    assert farm.farm_name == farm_name
    assert farm.url == url

    if config.FARM_ACTIVE_AFTER_REGISTRATION:
        assert farm.active is True
    else:
        assert farm.active is False

    # Test that token was created
    assert farm.token is not None
    assert farm.token.access_token == token['access_token']
    assert farm.token.expires_at == token['expires_at']
    assert farm.token.refresh_token == token['refresh_token']
    assert farm.token.expires_in == token['expires_in']

    # Remove farm from DB
    crud.farm.delete(db_session, farm_id=farm.id)
    farm = crud.farm.get_by_id(db_session, farm_id=farm.id)
    assert farm is None


def test_create_delete_active_farm():
    """Configure the active flag to True."""

    farm_name = random_lower_string()
    url = random_lower_string()

    farm_in = FarmCreate(
        farm_name=farm_name,
        url=url,
    )
    farm = crud.farm.create(db_session, farm_in=farm_in)
    assert farm.farm_name == farm_name
    assert farm.url == url
    assert farm.token is None

    assert farm.active is True

    # Remove farm from DB
    crud.farm.delete(db_session, farm_id=farm.id)
    farm = crud.farm.get_by_id(db_session, farm_id=farm.id)
    assert farm is None


def test_create_delete_inactive_farm():
    """Configure the active flag to False."""

    farm_name = random_lower_string()
    url = random_lower_string()
    farm_in = FarmCreate(
        farm_name=farm_name,
        url=url,
        active=True,
    )
    farm = crud.farm.create(db_session, farm_in=farm_in)
    assert farm.farm_name == farm_name
    assert farm.url == url
    assert farm.active is True

    # Remove farm from DB
    crud.farm.delete(db_session, farm_id=farm.id)
    farm = crud.farm.get_by_id(db_session, farm_id=farm.id)
    assert farm is None


def test_create_delete_inactive_farm():
    """Configure the active flag to False."""

    farm_name = random_lower_string()
    url = random_lower_string()
    farm_in = FarmCreate(
        farm_name=farm_name,
        url=url,
        active=False,
    )
    farm = crud.farm.create(db_session, farm_in=farm_in)
    assert farm.farm_name == farm_name
    assert farm.url == url
    assert farm.active is False

    # Remove farm from DB
    crud.farm.delete(db_session, farm_id=farm.id)
    farm = crud.farm.get_by_id(db_session, farm_id=farm.id)
    assert farm is None
