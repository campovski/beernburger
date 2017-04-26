CREATE TABLE country (
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE manufacturer (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	country INTEGER REFERENCES country NOT NULL
);

CREATE TABLE beer (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	review TEXT NOT NULL,
	grade_taste CHAR(1) NOT NULL,
	grade_color CHAR(1) NOT NULL,
	grade_smell CHAR(1) NOT NULL,
	grade_smoothness CHAR(1) NOT NULL,
	grade_foam CHAR(1) NOT NULL,
	grade_total CHAR(1) NOT NULL,
	alc TEXT,
	image TEXT NOT NULL,
	manufacturer INTEGER REFERENCES manufacturer NOT NULL
);

CREATE TABLE burger (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	grade CHAR(1) NOT NULL,
	review TEXT NOT NULL,
	manufacturer INTEGER REFERENCES manufacturer NOT NULL
);
