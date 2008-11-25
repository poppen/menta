package MENTA::Response;
use strict;
use warnings;
use base qw/Class::Accessor::Fast/;
use HTTP::Headers;

__PACKAGE__->mk_accessors(qw/code content headers/);

sub new {
    my ($class, %args) = @_;
    bless {
        code    => 200,
        content => '',
        headers => HTTP::Headers->new(),
        %args,
    }, $class;
}

sub header {
    my $self = shift;
    $self->headers->header(@_);
}

sub as_string {
    my $self = shift;
    join(
        '',
        $self->headers->as_string(),
        "\r\n",
        $self->content
    );
}

1;