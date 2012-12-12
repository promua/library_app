PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE book (
	id VARCHAR(36) NOT NULL, 
	name VARCHAR(64), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "book" VALUES('5bd66e11-98ff-4b0b-9d9e-8666350ee59b','Refactoring: Improving the Design of Existing Code');
INSERT INTO "book" VALUES('2fe36de4-4af4-4b6b-b43b-011889360d67','Design Patterns: Elements of Reusable Object-Oriented Software');
INSERT INTO "book" VALUES('647ba110-d2f9-4802-9c4a-cd329ea9563a','Introduction to Algorithms');
CREATE TABLE author (
	id VARCHAR(36) NOT NULL, 
	name VARCHAR(64), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "author" VALUES('bd82cf5a-4ce5-418d-ba37-f2680c258ec4','Martin Fowler');
INSERT INTO "author" VALUES('929a12d7-21b5-425c-a698-824fe129d192','Kent Beck');
INSERT INTO "author" VALUES('52b60d64-d07b-4c7e-bed7-4273da7bae6d','Erich Gamma');
INSERT INTO "author" VALUES('6213d916-64a4-4f85-bfed-cd907fab617e','Richard Helm');
INSERT INTO "author" VALUES('74f4e916-da53-44f1-a9b4-400eabc6a6f0','Thomas H. Cormen');
INSERT INTO "author" VALUES('d5bdb8fc-9bcd-477b-84d7-8b748d7c314b','Charles E. Leiserson');
CREATE TABLE author_book_rel (
	author_id VARCHAR(36) NOT NULL, 
	book_id VARCHAR(36) NOT NULL, 
	PRIMARY KEY (author_id, book_id), 
	FOREIGN KEY(author_id) REFERENCES author (id), 
	FOREIGN KEY(book_id) REFERENCES book (id)
);
INSERT INTO "author_book_rel" VALUES('929a12d7-21b5-425c-a698-824fe129d192','5bd66e11-98ff-4b0b-9d9e-8666350ee59b');
INSERT INTO "author_book_rel" VALUES('bd82cf5a-4ce5-418d-ba37-f2680c258ec4','5bd66e11-98ff-4b0b-9d9e-8666350ee59b');
INSERT INTO "author_book_rel" VALUES('52b60d64-d07b-4c7e-bed7-4273da7bae6d','2fe36de4-4af4-4b6b-b43b-011889360d67');
INSERT INTO "author_book_rel" VALUES('6213d916-64a4-4f85-bfed-cd907fab617e','2fe36de4-4af4-4b6b-b43b-011889360d67');
INSERT INTO "author_book_rel" VALUES('d5bdb8fc-9bcd-477b-84d7-8b748d7c314b','647ba110-d2f9-4802-9c4a-cd329ea9563a');
INSERT INTO "author_book_rel" VALUES('74f4e916-da53-44f1-a9b4-400eabc6a6f0','647ba110-d2f9-4802-9c4a-cd329ea9563a');
COMMIT;
