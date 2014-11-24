#! perl -slw

=HEADER
Copyright (c) 2014 Matthew Ezewudo <mezewud@emory.edu>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
=cut

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
