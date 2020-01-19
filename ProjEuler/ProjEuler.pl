#!/usr/bin/env perl
use strict;
use warnings;


sub isPrime
{
=begin comment
    
    isPrime() takes a positive integer as argument and returns 1 if it
    is a prime, 0 otherwise 
    
=cut
    
    my $num = $_;
    if ($num < 2)
    {
        return 0;
    }
    if (($num == 2) || ($num == 3))
    {
        return 1
    }
    if ((($num + 1) % 6 != 0) && (($num - 1) % 6 != 0))
    {
        return 0
    }
    my $lim = int(sqrt($num))+1;
    foreach (2..$lim)
    {
        if ($num % $_ == 0)
        {
            return 0;
        }
    }
    return 1;
}


sub testP
{
=pod
testP makes use of isPrime to check if substrings of prime numbers are
also prime numbers


=cut

    my $num = $_;
    if (isPrime($num) == 0)
    {
        return 0;
    }
    if ($num <= 9)
    {
        return isPrime($num);
    }
}

foreach (1..10)
{
    print($_, " ", testP($_), "\n");
}
