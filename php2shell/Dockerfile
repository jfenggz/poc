ARG PHP_VER=8.4.26
FROM php:${PHP_VER}-apache

COPY php.ini            /usr/local/etc/php/php.ini
COPY apache-prefork.conf /etc/apache2/conf-enabled/zz-prefork.conf
COPY www/               /var/www/html/

RUN mkdir -p /var/lib/php/sessions \
 && chown -R www-data:www-data /var/www/html /var/lib/php/sessions \
 && a2enmod mpm_prefork >/dev/null 2>&1 || true

