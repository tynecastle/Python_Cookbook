import html

def kwargs_only(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

if __name__ == "__main__":
    print(avg(1, 2))
    print(avg(1, 2, 3, 4, 5))
    print(make_element('item', 'Albatross', size='large', quantity=6))
    print(kwargs_only(1, 5, 2, -5, 10, clip=0))