A = load 'input.txt' as (line:chararray);
-- A = load '/user/chc631/HW5/input.txt' as (line:chararray);
B = foreach A generate TOKENIZE(line) as tokens;
C = foreach B generate flatten(tokens) as word;
D = FOREACH C GENERATE ((word matches '.*Chicago.*'? 1:0)) as t1,((word matches '.*Dec.*'?1:0)) as t2,((word matches '.*Java.*'?1:0)) as t3,((word matches '.*Hackathon.*'?1:0)) as t4;
D = FOREACH C GENERATE ((word matches '.*Chicago.*'? 1:0)) as t1,((word matches '.*Dec.*'?1:0)) as t2,((word matches '.*Java.*'?1:0)) as t3,((word matches '.*Hackathon.*'?1:0)) as t4;
E = group D all;
F  = FOREACH E GENERATE FLATTEN(TOBAG(CONCAT('Chicago',' ',(chararray)SUM(D.t1)),CONCAT('Dec',' ',(chararray)SUM(D.t2)),CONCAT('Java',' ',(chararray)SUM(D.t3)),CONCAT('hackathon',' ',(chararray)SUM(D.t4))));
DUMP F;
