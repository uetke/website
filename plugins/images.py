from docutils.parsers.rst import directives, Directive
from docutils import nodes


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class Image(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.nonnegative_int,
                   'width': directives.nonnegative_int,
                   'scale': directives.nonnegative_int,
                   'align': align,
                   }
    has_content = False

    def run(self):
        reference = directives.uri(self.arguments[0])
        self.options['uri'] = reference
        img_class = 'img-thumbnail'

        if 'align' in self.options:
            if self.options['align'] == 'right':
                img_class = 'rounded float-right'
            elif self.options['align'] == 'left':
                img_class = 'rounded float-left'
            elif self.options['align'] == 'center':
                img_class = 'rounded mx-auto d-block'

        img_str = '<img alt="{}" src="{}" class="{}">'.format(self.options['alt'],
                                                    self.options['uri'],
                                                    img_class)

        img = [nodes.raw('', img_str, format='html'), ]
        return img


def register():
    directives.register_directive('images', Image)
