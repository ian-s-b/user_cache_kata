import pytest

from user_repository.user import User
from user_repository.user_repository import UserRepository


@pytest.fixture
def repository():
    return UserRepository()


@pytest.fixture
def test_users():
    return [
        User("Test_name", "Test_last", 50, "TestJob", "100 Test address", "Test biography"),
        User("Test_name2", "Test_last2", 60, "TestJob2", "120 Test address", "Test biography 2"),
        User("Test_name3", "Test_last3", 60, "TestJob3", "140 Test address", "Test biography 3"),
        User("Test_name4", "Test_last4", 60, "TestJob4", "160 Test address", "Test biography 4"),
        User("Test_name5", "Test_last5", 70, "TestJob5", "180 Test address", "Test biography 5"),
        User("Test_name6", "Test_last6", 80, "TestJob6", "200 Test address", "Test biography 6"),
        User("Test_name7", "Test_last7", 90, "TestJob7", "220 Test address", "Test biography 7"),
        User("Test_name8", "Test_last8", 100, "TestJob8", "240 Test address", "Test biography 8"),
        User("Test_name9", "Test_last9", 110, "TestJob9", "260 Test address", "Test biography 9"),
        User("Test_name10", "Test_last10", 120, "TestJob10", "280 Test address", "Test biography 10"),
        User("Test_name11", "Test_last11", 120, "TestJob11", "300 Test address", "Test biography 11")
    ]


def test_user_procedures(repository, test_users) -> None:
    # Clean the cache
    repository.get_cache().clean_cache()

    # Add test data to the database
    repository.add_user(test_users[0])

    # Retrieve the user from the repository
    retrieved_added_user = repository.get_user((test_users[0].first_name, test_users[0].family_name))

    # Assert that the retrieved user matches the original user
    assert retrieved_added_user == test_users[0]

    # Update the user
    repository.update_user(test_users[1], (test_users[0].first_name, test_users[0].family_name))

    # Retrieve the user from the repository
    retrieved_updated_user = repository.get_user((test_users[1].first_name, test_users[1].family_name))

    # Assert that the retrieved user matches the updated user
    assert retrieved_updated_user == test_users[1]


def test_get_user_from_cache(repository, test_users):
    # Clean the cache
    repository.get_cache().clean_cache()

    # Create specific user
    cache_user = User("Cache", "User", 1, "TestJob", "100 Test address", "Test biography")

    # Add test data to the cache
    repository.get_cache().add_user(cache_user)

    # Retrieve the user from the repository
    retrieved_user = repository.get_user((cache_user.first_name, cache_user.family_name))

    # Assert that the retrieved user is from the cache
    assert retrieved_user == cache_user


def test_get_user_from_database(repository, test_users):
    # Clean the cache
    repository.get_cache().clean_cache()

    # Add test data to the database
    repository.get_database().add_user(test_users[3])

    # Retrieve the user from the repository
    retrieved_user = repository.get_user((test_users[3].first_name, test_users[3].family_name))

    # Assert that the retrieved user is from the database
    assert retrieved_user == test_users[3]


def test_cache_limit(repository, test_users):
    # Clean the cache
    repository.get_cache().clean_cache()

    # Add 10 users directly on the cache
    for user in test_users[:10]:
        repository.get_cache().add_user(user)

    # Add user on the database
    repository.add_user(test_users[-1])

    # Try to get the first used that was inserted on the cache
    retrieved_cache_user = repository.get_cache().get_user((test_users[0].first_name, test_users[0].family_name))

    # Assert that it was removed from the cache
    assert retrieved_cache_user is None

    # Assert that it is present on the database
    retrieved_db_user = repository.get_user((test_users[0].first_name, test_users[0].family_name))

    assert retrieved_db_user == test_users[0]
