DROP TABLE IF EXISTS 'country';

CREATE TABLE 'country' (
  'code' char(15) NOT NULL default '',
  'name' char(100) NOT NULL default '',
  'continent' char(50) NOT NULL default ''
);

INSERT INTO 'country' VALUES ('CHL','Chile','America');
INSERT INTO 'country' VALUES ('VEN','Venezuela','America');
INSERT INTO 'country' VALUES ('FRA','Francia','Europa');
INSERT INTO 'country' VALUES ('CHN','China','Asia');
