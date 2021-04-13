# Ansible role gitea - Install a gitea server
[![Build Status](https://travis-ci.org/thomas-maurice/ansible-role-gitea.svg?branch=master)](https://travis-ci.org/thomas-maurice/ansible-role-gitea)
![Ansible Role](https://img.shields.io/ansible/role/38779)
![Ansible Role](https://img.shields.io/ansible/role/d/38779)
![Ansible Quality Score](https://img.shields.io/ansible/quality/38779)

This role installs and manages a [gitea](https://gitea.io) server -
[Source code & screenshots](https://github.com/go-gitea/gitea).

Gitea is a Golang Git repository webapp, having the same look and feel as GitHub.

## Sample example of use in a playbook

The following code has been tested with Debian 8, it should work on Ubuntu as well.

```yaml
- name: "Install gitea"
  hosts: all
  vars:
    gitea_user: "gitea"
    gitea_home: "/var/lib/gitea"
    # To limit your users to 30 repos
    gitea_user_repo_limit: 30
    # Don't use a public CDN for frontend assets
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

* `gitea_version_check`: Check if installed version != `gitea_version` before initiating binary download
* `gitea_user`: UNIX user used by Gitea
* `gitea_group`: UNIX group used by Gitea
* `gitea_home`: Base directory to work
* `gitea_dl_url`: The URL, the compiled gitea-binary will be downloaded from
* `gitea_systemd_cap_net_bind_service`: Adds `AmbientCapabilities=CAP_NET_BIND_SERVICE` to systemd service file
* `gitea_extra_config`: Additional configuration

### Look and feel

* `gitea_app_name`: Displayed application name
* `gitea_show_user_email`: Do you want to display email addresses ? (true/false)
* `gitea_disable_gravatar`: Do you want to disable Gravatar ? (privacy and so on) (true/false)
* `gitea_offline_mode`: Same but for disabling CDNs for frontend assets (true/false)
* `gitea_disable_registration`: Do you want to disable user registration ? (true/false)
* `gitea_only_allow_external_registration`: Do you want to force registration only using third-party services ? (true/false)
* `gitea_show_registration_button`: Do you want to show the registration button? (true/false)
* `gitea_require_signin`: Do you require a signin to see repo's (even public ones) ? (true/false)
* `gitea_enable_captcha`: Do you want to enable captcha's ? (true/false)
* `gitea_themes`: List of enabled themes
* `gitea_theme_default`: Default theme

### Security
* `gitea_secret_key`: Cookie secret key
* `gitea_internal_token`: Internal API token
* `gitea_disable_git_hooks`: Do you want to disable the interface to add git hooks? If enabled it could be a security bug as it can be used for RCE. Defaults to true (true/false)

### Limits

* `gitea_user_repo_limit`: Limit how many repos a user can have (-1 for unlimited)

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
* `gitea_start_ssh`: Do you want to start a built-in SSH server ? (true/false)
* `gitea_ssh_port`: SSH bind port

### Database configuration

* `gitea_db_type`: Database type, can be `mysql`, `postgres` or `sqlite3`
* `gitea_db_host`: Database host string `host:port` or `/run/postgresql/` when connectiong to postgres via local unix socket (peer authentication)
* `gitea_db_name`: Database name
* `gitea_db_user`: Database username
* `gitea_db_password`: Database password
* `gitea_db_ssl`: Use SSL ? (postgres only!). Can be `require`, `disable`, `verify-ca` or `verify-full`
* `gitea_db_path`: DB path, if you use `sqlite3`. The default is good enough to work though.

### Mailer configuration

* `gitea_mailer_enabled`: Whether to enable the mailer. Default: `false`
* `gitea_mailer_skip_verify`: Skip SMTP TLS certificate verification (true/false)
* `gitea_mailer_tls_enabled`: Enable TLS for SMTP connections (true/false)
* `gitea_mailer_host`: SMTP server hostname and port
* `gitea_mailer_user`: SMTP server username
* `gitea_mailer_password`: SMTP server password
* `gitea_mailer_from`: Sender mail address
* `gitea_enable_notify_mail`:  Whether e-mail should be send to watchers of a repository when something happens. Default: `false`
* `gitea_mail_default`: Default configuration for email notifications for users (user configurable). Options: enabled, onmention, disable  (Default: `onmention` )
* `gitea_autowatch_new_repo`: Enable this to let all organisation users watch new repos when they are created (Default: `false`)
* `gitea_autowatch_on_change`: Enable this to make users watch a repository after their first commit to it (Default: `true`)
* `gitea_show_mailstones_dashboard`: Enable this to show the milestones dashboard page - a view of all the user’s milestones (Default: `true`)

### Fail2Ban configuration

If enabled, this will deploy a fail2ban filter and jail config for Gitea as described in the [Gitea Documentation](https://docs.gitea.io/en-us/fail2ban-setup/).

As this will only deploy config files, fail2ban already has to be installed or otherwise the role will fail.

* `gitea_fail2ban_enabled`: Whether to deploy the fail2ban config or not
* `gitea_fail2ban_jail_maxretry`: fail2ban jail `maxretry` setting. Default: `10`
* `gitea_fail2ban_jail_findtime`: fail2ban jail `findtime` setting. Default: `3600`
* `gitea_fail2ban_jail_bantime`: fail2ban jail `bantime` setting. Default: `900`
* `gitea_fail2ban_jail_action`: fail2ban jail `action` setting. Default: `iptables-allports`

### Oauth2 provider configuration

* `gitea_oauth2_enabled`: Enable the Oauth2 provider (true/false)
* `gitea_oauth2_jwt_secret`: Oauth2 JWT secret. Can be generated with ``gitea generate secret JWT_SECRET``

### GIT LFS configuration
* `gitea_lfs_enabled`: Enable GIT LFS (large filesystem)
* `gitea_lfs_mode`: should lfs be in offline mode (true/false)
* `gitea_lfs_secret`: JWT secret for remote LFS usage 

### Metrics endpoint configuration

* `gitea_metrics_enabled`: Enable the metrics endpoint
* `gitea_metrics_token`: Bearer token for the Prometheus scrape job

### Repository Indexer configuration

* `gitea_repo_indexer_enabled`: Whether to enable the repository indexer (code search). Default: `false`
* `gitea_repo_indexer_include`: Glob patterns to include in the index (comma-separated list). Default: `""` (all files)
* `gitea_repo_indexer_exclude`: Glob patterns to exclude from the index (comma-separated list). Default: `""` (no files)
* `gitea_repo_exclude_vendored`: Exclude vendored files from the index. Default: `true`
* `gitea_repo_indexer_max_file_size`: Maximum size of files to be indexed (in bytes). Default: `1048576` (1 MB)

### backup on upgrade
* `gitea_backup_on_upgrade`: Optionally a backup can be created with every update of gitea. Default: `false`
* `gitea_backup_location`: Where to store the gitea backup if one is created with this role. Default: `{{ gitea_home }}/backups/`

## Contributing
Don't hesitate to create a pull request, and when in doubt you can reach me on
Twitter [@thomas_maurice](https://twitter.com/thomas_maurice).

I'm happy to fix any issue that's been opened, or even better, review your pull requests :)

## Testing
Testing uses [molecule](https://molecule.readthedocs.io/en/stable-1.22/usage.html). To start the
tests, install the dependencies first. I would recommend you use [a virtual env](https://virtualenv.pypa.io/en/latest/) for that but who am I to tell you what to do.

```
pip install pew # install pew to manage the venvs
pew new ansible # create the venv
pip install -r requirements-travis.txt # install the requirements
molecule test # Run the actual tests
```

Note: you need Docker installed

### Known testing limitations
Currently it's mainly validating that the playbook runs, the lint is ok, and that kind of things.
Since it runs in Docker, we currently have no way to check if the service is actually launched by systemd
and so on. This has to be worked on.

## License
```
Copyright 2019-present Thomas Maurice

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
