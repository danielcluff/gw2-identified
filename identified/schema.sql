DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE post (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	author_id INTEGER NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	rarity TEXT NOT NULL,
	amount INTEGER NOT NULL DEFAULT 0,
	mithril INTEGER NOT NULL DEFAULT 0,
	oric INTEGER NOT NULL DEFAULT 0,
	elder INTEGER NOT NULL DEFAULT 0,
	ancient INTEGER NOT NULL DEFAULT 0,
	thick INTEGER NOT NULL DEFAULT 0,
	hardened INTEGER NOT NULL DEFAULT 0,
	silk INTEGER NOT NULL DEFAULT 0,
	gossamer INTEGER NOT NULL DEFAULT 0,
	lucentmote INTEGER NOT NULL DEFAULT 0,
	reclaimedmetal INTEGER NOT NULL DEFAULT 0,
	spain INTEGER NOT NULL DEFAULT 0,
	senhancement INTEGER NOT NULL DEFAULT 0,
	scontrol INTEGER NOT NULL DEFAULT 0,
	cskill INTEGER NOT NULL DEFAULT 0,
	cpotence INTEGER NOT NULL DEFAULT 0,
	cbrilliance INTEGER NOT NULL DEFAULT 0,
	luck10 INTEGER NOT NULL DEFAULT 0,
	luck50 INTEGER NOT NULL DEFAULT 0,
	luck100 INTEGER NOT NULL DEFAULT 0,
	luck200 INTEGER NOT NULL DEFAULT 0,
	rare INTEGER NOT NULL DEFAULT 0,
	exotic INTEGER NOT NULL DEFAULT 0,
	r_salvaged INTEGER NOT NULL DEFAULT 0,
	e_salvaged INTEGER NOT NULL DEFAULT 0,
	r_ecto INTEGER NOT NULL DEFAULT 0,
	e_ecto INTEGER NOT NULL DEFAULT 0,
	FOREIGN KEY (author_id) REFERENCES user (id)
);