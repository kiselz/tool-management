DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tools;
DROP TABLE IF EXISTS tool_track;

-- Table for users
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT UNIQUE NOT NULL,
    admin_rights INTEGER NOT NULL
);

-- Table for tools
CREATE TABLE tools(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    toolname TEXT UNIQUE NOT NULL
);

-- Table for keeping track of tool's usage
CREATE TABLE tool_track(
    firstname TEXT NOT NULL,
    toolname TEXT NOT NULL,
    ammount INTEGER NOT NULL,
    FOREIGN KEY(firstname) REFERENCES users(firstname) ON DELETE CASCADE
    FOREIGN KEY(toolname) REFERENCES tools(toolname) ON DELETE CASCADE
);

INSERT INTO users(firstname, admin_rights) VALUES ('admin', 1);