# Ansible role gitea - Install a gitea server

This role installs and manages a [gitea](https://gitea.io) server -
[Source code & screenshots](https://github.com/go-gitea/gitea).

Gitea is a Golang Git repository webapp, having the same look and feel as GitHub.

It is still under developpement, see "Disclaimer" if you can't make it work.

## Sample exemple of use in a playbook

The following have been tested with Debian 8, it should work on Ubuntu as well.

```yaml
- name: "Install gitea"
  hosts: all
  vars:
    gitea_user: "gitea"
    gitea_home: "/var/lib/gitea"
    # To limit your users to 30 repos
    gitea_user_repo_limit: 30
    # Not to make use of any CDN
    gitea_offline_mode: true

    # Some 'rendering' options for your URLs
    gitea_http_domain: git.yourdomain.fr
    gitea_root_url: https://git.yourdomain.fr

    # Here we assume we are behind a reverse proxy that will
    # handle https for us, so we bind on localhost:3000 using HTTP
    gitea_protocol: http
    gitea_http_listen: 127.0.0.1
    gitea_http_port: 3000

    # SSH server configuration
    gitea_ssh_listen: 0.0.0.0
    gitea_ssh_port: 2222
    # For URLs rendering again
    gitea_ssh_domain: git.yourdomain.fr
    gitea_start_ssh: true

    gitea_secret_key: 3sp00ky5me
    gitea_disable_gravatar: true
    # To make at least your first user register
    gitea_disable_registration: false
    gitea_require_signin: true
    gitea_enable_captcha: true

    gitea_show_user_email: false
  roles:
    - gitea
```

## More detailed options
### General

* `gitea_user`: UNIX user used by Gitea
* `gitea_home`: Base directory to work

### Look and feel

* `gitea_app_name`: Displayed application name
* `gitea_show_user_email`: Do you share emails ? (true/false)
* `gitea_disable_gravatar`: Do you disable Gravatar ? (privacy and so on) (true/false)
* `gitea_offline_mode`: Same but with disabling CDNs (true/false)
* `gitea_disable_registration`: Do you disable user registration ? (true/false)
* `gitea_require_signin`: Do you require signin to see things (even public ones) ? (true/false)
* `gitea_enable_captcha`: Do you enable captcha ? (true/false)
* `gitea_secret_key`: Cookie secret key

### Limits

* `gitea_user_repo_limit`: Limit how many repos your user can have (-1 for unlimited)

### HTTP configuration

* `gitea_http_domain`: HTTP domain (displayed in your clone URLs, just the domain like git.foo.fr)
* `gitea_root_url`: Root URL used to access your web app (full URL)
* `gitea_protocol`: Listening protocol (http/https)
* `gitea_http_listen`: Bind address
* `gitea_http_port`: Bind port
* `gitea_disable_http_git`: Disable the use of Git over HTTP ? (true/false)

### SSH configuration

* `gitea_ssh_listen`: Bind address for the SSH server
* `gitea_ssh_domain`: SSH domain (displayed in your clone URLs)
* `gitea_start_ssh`: Do you start the SSH server ? (true/false)
* `gitea_ssh_port`: SSH bind port

### Database configuration

* `gitea_db_type`: Database type, can be `mysql`, `postgres` or `sqlite3`
* `gitea_db_host`: Database host string `host:port`
* `gitea_db_name`: Database name
* `gitea_db_user`: Database username
* `gitea_db_password`: Database password
* `gitea_db_ssl`: Use SSL ? (postgres only!). Can be `required`, `disable`, `verify-full`
* `gitea_db_path`: DB path, if you use `sqlite3`. The default is good enough to work though.

### Mailer configuration

* `gitea_mailer_enabled`: Wether to enable the mailer. Default: `false`
* `gitea_mailer_skip_verify`: Skip SMTP TLS certificate verification
* `gitea_mailer_host`: SMTP server hostname and port
* `gitea_mailer_from`: Sender mail address

## Disclaimer
This module is currently a work in progress. For now it is only able to install
gitea from the Github Release, in a fixed version for Linux amd64, on systems
using systemd.

This said, it should work on every major Linux distribution, it has been tested
successfully on Debian Jessie 64 bits.

## Contributing
Do not hesitate to make me a pull request, and when in doubt you can reach me on
Twitter [@thomas_maurice](https://twitter.com/thomas_maurice).

I also would be happy to fix the issues that would be opened.

## Author
This role is written by [Thomas Maurice](https://thomas.maurice.fr).
