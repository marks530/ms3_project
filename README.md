
## Milestone 3 Project
###Errors
Inevitably some tying errors will occur and trying to identify them can be difficult and time comsuming. However,
using the Traceback in the Jinja Error page proved to be very useful in tracing the exact location of the
syntax error
Example:
File "/workspace/ms3_project/templates/login.html", line 40, in template
    <a href="{{ url_for('register' }}" class="light-blue darken-4 text-shadow">Register Account</a>
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'

jinja2.exceptions.TemplateSyntaxError
jinja2.exceptions.TemplateSyntaxError: unexpected '}', expected ')'