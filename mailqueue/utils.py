import re

from django.utils.html import strip_tags
from django.template.loader import render_to_string


def clean_email(email):
    """
    >>> clean_email('xxx@GMail.com')
    'xxx@gmail.com'
    >>> clean_email('xxx+whois@GMail.com')
    'xxx@gmail.com'
    """
    email = email.lower()
    return re.compile('\\+[^@]+@').sub('@', email)


def clean_subject(subject):
    return subject.strip().replace(
        '\r',
        ' ',
    ).replace(
        '\n',
        ' ',
    ).replace(
        '  ',
        ' ',
    )


def html2plaintext(s):
    s = s.replace('<br />', '\r\n')
    s = strip_tags(s)
    # TODO: expand <a href="">
    return s


def render_letter(template, context=None):
    splitter = '=-' * 100
    content = render_to_string(template, dict(
        context or {},
        subject_body_splitter=splitter,
    ))
    bits = content.split(splitter)
    assert len(bits) == 2, 'Incorrect mail tempate: {}'.format(template)
    subject = clean_subject(bits[0])
    body = bits[1].strip()
    return subject, body
