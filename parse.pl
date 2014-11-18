#! perl -slw
use strict;

my( $ID, $query, $off );
my $filename = $ARGV[0];
my $filename2 = $filename.".txt";
open(FILE1, $filename); 
open(FILE2,'>'.$filename2);
while( <FILE1> ) {
    if( m[^>]  ) {
        ( $ID ) = (split " ", $_)[ 1 ];
        next;
    }
    if( m[^Query] ) {
        ( $query ) = m[^Query\s+(\d+)];
        my $top = substr $_, 15;
        my $pipes = substr <FILE1>, 15;
        my $bot = substr <FILE1>, 15;
        my $p = 0;
        while( $p = 1+index $pipes, " ", $p ) {
            printf FILE2 "%20s :(%d) %1s/%1s\n",
             $ID, $query+$p,
             substr( $top, $p-1, 1 ),
             substr( $bot, $p-1, 1 );
        }
    }
}
close(FILE1);
close(FILE2);
