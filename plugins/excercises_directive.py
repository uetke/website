from docutils.parsers.rst import directives, Directive
from docutils import nodes

import re


class Excercise(Directive):
    has_content = True

    def run(self):
        text = ""
        for c in self.content:
            text += c + "<br />"

        return [
            nodes.raw('', "<div class='excercise'>", format='html'),
            nodes.raw('', "<p class='title'>Excercise</p>", format='html'),
            nodes.raw('', text, format='html'),
            nodes.raw('', "</div>", format='html')
        ]


class Exercise(Directive):
    required_arguments = 0
    optional_arguments = 1
    has_content = True
    option_spec = {'image': directives.unchanged}

    def run(self):
        text = ""
        for c in self.content:
            text += c + "<br />"

        text = re.sub(r"\`\`(.+?)\`\`", r'<tt class="literal">\1</tt>', text)

        text_title = "<p class='first admonition-title'><i class=\"far fa-question-circle\"></i>Exercise</p>"
        text_str = text

        img_str = ""
        if 'image' in self.options:
            reference = directives.uri(self.options['image'])
            img_class = 'fluid'
            img_str = '<img src="{}" class="{}">'.format(reference, img_class)

        div_raw = '<div class="admonition exercise"> ' \
                  '             {}' \
                  '     <p>{}</p>' \
                  '     <p>{}</p>' \
                  '</div>'.format(text_title, text_str, img_str)

        return [nodes.raw('', div_raw, format='html'),]

def register():
    directives.register_directive('excercise', Excercise)
    directives.register_directive('exercise', Exercise)
