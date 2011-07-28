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

register = template.Library()


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_text(context, text, size='M'):
    sizes_dict = {'s': 120, 'm': 230, 'l': 350}
    if not size.lower() in sizes_dict:
        size = 'm'
    return {'text': text,
            'size': sizes_dict[size.lower()]}


@register.inclusion_tag('qrcode/qr_tag.html', takes_context=True)
def qr_from_mail(context, text, size='M'):
    return qr_from_text(context, text='mailto:%s' % text, size=size)
