# Copyright (c) 2011 by Zocolab <pablo@zocolab.es>
#
# Merengue is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Merengue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software. If not, see <http://www.gnu.org/licenses/>.

from django import template

from django.contrib.sites.models import Site

register = template.Library()


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_text(context, text, size='M'):
    if type(size) == type(0) or type(size) == type('') and size.isdigit():
        # this checks if it's an integer or a string with an integer
        actual_size = size
    else:
        sizes_dict = {'s': 120, 'm': 230, 'l': 350}
        if not size.lower() in sizes_dict:
            size = 'm'
        actual_size = sizes_dict[size.lower()]
    return {'text': text,
            'size': actual_size}


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_mail(context, text, size='M'):
    return qr_from_text(context, text='mailto:%s' % text, size=size)


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_contact(context, contact, size='M'):
    final_string = 'MECARD:'
    if contact['name']:
        final_string += 'N:%s;' % contact['name'].replace(' ', '+')
    if contact['phone_number']:
        final_string += 'TEL:%s;' % contact['phone_number'].replace(
            ' ', '+')
    if contact['url']:
        final_string += 'URL:%s;' % contact['url'].replace(
            ' ', '+')
    if contact['email']:
        final_string += 'EMAIL:%s;' % contact['email'].replace(
            ' ', '+')
    if contact['company']:
        final_string += 'ORG:%s;' % contact['company'].replace(
            ' ', '+')
    return qr_from_text(context, text=final_string, size=size)


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_object(context, obj, size='M'):
    domain = Site.objects.get_current().domain
    path = obj.get_absolute_url()
    text = 'http://%s%s' % (domain, path)
    return qr_from_text(context, text, size=size)
