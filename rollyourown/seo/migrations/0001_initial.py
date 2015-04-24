# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "example.com" will be used.', max_length=511, blank=True)),
                ('heading', models.CharField(default=b'', max_length=68, verbose_name=b'tag two', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', max_length=155, verbose_name=b'metatag two', blank=True)),
                ('raw1', models.TextField(default=b'', blank=True)),
                ('raw2', models.TextField(default=b'', verbose_name=b'raw two', blank=True)),
                ('help_text1', models.CharField(default=b'', help_text=b'Some help text 1.', max_length=511, blank=True)),
                ('help_text2', models.CharField(default=b'', help_text=b'Updated help text2.', max_length=511, blank=True)),
                ('help_text3', models.CharField(default=b'', help_text=b'Some help text 3.', max_length=511, blank=True)),
                ('help_text4', models.CharField(default=b'', help_text='If empty, Always xyz', max_length=511, blank=True)),
                ('help_text5', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('help_text6', models.CharField(default=b'', help_text=b'Some help text 6.', max_length=511, blank=True)),
                ('populate_from1', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from2', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('populate_from3', models.CharField(default=b'', help_text='If empty, "efg" will be used.', max_length=511, blank=True)),
                ('populate_from4', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from6', models.CharField(default=b'', help_text='If empty, None will be used.', max_length=511, blank=True)),
                ('populate_from7', models.CharField(default=b'', max_length=511, blank=True)),
                ('field1', models.TextField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Basic Metadatum (Model)',
                'verbose_name_plural': 'Basic Metadata (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoverageModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "example.com" will be used.', max_length=511, blank=True)),
                ('heading', models.CharField(default=b'', max_length=68, verbose_name=b'tag two', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', max_length=155, verbose_name=b'metatag two', blank=True)),
                ('raw1', models.TextField(default=b'', blank=True)),
                ('raw2', models.TextField(default=b'', verbose_name=b'raw two', blank=True)),
                ('help_text1', models.CharField(default=b'', help_text=b'Some help text 1.', max_length=511, blank=True)),
                ('help_text2', models.CharField(default=b'', help_text=b'Updated help text2.', max_length=511, blank=True)),
                ('help_text3', models.CharField(default=b'', help_text=b'Some help text 3.', max_length=511, blank=True)),
                ('help_text4', models.CharField(default=b'', help_text='If empty, Always xyz', max_length=511, blank=True)),
                ('help_text5', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('help_text6', models.CharField(default=b'', help_text=b'Some help text 6.', max_length=511, blank=True)),
                ('populate_from1', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from2', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('populate_from3', models.CharField(default=b'', help_text='If empty, "efg" will be used.', max_length=511, blank=True)),
                ('populate_from4', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from6', models.CharField(default=b'', help_text='If empty, None will be used.', max_length=511, blank=True)),
                ('populate_from7', models.CharField(default=b'', max_length=511, blank=True)),
                ('field1', models.TextField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', unique=True, max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Basic Metadatum (Model Instance)',
                'verbose_name_plural': 'Basic Metadata (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoveragePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "example.com" will be used.', max_length=511, blank=True)),
                ('heading', models.CharField(default=b'', max_length=68, verbose_name=b'tag two', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', max_length=155, verbose_name=b'metatag two', blank=True)),
                ('raw1', models.TextField(default=b'', blank=True)),
                ('raw2', models.TextField(default=b'', verbose_name=b'raw two', blank=True)),
                ('help_text1', models.CharField(default=b'', help_text=b'Some help text 1.', max_length=511, blank=True)),
                ('help_text2', models.CharField(default=b'', help_text=b'Updated help text2.', max_length=511, blank=True)),
                ('help_text3', models.CharField(default=b'', help_text=b'Some help text 3.', max_length=511, blank=True)),
                ('help_text4', models.CharField(default=b'', help_text='If empty, Always xyz', max_length=511, blank=True)),
                ('help_text5', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('help_text6', models.CharField(default=b'', help_text=b'Some help text 6.', max_length=511, blank=True)),
                ('populate_from1', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from2', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('populate_from3', models.CharField(default=b'', help_text='If empty, "efg" will be used.', max_length=511, blank=True)),
                ('populate_from4', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from6', models.CharField(default=b'', help_text='If empty, None will be used.', max_length=511, blank=True)),
                ('populate_from7', models.CharField(default=b'', max_length=511, blank=True)),
                ('field1', models.TextField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'Basic Metadatum (Path)',
                'verbose_name_plural': 'Basic Metadata (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoverageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "example.com" will be used.', max_length=511, blank=True)),
                ('heading', models.CharField(default=b'', max_length=68, verbose_name=b'tag two', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', max_length=155, verbose_name=b'metatag two', blank=True)),
                ('raw1', models.TextField(default=b'', blank=True)),
                ('raw2', models.TextField(default=b'', verbose_name=b'raw two', blank=True)),
                ('help_text1', models.CharField(default=b'', help_text=b'Some help text 1.', max_length=511, blank=True)),
                ('help_text2', models.CharField(default=b'', help_text=b'Updated help text2.', max_length=511, blank=True)),
                ('help_text3', models.CharField(default=b'', help_text=b'Some help text 3.', max_length=511, blank=True)),
                ('help_text4', models.CharField(default=b'', help_text='If empty, Always xyz', max_length=511, blank=True)),
                ('help_text5', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('help_text6', models.CharField(default=b'', help_text=b'Some help text 6.', max_length=511, blank=True)),
                ('populate_from1', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from2', models.CharField(default=b'', help_text='If empty, tag two will be used.', max_length=511, blank=True)),
                ('populate_from3', models.CharField(default=b'', help_text='If empty, "efg" will be used.', max_length=511, blank=True)),
                ('populate_from4', models.CharField(default=b'', max_length=511, blank=True)),
                ('populate_from6', models.CharField(default=b'', help_text='If empty, None will be used.', max_length=511, blank=True)),
                ('populate_from7', models.CharField(default=b'', max_length=511, blank=True)),
                ('field1', models.TextField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'Basic Metadatum (View)',
                'verbose_name_plural': 'Basic Metadata (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultMetadataModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text=b'This is the page title, that appears in the title bar.', max_length=68, blank=True)),
                ('keywords', models.CharField(default=b'', help_text=b'Comma-separated keywords for search engines.', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', help_text=b'A short description, displayed in search results.', max_length=155, blank=True)),
                ('heading', models.CharField(default=b'', help_text=b'This is the page heading, appearing in the &lt;h1&gt; tag.', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Metadata (Model)',
                'verbose_name_plural': 'Metadata (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultMetadataModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text=b'This is the page title, that appears in the title bar.', max_length=68, blank=True)),
                ('keywords', models.CharField(default=b'', help_text=b'Comma-separated keywords for search engines.', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', help_text=b'A short description, displayed in search results.', max_length=155, blank=True)),
                ('heading', models.CharField(default=b'', help_text=b'This is the page heading, appearing in the &lt;h1&gt; tag.', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', unique=True, max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Metadata (Model Instance)',
                'verbose_name_plural': 'Metadata (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultMetadataPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text=b'This is the page title, that appears in the title bar.', max_length=68, blank=True)),
                ('keywords', models.CharField(default=b'', help_text=b'Comma-separated keywords for search engines.', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', help_text=b'A short description, displayed in search results.', max_length=155, blank=True)),
                ('heading', models.CharField(default=b'', help_text=b'This is the page heading, appearing in the &lt;h1&gt; tag.', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'Metadata (Path)',
                'verbose_name_plural': 'Metadata (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultMetadataView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text=b'This is the page title, that appears in the title bar.', max_length=68, blank=True)),
                ('keywords', models.CharField(default=b'', help_text=b'Comma-separated keywords for search engines.', max_length=511, blank=True)),
                ('description', models.CharField(default=b'', help_text=b'A short description, displayed in search results.', max_length=155, blank=True)),
                ('heading', models.CharField(default=b'', help_text=b'This is the page heading, appearing in the &lt;h1&gt; tag.', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'Metadata (View)',
                'verbose_name_plural': 'Metadata (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithBackendsPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'with backends (Path)',
                'verbose_name_plural': 'with backendss (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithBackendsView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'with backends (View)',
                'verbose_name_plural': 'with backendss (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheI18nModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with cache i18n (Model)',
                'verbose_name_plural': 'with cache i18ns (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheI18nModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with cache i18n (Model Instance)',
                'verbose_name_plural': 'with cache i18ns (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheI18nPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(max_length=255, verbose_name='path')),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
            ],
            options={
                'verbose_name': 'with cache i18n (Path)',
                'verbose_name_plural': 'with cache i18ns (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheI18nView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', max_length=255, verbose_name='view', blank=True)),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
            ],
            options={
                'verbose_name': 'with cache i18n (View)',
                'verbose_name_plural': 'with cache i18ns (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with cache (Model)',
                'verbose_name_plural': 'with caches (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', unique=True, max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with cache (Model Instance)',
                'verbose_name_plural': 'with caches (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCachePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'with cache (Path)',
                'verbose_name_plural': 'with caches (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheSitesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with cache sites (Model)',
                'verbose_name_plural': 'with cache sitess (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheSitesModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with cache sites (Model Instance)',
                'verbose_name_plural': 'with cache sitess (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheSitesPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(max_length=255, verbose_name='path')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with cache sites (Path)',
                'verbose_name_plural': 'with cache sitess (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheSitesView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', max_length=255, verbose_name='view', blank=True)),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with cache sites (View)',
                'verbose_name_plural': 'with cache sitess (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithCacheView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', help_text='If empty, "1234" will be used.', max_length=511, blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'with cache (View)',
                'verbose_name_plural': 'with caches (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithI18nModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with i18n (Model)',
                'verbose_name_plural': 'with i18ns (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithI18nModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with i18n (Model Instance)',
                'verbose_name_plural': 'with i18ns (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithI18nPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(max_length=255, verbose_name='path')),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
            ],
            options={
                'verbose_name': 'with i18n (Path)',
                'verbose_name_plural': 'with i18ns (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithI18nView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', max_length=255, verbose_name='view', blank=True)),
                ('_language', models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')], max_length=5, blank=True, null=True, verbose_name='language', db_index=True)),
            ],
            options={
                'verbose_name': 'with i18n (View)',
                'verbose_name_plural': 'with i18ns (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with redirect (Model)',
                'verbose_name_plural': 'with redirects (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', unique=True, max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with redirect (Model Instance)',
                'verbose_name_plural': 'with redirects (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'with redirect (Path)',
                'verbose_name_plural': 'with redirects (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectSitesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with redirect sites (Model)',
                'verbose_name_plural': 'with redirect sitess (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectSitesModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with redirect sites (Model Instance)',
                'verbose_name_plural': 'with redirect sitess (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectSitesPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(max_length=255, verbose_name='path')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with redirect sites (Path)',
                'verbose_name_plural': 'with redirect sitess (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectSitesView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', max_length=255, verbose_name='view', blank=True)),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with redirect sites (View)',
                'verbose_name_plural': 'with redirect sitess (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithRedirectView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'with redirect (View)',
                'verbose_name_plural': 'with redirects (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSEOModelsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with seo models (Model)',
                'verbose_name_plural': 'with seo modelss (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSEOModelsModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', unique=True, max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'with seo models (Model Instance)',
                'verbose_name_plural': 'with seo modelss (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSEOModelsPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(unique=True, max_length=255, verbose_name='path')),
            ],
            options={
                'verbose_name': 'with seo models (Path)',
                'verbose_name_plural': 'with seo modelss (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSEOModelsView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', unique=True, max_length=255, verbose_name='view', blank=True)),
            ],
            options={
                'verbose_name': 'with seo models (View)',
                'verbose_name_plural': 'with seo modelss (View)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSitesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with sites (Model)',
                'verbose_name_plural': 'with sitess (Model)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSitesModelInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(verbose_name='path', max_length=255, editable=False, blank=True)),
                ('_object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('_content_type', models.ForeignKey(verbose_name='model', to='contenttypes.ContentType')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with sites (Model Instance)',
                'verbose_name_plural': 'with sitess (Model Instance)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSitesPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_path', models.CharField(max_length=255, verbose_name='path')),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with sites (Path)',
                'verbose_name_plural': 'with sitess (Path)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WithSitesView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=511, blank=True)),
                ('_view', models.CharField(default=b'', max_length=255, verbose_name='view', blank=True)),
                ('_site', models.ForeignKey(verbose_name='site', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'with sites (View)',
                'verbose_name_plural': 'with sitess (View)',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='withsitesview',
            unique_together=set([('_view', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withsitespath',
            unique_together=set([('_path', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withsitesmodelinstance',
            unique_together=set([('_path', '_site'), ('_content_type', '_object_id', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withsitesmodel',
            unique_together=set([('_content_type', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withseomodelsview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withseomodelspath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withseomodelsmodelinstance',
            unique_together=set([('_path',), ('_content_type', '_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='withseomodelsmodel',
            unique_together=set([('_content_type',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectsitesview',
            unique_together=set([('_view', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectsitespath',
            unique_together=set([('_path', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectsitesmodelinstance',
            unique_together=set([('_path', '_site'), ('_content_type', '_object_id', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectsitesmodel',
            unique_together=set([('_content_type', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectpath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectmodelinstance',
            unique_together=set([('_path',), ('_content_type', '_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='withredirectmodel',
            unique_together=set([('_content_type',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withi18nview',
            unique_together=set([('_view', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withi18npath',
            unique_together=set([('_path', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withi18nmodelinstance',
            unique_together=set([('_path', '_language'), ('_content_type', '_object_id', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withi18nmodel',
            unique_together=set([('_content_type', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcacheview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachesitesview',
            unique_together=set([('_view', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachesitespath',
            unique_together=set([('_path', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachesitesmodelinstance',
            unique_together=set([('_path', '_site'), ('_content_type', '_object_id', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachesitesmodel',
            unique_together=set([('_content_type', '_site')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachepath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachemodelinstance',
            unique_together=set([('_path',), ('_content_type', '_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachemodel',
            unique_together=set([('_content_type',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachei18nview',
            unique_together=set([('_view', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachei18npath',
            unique_together=set([('_path', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachei18nmodelinstance',
            unique_together=set([('_path', '_language'), ('_content_type', '_object_id', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withcachei18nmodel',
            unique_together=set([('_content_type', '_language')]),
        ),
        migrations.AlterUniqueTogether(
            name='withbackendsview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='withbackendspath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='defaultmetadataview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='defaultmetadatapath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='defaultmetadatamodelinstance',
            unique_together=set([('_path',), ('_content_type', '_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='defaultmetadatamodel',
            unique_together=set([('_content_type',)]),
        ),
        migrations.AlterUniqueTogether(
            name='coverageview',
            unique_together=set([('_view',)]),
        ),
        migrations.AlterUniqueTogether(
            name='coveragepath',
            unique_together=set([('_path',)]),
        ),
        migrations.AlterUniqueTogether(
            name='coveragemodelinstance',
            unique_together=set([('_path',), ('_content_type', '_object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='coveragemodel',
            unique_together=set([('_content_type',)]),
        ),
    ]
