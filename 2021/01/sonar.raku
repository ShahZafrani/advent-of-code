say 'hello raku';


my $testFile = 'test.txt'.IO.lines;

say split('\s', $testFile.lines[0])