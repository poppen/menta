? my $title = 'ケータイ対応'
?=r render_partial('header.mt', $title)
<h1><?= $title ?></h1>
<p>あなたのブラウザは <?= mobile_carrier_longname ?> です</p>
?=r render_partial('footer.mt')