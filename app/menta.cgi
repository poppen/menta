#!/usr/bin/perl
use lib '../lib';
use MENTA;
# -- ここまではおまじない --

require "../plugins/mail.pl";
require "../plugins/dbi_select.pl";

run_menta({
    # MENTA 自体の設定
    menta => {
        # エラー出力するか？
        kcatch_mode => 1,
        # 最大表示文字数
        max_post_body => 1_024_000,
        # テンプレートファイルディレクトリへのパス
        tmpl_dir => 'tmpl/',
        # テンプレートファイルのキャッシュディレクトリへのパス
        tmpl_cache_dir => 'tmpl_cache/',
    },
    # あなたのアプリの設定
    application => {
        docroot => '',
        title => 'MENTA サンプルアプリ',
    },
});

# あなたのプログラム
sub do_index {
    render('index.html');
}

sub do_param {
    my $foo = param('foo');
    finalize("PARAM foo: $foo");
}

sub do_goto_wassr {
    redirect('http://wassr.jp/');
}

sub do_mail {
    mail_send('info@example.com', 'this is subject', 'hi!');
    redirect('http://example.com');
}

sub do_users {
    my @rows = dbi_select('DBI:CSV:f_dir=../app/data', 'select * from users');
    render('users.html', \@rows);
}

sub do_form {
    my $r = param('r') || '';
    render('form.html', $r);
}

sub do_die {
    die "こういう風に死にます"
}
