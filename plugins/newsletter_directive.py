from docutils.parsers.rst import directives, Directive
from docutils import nodes


newsletter_div = """
<div class="inline-newsletter">
    <div class="newsletter-title"><p class="lead">Newsletter</p></div>
    <newsletter-body>
    <p>Sign up to keep up to date with all the latest news and articles</p>
        <form action="https://uetke.us17.list-manage.com/subscribe/post?u=57a7ac8cbc79b7548db42490e&amp;id=6fde4af646" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="form-inline validate" target="_blank" novalidate>
            <div class="form-group mc-field-group">
                <input type="email" placeholder="Enter your Email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
            </div>
            <div id="mce-responses" class="clear">
                <div class="response" id="mce-error-response" style="display:none"></div>
                <div class="response" id="mce-success-response" style="display:none"></div>
            </div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
            <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_57a7ac8cbc79b7548db42490e_6fde4af646" tabindex="-1" value=""></div>
            <input type="submit" value="Subscribe" name="subscribe" id="mc-inline-subscribe"  class="btn ml-2 btn-secondary mc-inline-subscribe">&nbsp;</button>
        </form>
        <p class="">No spam, promise.</p>
    </newsletter-body>
</div>
"""


class Newsletter(Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = False

    def run(self):
        return [nodes.raw('', newsletter_div, format='html'),]


def register():
    directives.register_directive('newsletter', Newsletter)
