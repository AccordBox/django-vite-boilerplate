import "./app.css";
import 'htmx.org';
import Alpine from 'alpinejs';

window.Alpine = Alpine;
Alpine.start();

document.addEventListener('DOMContentLoaded', () => {
    console.log('👋 Hello World from django-vite-boilerplate');
});
