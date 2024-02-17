# User Cache Kata

## Instructions
A User is composed of:
- firstName
- familyName
- age
- job
- address
- biography

1. We need to implement a UserRepository with 3 methods :
- getUser
- addUser
- updateUser
2. We’d like to add a cache for getUser method so that we don’t have to request real
UserRepository implementation (database or Rest based...) in case we try to retrieve
a same User several times in a row.
3. We can cache up to 10 different users.
