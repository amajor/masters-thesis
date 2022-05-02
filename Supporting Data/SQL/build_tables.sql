CREATE TABLE pylint_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 50 ),
  n_refactor  VARCHAR ( 50 ),
  n_convention VARCHAR ( 50 ),
  statement VARCHAR ( 50 ),
  global_note VARCHAR ( 50 )
);

CREATE TABLE pylint_metrics_by_msg (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 50 ),
  msg  VARCHAR ( 50 ),
  code VARCHAR ( 50 ),
  n VARCHAR ( 50 )
);

CREATE TABLE git_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 50 ),
  commit_digest  VARCHAR ( 50 ),
  author VARCHAR ( 50 ),
  commited_at VARCHAR ( 50 ),
  commit_msg VARCHAR ( 50 ),
  lines_added VARCHAR ( 50 ),
  lines_removed VARCHAR ( 50 ),
  bug VARCHAR ( 50 )
);

CREATE TABLE radon_raw_metrics (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 50 ),
  loc VARCHAR ( 50 ),
  lloc VARCHAR ( 50 ),
  single_comments VARCHAR ( 50 ),
  sloc VARCHAR ( 50 ),
  multi VARCHAR ( 50 ),
  comments VARCHAR ( 50 ),
  blank VARCHAR ( 50 )
);

CREATE TABLE radon_complexity_details (
  name VARCHAR ( 50 ),
  module_name VARCHAR ( 50 ),
  entity_name VARCHAR ( 50 ),
  type VARCHAR ( 50 ),
  complexity VARCHAR ( 50 ),
  rank VARCHAR ( 50 ),
  indentation VARCHAR ( 50 ),
  classname VARCHAR ( 50 )
);
