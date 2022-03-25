DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS todo;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    text TEXT NOT NULL,
    createdOn TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user(username, password) VALUES ("sean", "pbkdf2:sha256:260000$oNJkw9ANgpDP5Alf$6b8ded9511a953efd23970b57bca297f1e922c8156844dec54eacaf4aced79f8");

INSERT INTO todo(username, text) VALUES ("beryl", "va faire la vaisselle");
INSERT INTO todo(username, text) VALUES ("sean", "flemme");