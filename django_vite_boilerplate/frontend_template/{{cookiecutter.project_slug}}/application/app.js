{% if cookiecutter.javascript_solution == 'htmx_alpine' %}
import htmx from 'htmx.org';
import Alpine from 'alpinejs';

window.htmx = htmx;
window.Alpine = Alpine;
Alpine.start();
{% elif cookiecutter.javascript_solution == 'valinajs' and cookiecutter.style_solution == 'bootstrap'%}
import "bootstrap/dist/js/bootstrap.bundle";

document.addEventListener('DOMContentLoaded', () => {
    console.log('👋 Hello World from django-vite-boilerplate');
});
{% elif cookiecutter.javascript_solution == 'valinajs' %}
document.addEventListener('DOMContentLoaded', () => {
    console.log('👋 Hello World from django-vite-boilerplate');
});
{% elif cookiecutter.javascript_solution == 'hotwire' %}
import "@hotwired/turbo-rails";
import '@hotwired/stimulus';
{% endif %}
