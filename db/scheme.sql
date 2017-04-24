CREATE TABLE country (
	id SERIAL PRIMARY KEY,
	name TEXT
);

CREATE TABLE manufacturer (
	id SERIAL PRIMARY KEY,
	name TEXT,
	country INTEGER REFERENCES country
);

CREATE TABLE beer (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	review TEXT,
	grade_taste CHAR(1),
	grade_color CHAR(1),
	grade_smell CHAR(1),
	grade_smoothness CHAR(1),
	grade_foam CHAR(1),
	grade_total CHAR(1),
	image TEXT,
	manufacturer INTEGER REFERENCES manufacturer 
);

CREATE TABLE burger (
	id SERIAL PRIMARY KEY,
	name TEXT,
	grade CHAR(1),
	review TEXT,
	manufacturer INTEGER REFERENCES manufacturer
);
